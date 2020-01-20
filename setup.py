#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import re
import os

from setuptools import setup
from _version import __version__

def get_lib_version():
    """
        Extract version list from versionList.txt file
    """
    with open("_versionList.txt", "r") as f:
        l_ver = f.read().splitlines()
    return l_ver

def find_packages(path="."):
    ret = []
    for root, _, files in os.walk(path):
        if "__init__.py" in files:
            ret.append(re.sub("^[^A-z0-9_]+", "", root.replace("/", ".")))
    return ret

readme = open("./README.md").read()
l_install_requires = get_lib_version()
l_package = find_packages()
l_package = list(filter(None, l_package))

setup(
    name="countOccurence",
    description="countOccurence package",
    version= __version__,

    url="",
    author="CBA",
    author_email="chaikou.balde@toto.com",
    license="OS",
    # List of all script to add
    packages=l_package,

    # take in consideration MANIFEST.in
    include_package_data=True,
    # List of all lib to add with version number
    install_requires=l_install_requires,
    # README description
    long_description=readme,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 0",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3.6",
        "Topic :: Communications",
    ],
    zip_safe=False,
)
