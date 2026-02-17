# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:15:22 2025

@author: pathouli
"""

from utils import *

the_path = "C:/Users/pathouli/Box Sync/myStuff/academia/torhea/fall_2025/data/"

file_n = "fishing/0,4570,7-153-10364-34956--,00.html_121800529000.txt"
full_path = the_path + file_n

def file_reader(p_in):
    f = open(p_in, "r")
    text = f.read()
    text = clean_txt(text)
    #print (text)
    f.close()
    return text

test_tmp = file_reader(full_path)

# ex = j("the cat jumped over the bed", 
#        "the dog chased the cat")
#print (ex)

"""create a function called word_fun that outputs a dictionary where every 
key is a unique token and the value is the number of times that token shows up
in the input corpus"""

"""red red blue purple --> {'red': 2, 'blue': 1, 'purple': 1}
"""

#test = word_fun("the cat and the dog chased the cat")
#
#https://docs.python.org/3/library/re.html
#lower case everything and replace any non letter with a " "
#https://www.asciitable.com/

#test = clean_txt(str_in)
#str_t = "The! cat and the dog123_ chased[] the cat!!"
#test_wf = word_fun(str_t)
#print (test_wf)

# f = open(full_path, "r")
# text = f.readlines()
# f.close()

#f = open(full_path, "r")
#text = f.readline()
#print (text)
#f.close()

#good for VERY large files
# with open(full_path, "r") as file:
#     while True:
#         line = file.readline()
#         print (line)
#         if not line:
#             break




