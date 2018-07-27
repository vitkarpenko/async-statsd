from distutils.core import setup

setup(
    name='async-statsd',
    version='0.1.4',
    description='Модуль для асинхронной отправки метрик в Statsd по UDP',
    packages=['async_statsd'],
    license='MIT License',
    long_description=open('README.md').read(),
    author='Vitaly Karpenko',
    author_email='vitkarpenko@gmail.com',
    url='https://github.com/vitkarpenko/async-statsd',
    install_requires=[
        'aiojobs'
    ],
    python_requires='>=3.6',
)