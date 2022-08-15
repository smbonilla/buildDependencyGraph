#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#
class BuildConnections:
    def __init__(self, cities):
        self.adjList = {}
        
        for city in cities:
            if city[0] not in self.adjList.keys():
                self.adjList[city[0]] = []
            if city[1] not in self.adjList.keys():
                self.adjList[city[1]] = []
            
            self.adjList[city[0]].append(city[1])
            self.adjList[city[1]].append(city[0])

def roadsAndLibraries(n, c_lib, c_road, cities):
    
    cost = 0
    
    libraries = []
    
    connections = dict()
    print(connections)
    
    citiesDict = BuildConnections(cities)
    
    # check all cities in n
    for city in range(n):
        
        # if no libraries exist, add a library to node
        if not libraries:
            cost += c_lib
            libraries.append(city)

        # check if city does have a connection to any library, if it does 
        # have a connection then pass 
        elif hasPath(connections, city, libraries):
            pass
            
        else:
            
            # if cost of building is less than a road, build a library in the 
            # city and add cost of building to total 
            if c_lib < c_road:
                cost += c_lib
                libraries.append(city)
            
            else: 
                
                # for all possible neighbors of this city, check if that      
                # neighbor has a path to a library and if so build a road to 
                # that city
                for possibleNeighbor in cities[city]:
                    if hasPath(citiesDict.adjList, possibleNeighbor, libraries):
                        cost += c_road
                        connections[city] = possibleNeighbor
    
    return cost

def hasPath(connections, city, libraries):
    
    print(connections.keys())
    if (not connections.keys()) or (city not in connections.keys()):
        print(connections.keys())
        return False
    
    else:
        # loop through libraries to check if city has a connection to any               library
        for library in libraries:
            
            # if city is library, return True
            if city == library:
                return True
            
            else:
                for neighbor in connections[city]:
                    if hasPath(connections, neighbor, libraries):
                        return True

if __name__ == '__main__':

    cities = [[1, 2], [3, 1], [2, 3]]

    n = 3

    m = 3

    c_lib = 2

    c_road = 1

    result = roadsAndLibraries(n, c_lib, c_road, cities)
