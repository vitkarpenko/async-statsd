from distutils.core import setup

setup(
    name='async-statsd',
    version='0.1.0',
    description='Модуль для асинхронной отправки метрик в Statsd по UDP',
    packages=['async_statsd'],
    license='MIT License',
    long_description=open('README.md').read(),
    install_requires=[
        'aiojobs'
    ],
    python_requires='>=3.6',
)