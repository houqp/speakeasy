from distutils.core import setup

setup(name='speakeasy',
    version='0.0.7',
    description='Metrics aggregation server',
    author='Eric Wong',
    packages=['speakeasy', 'speakeasy.emitter'],
    scripts=['bin/speakeasy'],
    )
