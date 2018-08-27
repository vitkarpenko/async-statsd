## Module for processing metrics to Statsd by UDP with asyncio

### Install
```
pip install git+https://github.com/vitkarpenko/async-statsd.git@branch
```

### Usage
```python
from async_statsd import Statsd
statsd = Statsd(
    # Host and port of Statsd server
    address=('127.0.0.1', 8125),
    # Metric will be saved by 
    # stats.{prefix}.{metric_name} address
    prefix='test',
    # Maximum number of metrics in the pool
    # When the maximum pool size is reached, 
    # all metrics will be sent to Statsd by UDP
    pool_capacity=1000,
    # Period in seconds when client will send 
    # all metrics from pool to Statsd,
    # even when pool is not full
    flush_interval=5,
    # aiojobs's scheduler instance (optional)
    scheduler=app['AIOJOBS_SCHEDULER']
)
await statsd.connect()
with statsd.timer('iseedeadpeople'):
    # your charming code 
```