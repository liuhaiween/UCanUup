#!/usr/bin/env python
#coding=utf-8
import urllib2

HOST="http://106.75.28.160/UCloud.txt#rd?nsukey=%2BAhDBz%2BtXRAZc4U7S0%2Ft2S8cPsPtXunmzmNO6ZSv5ZnkOdm6x4%2BDgZc1U3L1lyG7E50EPMeYl0bNsftNpUYp8w%3D%3D"
print urllib2.urlopen(HOST).read().count("UCanUup")