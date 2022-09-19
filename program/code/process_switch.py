from errno import ESTALE
from posixpath import split
from re import A
from numpy import record
from scapy.all import *
from scipy import stats
import os
path = 'bar/better/tmp2'

allFileList = os.listdir(path)
for file in allFileList:
    file_name = 'bar/better/tmp2/'+file
    f1 = open(file_name,'r')
    tmp = file.split('.')
    tmp2 = tmp[0] + '_trimmean.txt'
    file2 = 'bar/better/tmp2/' + tmp2
    f2 = open(file2,'w')
    record_list = {}
    name_list = ['2-1','2-2','3-1','3-2','3-3']
    k_list=[]
    two_one = {}
    two_two = {}
    three_one = {}
    three_two = {}
    three_three = {}
    all_in_one=[two_one,two_two,three_one,three_two,three_three]
    for string in f1:
        if('d:' in string):
            tmp = string
            k_list.append(tmp)
        if(len(string)>6):
            if("2-1" in string):
                tmp2 = string.split('2-1')
                tmp3 = tmp2[1].split('[')
                tmp4 = tmp3[1].split(']')
                tmp5 = tmp4[0].split(',')
                two_one[tmp] = tmp5
            if("2-2" in string):
                tmp2 = string.split('2-2')
                tmp3 = tmp2[1].split('[')
                tmp4 = tmp3[1].split(']')
                tmp5 = tmp4[0].split(',')
                two_two[tmp] = tmp5
            if("3-1" in string):
                tmp2 = string.split('3-1')
                tmp3 = tmp2[1].split('[')
                tmp4 = tmp3[1].split(']')
                tmp5 = tmp4[0].split(',')
                three_one[tmp] = tmp5
            if("3-2" in string):
                tmp2 = string.split('3-2')
                tmp3 = tmp2[1].split('[')
                tmp4 = tmp3[1].split(']')
                tmp5 = tmp4[0].split(',')
                three_two[tmp] = tmp5
            if("3-3" in string):
                tmp2 = string.split('3-3')
                tmp3 = tmp2[1].split('[')
                tmp4 = tmp3[1].split(']')
                tmp5 = tmp4[0].split(',')
                three_three[tmp] = tmp5
            

    for i in k_list:
        print(i,file=f2)
        for index,j in enumerate(all_in_one):
            tmp = []
            print(i,index,j)
            for k in j[i]:
                if(k!=''):
                    tmp.append(float(k))
            print(name_list[index],file=f2)
            print(stats.trim_mean(tmp,0.1),'\n',file=f2)

        