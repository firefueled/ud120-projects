#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL', 0)
data = featureFormat(data_dict, features)

import math
listy = []
for item in data_dict.keys():
  if data_dict[item]['salary'] != 'NaN':
    listy.append((item, data_dict[item]['salary'], data_dict[item]['exercised_stock_options'], data_dict[item]['poi']))

# for point in data:
#     salary = point[0]
#     bonus = point[1]
#     matplotlib.pyplot.scatter( salary, bonus )

print 'list: ', sorted(listy, key = lambda t: t[1] , reverse = True)

# matplotlib.pyplot.xlabel("salary")
# matplotlib.pyplot.ylabel("bonus")
# matplotlib.pyplot.show()
