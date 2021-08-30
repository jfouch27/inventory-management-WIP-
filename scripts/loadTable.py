import glob
import os
from polls.models import Host
HostTable=[]
def run():
  for file in glob.glob('~/djangoProjects/mysiteOne/test.txt'):
    #newfile = open('test.txt', 'r')
        with open(file,'r') as i:
            fileLines = i.readlines()
            print("Hello")