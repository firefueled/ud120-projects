#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
sys.path.append("../../../30/")
from ClassifySVM import classify

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = classify(features_train, labels_train)

t0 = time()
pred = clf.predict(features_test)
# print "prediction time:", round(time()-t0, 3), "s"
# print pred[10],'-',pred[26],'-',pred[50]
i = 0
for item in pred:
  if item == 1:
    i += 1

print i

# print "Acurracy: " + str(clf.score(features_test, labels_test))



#########################################################
### your code goes here ###

#########################################################


