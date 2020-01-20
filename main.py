#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, os

from countOccurence import CountOccurence

class Main():
    def __init__(self, ):
        #set a default value of strings for testing
        if "STRINGS_TEST" in os.environ:
            self.strings = os.environ['STRINGS_TEST']
        else:
            self.strings = "aba,baba,aba,xzxb"

    def create_sysargv(self, ):
        """ 
            create fake call of current script for testing
        """
        sys.argv = [
            "motion-processing",
            "aba,xzxb,ab"
        ]

    def runMain(self, ):
        if len(sys.argv) < 2:
            self.create_sysargv()

        queries = sys.argv[1].split(",")

        algo = CountOccurence(self.strings.split(","))
        algo.splitInputFormat(queries)

if __name__ == "__main__":
    m = Main()
    m.runMain()