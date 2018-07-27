## Модуль для асинхронной отправки метрик в Statsd по UDP

### Установка
```
pip install git+http://cri.atol.ru/bitbucket/scm/s280/asyncio-statsd.git@branch
```

### Использование
```python
statsd = Statsd(
    # хост Statsd и порт, который он слушает
    address=('127.0.0.1', 8125),
    # метрика ::metric_name:: запишется по адресу stats.{prefix}.{metric_name}
    prefix='test',
    # количество метрик в буффере.
    # при достижении указанного значения все метрики объединяются в UDP-пакет и скидываются в Statsd
    pool_capacity=1000,
    # каждый ::flush_interval:: секунд клиент будет скидывать метрики в Statsd, даже если не превышен ::pool_capacity::
    flush_interval=5
)
await statsd.connect()
with statsd.timer('iseedeadpeople'):
    # your charming code 
```