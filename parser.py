import sys
import os
#import numpy
f = open('all.csv', "r")
lines  = f.readlines()
dic = {}

for line in lines:
  name, stars = line.split(',')
  if int(stars) >= 1313 and name not in dic:
    print name,stars
  dic[name] = stars
#print len(dic)
numset = []
for ii in dic:
  numset.append(int(dic[ii]))


numset.sort()
numset.reverse()
print len(numset)
#print numset
#for ii in range(0,10):
#  print numset[ii]
