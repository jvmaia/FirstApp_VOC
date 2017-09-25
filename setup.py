from setuptools import setup

setup(
    name='firstapp',
    version='0.0.1',
    packages=['firstapp'],
    options={
        'app': {
            'formal_name':'FirstApp',
            'bundle':'org.pybee.demo',
        }
    }
)
