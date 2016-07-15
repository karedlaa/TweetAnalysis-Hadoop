#!/usr/bin/python

import sys

years_dict = {}
for line in sys.stdin:
  (key,val) = line.strip().split('\t')
  if not(key in years_dict.keys()): 
    years_dict[key] = 1
  else:
    years_dict[key] += 1

for year in years_dict.keys():
  print year, years_dict[year]
