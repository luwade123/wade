from errno import ESTALE
from posixpath import split
from re import A
from numpy import record
from scapy.all import *
from scipy import stats
import os
path = 'new/'

allFileList = os.listdir(path)
for file in allFileList:
    file_name = 'new/'+file
    f1 = open(file_name,'r')
    tmp = file.split('.')
    tmp2 = tmp[0] + '_trimmean.txt'
    file2 = 'new/' + tmp2
    f2 = open(file2,'w')
    record_list = {}

    for string in f1:
        if('d:' in string):
            tmp = string
        if("all" in string):
            tmp2 = string.split('all')
            tmp3 = tmp2[1].split('[')
            tmp4 = tmp3[1].split(']')
            tmp5 = tmp4[0].split(',')
            record_list[tmp] = tmp5

    for i in record_list.keys():
        tmp = []
        for j in record_list[i]:
            tmp.append(float(j))
        print(i,file=f2)
        print(stats.trim_mean(tmp,0.1),'\n',file=f2)
    for i in record_list.keys():
        print(i,record_list[i])
        