#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 15:35:46 2019

@author: prathibha
"""

import sys
import math

#distance calculaton between two points  
def dist(point1, point2):
    
    value= math.sqrt((float(point1[0])-float(point2[0]))**2 + (float(point1[1])-float(point2[1]))**2 + (float(point1[2])-float(point2[2]))**2)
    return value;


#Initialization of lists for storing the points from the files
one=[] #uncompressed 
two=[] #decompressed A 
three=[] #decompressed B
four=[] #decompressed C


#Input files are stored in tsv format
       
with open('/Users/prathibha/Documents/Teraki3DRecruitmentTestApr19/input/Car_XYZI_uncompressed_ASCII.tsv', 'r') as f:
    lines=f.readlines() 
    for line in lines[:-1]:
        x,y,z,a = line.split()
        one.append((x,y,z,a))  #Addition of the points from uncompressed tsv to list 'one'
   
with open('/Users/prathibha/Documents/Teraki3DRecruitmentTestApr19/input/Car_XYZI_decompressed_ASCII_A.tsv', 'r') as f:
    lines=f.readlines()
    for line in lines[:-1]:
        x,y,z,a = line.split()
        two.append((x,y,z,a))   #Addition of the points from decompressed A tsv to list 'two'

 
with open('/Users/prathibha/Documents/Teraki3DRecruitmentTestApr19/input/Car_XYZI_decompressed_ASCII_B.tsv', 'r') as f:
    lines=f.readlines()
    for line in lines[:-1]:
        x,y,z,a = line.split()
        three.append((x,y,z,a))   #Addition of the points from decompressed B tsv to list 'three'
        
 
with open('/Users/prathibha/Documents/Teraki3DRecruitmentTestApr19/input/Car_XYZI_decompressed_ASCII_C.tsv', 'r') as f:
    lines=f.readlines()
    for line in lines[:-1]:
        x,y,z,a = line.split()
        four.append((x,y,z,a))    #Addition of the points from decompressed C tsv to list 'four'
        
     
with open('/Users/prathibha/Documents/Teraki3DRecruitmentTestApr19/output/outputfile.tsv', 'w') as f:
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
print("Average distance between the points sets of Uncompressed and Decompressed A" ,sumA)
print("Average distance between the points sets of Uncompressed and Decompressed B" ,sumB)
print("Average distance between the points sets of Uncompressed and Decompressed C" ,sumC)
dict={}
dict[sumA]="A"
dict[sumB]="B"
dict[sumC]="C"
print(dict)
print("Best compression Technique : " ,dict[min(sumA,sumB,sumC)])  
print("Worst compression Technique : " ,dict[max(sumA,sumB,sumC)]) 
