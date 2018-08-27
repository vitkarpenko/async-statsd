from distutils.core import setup

setup(
    name='async-statsd',
    version='0.1.4',
    description='Module for processing metrics to Statsd by UDP with asyncio',
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