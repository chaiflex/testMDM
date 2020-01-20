#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import re
import os

from setuptools import setup

from _version import __version__

def set_lib_version(requires):
    """
        Have to be use to update the versionList.txt file
    """
    std = subprocess.Popen(
        r"python3 -m pip freeze -l",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    l_ver = [line.decode("utf-8")[:-1] for line in std.stdout.readlines()]   

    #get lib version
    temp_l = []
    for pat in requires:
        regex = re.compile("(" + pat + ")==.*")
        temp = [
            lib_version
            for lib_version in l_ver
            for m in [regex.search(lib_version.lower())]
            if m
        ]
        if len(temp) != 0:
            temp_l.append(temp[0])
    l_ver = temp_l

    print(">>> - Library to add to _versionList.txt file : ")
    print(*l_ver, sep='\n')

    #if file already exist, delete it
    if os.path.isfile("_versionList.txt"):
        os.remove("_versionList.txt")

    with open("_versionList.txt", "w") as f:
        for item in l_ver:
            f.write("%s\n" % item)

    print(">>> - Element save in file")

if __name__ == "__main__":

    requires = [
        "numpy",
    ]
    set_lib_version(requires)


