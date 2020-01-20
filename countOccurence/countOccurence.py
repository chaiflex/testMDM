# !/usr/bin/env python3
# -*- coding: utf-8 -*-

__all__ = ["CountOccurence"]

class CountOccurence():
    def __init__(self, strings:list):
        self.strings = strings

    def matchingStrings(self, input_string:list, queries:list ):
        """
            return an array of integers representing the frequency of occurrence of each query string in strings

            Input:
                input_string : an array of strings to search 
                queries : an array of query strings 
            
            Output:
                Return dict of occurence
        """

        list_occ = [input_string.count(current_string) for current_string in queries]
        return dict(zip(queries, list_occ))


    def splitInputFormat(self, queries: list):
        """ 
            Print the result of matchingStrings

            Input:
                queries : an array of query strings 

            Output:
                None
        """
        
        def getSize(queries ):
            return len(self.strings), len(queries)
        size_input_string, size_queries = getSize(queries, )
        dict_occurence = self.matchingStrings(self.strings, queries)
        print(f"{dict_occurence}")
    
if __name__ == "__main__":
    print("CountOccurence class")
