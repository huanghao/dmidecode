from setuptools import setup

import dmidecode

setup(
    name="dmidecode",
    version=dmidecode.__version__,
    py_modules=["dmidecode"],
    license='MIT',
    platforms='linux',
    )
