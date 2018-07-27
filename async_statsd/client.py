import asyncio
from contextlib import contextmanager
from time import time

from typing import Tuple

from aiojobs import create_scheduler
from aiojobs import Scheduler


class Statsd:
    """ Осуществляет асинхронную отправку статистики в Statsd по UDP.

    Копит метрики в пуле, отправляет при достижении максимального объёма пула ::pool_size::
    и с определённой периодичностью в секундах ::send_period::
    """
    def __init__(
        self,
        address: Tuple[str, int] = ('127.0.0.1', 8125),
        prefix: str = '',
        pool_capacity: int = 5000,
        flush_interval: int = 10,
        scheduler: Scheduler = None
    ):
        self.address = address,
        self.prefix = prefix
        self.pool_capacity = pool_capacity
        self.flush_interval = flush_interval
        self.scheduler = scheduler
        self.messages = list()
        self.transport = None
        self.protocol = None

    async def connect(self):
        loop = asyncio.get_event_loop()
        self.transport, self.protocol = await loop.create_datagram_endpoint(
            asyncio.DatagramProtocol, remote_addr=self.address
        )
        if not self.scheduler:
            self.scheduler = await create_scheduler()
        await self.scheduler.spawn(self.periodic_flush())

    def close(self):
        self.transport.close()

    def flush(self):
        if self.transport and self.messages:
            packet = '\n'.join(self.messages)
            self.messages = list()
            self.transport.sendto(packet.encode())

    async def periodic_flush(self):
        while True:
            await asyncio.sleep(self.flush_interval)
            self.flush()

    def send_timer(self, name: str, duration: int) -> None:
        self._push_message(f'{name}:{duration}|ms')

    def send_counter(self, name: str, count: int) -> None:
        self._push_message(f'{name}:{count}|c')

    def _push_message(self, message: str):
        self.messages.append(f'cct_{self.prefix}.{message}')
        if len(self.messages) >= self.pool_capacity:
            self.flush()

    @contextmanager
    def timer(self, name: str) -> None:
        start = time()
        try:
            yield
        finally:
            # Statsd ждёт микросекунды, time() возвращает секунды
            duration = round((time() - start) * 1000)
            self.send_timer(name, duration)
