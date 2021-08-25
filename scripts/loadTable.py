import glob
import os
from polls.models import Host
HostTable=[]
def run():
  newfile = open('test.txt', 'r')
  with open('test.txt','r') as i:
    #for file in glob.glob('~/test.txt'):
    print("1")
    fileLines = i.readlines()
        #    print(i.readLines())
  for j in range(len(fileLines)):
    HostTable.append(fileLines[j].split())
    
  for k in range(len(HostTable)):
    HostTable[k].insert(3,HostTable[k].pop(1))
  HostTable.sort()
    
  Host.Ip_address=HostTable[0][0]
  Host.inci_date=HostTable[0][1]
  Host.inci_time=HostTable[0][2]
  Host.port=HostTable[0][3]
  Host.save()
  print(Host.Ip_address)
