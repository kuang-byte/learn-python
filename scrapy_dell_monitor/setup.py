"""Setup script."""

from setuptools import setup, find_packages

PYPI_PKG_NAME = 'scrapy-dell-monitor'
PACKAGES = find_packages()
INSTALL_REQUIRES = []
version = "0.0.1"

setup(
    name=PYPI_PKG_NAME,
    version=version,
    description='Track Dell monitor price',
    url='',
    author='Hao Kuang',
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    tests_require=['pytest', 'pytest-cov', 'mock'],
)
