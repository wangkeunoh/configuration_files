#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import re


def decryptor(given_name, key) :
    decrypted = ""
    #flow
    f_ori = open("./" + given_name, 'r')
    while True:
        line = f_ori.readline()
        if not line: break

        for a in line:
            tmp = ord(a)
            if tmp < 96 or tmp == 118:
                tmp = tmp - 32

            tmp = tmp - key
            if tmp < 0:
                tmp = tmp + 127
            decrypted = decrypted + chr(tmp)
        decrypted = decrypted + '\n'

        if 'mobiledata_tp.dat' in given_name :
            f_analysis_mobiledata_tp = open(given_name + "__decrypt", 'w').write(decrypted + '\n')
        elif 'mobiledata_tp2.dat' in given_name :
            f_analysis_mobiledata_tp2 = open(given_name + "__decrypt", 'w')
            f_analysis_mobiledata_tp2.write(decrypted + '\n')
        elif 'mobiledata_dns.dat' in given_name :
            f_analysis_mobiledata_dns = open(given_name + "__decrypt", 'w')
            f_analysis_mobiledata_dns.write(decrypted + '\n')
def search(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename):
            search(full_filename)
        else :
            if ('mobiledata_tp.dat' in filename) :
                print(filename)
                decryptor(os.path.join(dirname, filename), 54)
            elif ('mobiledata_tp2.dat' in filename) :
                print(filename)
                decryptor(os.path.join(dirname, filename), 54)
            elif ('mobiledata_dns.dat' in filename) :
                print(filename)
                decryptor(os.path.join(dirname, filename), 54)

def deleteall(dirname):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        if os.path.isdir(full_filename) :
            deleteall(full_filename)
        else :
            if ('__decrypt' in filename) :
                os.remove(full_filename)
                print("delte pre-exist files")


#main
#search file
#decrypt
deleteall("./")
search("./")


