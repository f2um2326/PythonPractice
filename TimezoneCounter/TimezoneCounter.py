# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:02:46 2015

@author: shimba
"""

# Read data test

import json

# count timezone
'''
def get_counts(sequence):
    counts = {} # create empty Dictionaly var
    for x in sequence:
        if x in counts:
            counts[x] += 1  # add
        else:
            counts[x] = 1   # create item in dictionary
    return counts
'''

# more beautiful
from collections import defaultdict

def get_counts(sequence):
    counts = defaultdict(int)   # initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

# ranking
def top_counts(count_dict, n=10):
    # create list like [(count, tz), (count, tz), ... ]
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    #print value_key_pairs
    value_key_pairs.sort()
    value_key_pairs.reverse()   # from Top
    #return value_key_pairs[-n:] # from 10 to 1
    return value_key_pairs[:10]

path = '../pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
#json_str = open(path).readline()
#print json_str
records = [json.loads(line) for line in open(path)]
#print records[0]['tz']

#time_zones = [rec['tz'] for rec in records] # Key Error: 'tz'
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
#print time_zones

# Dictionary usage
'''
dic = {}
print dic
dic['America'] = 1
print dic
'''

counts = get_counts(time_zones)
#print counts['America/New_York']
#print len(time_zones)

ranking = top_counts(counts)
print ranking