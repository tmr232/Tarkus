from setuptools import setup, find_packages
import os


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='Tarkus',
    version='0.9',
    packages=find_packages(),
    scripts=["scripts/tarkus.bat"],
    install_requires=['docopt', 'pip', 'GitPython', 'PyYAML', 'attrdict'],
    url='https://github.com/tmr232/Tarkus',
    license='MIT',
    author='Tamir Bahar',
    author_email='',
    description='IDA Pro Plugin Manager',
    long_description=(read('README.rst')),
    include_package_data=True,
)
