from setuptools import setup

import dmidecode

setup(
    name="dmidecode",
    version=dmidecode.__version__,
    py_modules=["dmidecode"],
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
        ],
    )
