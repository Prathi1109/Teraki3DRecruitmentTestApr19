#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:35:46 2019

@author: prathibha
"""

import sys
import math
import argparse

#Input data
argparser = argparse.ArgumentParser(description='compression')
argparser.add_argument("--data")
argparser.add_argument("--dataA")
argparser.add_argument("--dataB")
argparser.add_argument("--dataC")
argparser.add_argument("--output")
arg = argparser.parse_args()
#function for distance calculaton between two points  
def dist(point1, point2):
    
    value= math.sqrt((float(point1[0])-float(point2[0]))**2 + (float(point1[1])-float(point2[1]))**2 + (float(point1[2])-float(point2[2]))**2)
    return value;


#Initialization of lists for storing the points from the files
one=[] #uncompressed 
two=[] #decompressed A 
three=[] #decompressed B
four=[] #decompressed C


#Input files are stored in tsv format
       
with open(arg.data, 'r') as f:
    lines=f.readlines() 
    for line in lines[:-1]:
        x,y,z,a = line.split()
        one.append((x,y,z,a))  #Addition of the points from uncompressed tsv to list 'one'
   
with open(arg.dataA, 'r') as f:
    lines=f.readlines()
    for line in lines[:-1]:
        x,y,z,a = line.split()
        two.append((x,y,z,a))   #Addition of the points from decompressed A tsv to list 'two'

 
with open(arg.dataB, 'r') as f:
    lines=f.readlines()
    for line in lines[:-1]:
        x,y,z,a = line.split()
        three.append((x,y,z,a))   #Addition of the points from decompressed A tsv to list 'three'
        
 
with open(arg.dataC, 'r') as f:
    lines=f.readlines()
    for line in lines[:-1]:
        x,y,z,a = line.split()
        four.append((x,y,z,a))    #Addition of the points from decompressed A tsv to list 'four'
        
     
with open(arg.output, 'w') as f:
    for point in one:
        nearestA = None
        nearestB = None
        nearestC = None
        distanceA = sys.float_info.max
        distanceB = sys.float_info.max
        distanceC = sys.float_info.max
        sumA=0
        sumB=0
        sumC=0;
        for point2 in two:
            d = dist(point2, point) 
            if d < distanceA:       #computing the nearest point for each in A for the re-arrangement
                distanceA = d
                nearestA = point2    
            sumA=sumA+distanceA    
        for point3 in three:
            d=dist(point3,point)
            if d< distanceB:        #computing the nearest point for each in B for the re-arrangement
                distanceB = d
                nearestB = point3
            sumB=sumB+distanceB   
        for point4 in four:
            d=dist(point4,point)    #computing the nearest point for each in C for the re-arrangement
            if d < distanceC:
                distanceC = d
                nearestC = point4   
            sumC=sumC+distanceC  
        f.write("%f %f %f %f %f %f %f\n"%(float(point[0]), float(point[1]), float(point[2]),float(nearestA[0]),float(nearestA[1]),float(nearestA[2]),float(distanceA)))
        f.write("%f %f %f %f %f %f %f\n"%(float(point[0]), float(point[1]), float(point[2]),float(nearestB[0]),float(nearestB[1]),float(nearestB[2]),float(distanceB)))
        f.write("%f %f %f %f %f %f %f\n"%(float(point[0]), float(point[1]), float(point[2]),float(nearestB[0]),float(nearestB[1]),float(nearestB[2]),float(distanceB)))
print("Maximum distance between the points sets of Uncompressed and Decompressed A" ,sumA)
print("Maximum distance between the points sets of Uncompressed and Decompressed B" ,sumB)
print("Maximum distance between the points sets of Uncompressed and Decompressed C" ,sumC)
dict={}
dict[sumA]="A"
dict[sumB]="B"
dict[sumC]="C"
#Geometric Accuracy measure: maximum distance between the point sets of uncompressed and ordered decompressed point cloud 
print("Best compression Technique : " ,dict[min(sumA,sumB,sumC)])  
print("Worst compression Technique : " ,dict[max(sumA,sumB,sumC)]) 
