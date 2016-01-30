#!/usr/bin/env python   
#the above just indicates to use python to intepret this file

# ---------------------------------------------------------------
#This mapper code will input a line of text and output <word, 1>
# 
# ---------------------------------------------------------------

import sys             #a python module with system functions for this OS

## 
import os


## on hadoop 
## myid=os.environ["gwx_test_map1"] 
## on unix
myid='pipe_test' 

mylog=open("/tmp/mymaplog"+myid,"w") 
## 




# ------------------------------------------------------------
#  this 'for loop' will set 'line' to an input line from system 
#    standard input file
# ------------------------------------------------------------
for line in sys.stdin:  


# gwx 
	

#-----------------------------------
#sys.stdin call 'sys' to read a line from standard input, 
# note that 'line' is a string object, ie variable, and it has methods that you can apply to it,
# as in the next line
# ---------------------------------
    line = line.strip()  #strip is a method, ie function, associated
                         #  with string variable, it will strip 
                         #   the carriage return (by default)
    mylog.write(line) #instead of line, you could put any string or string + str(integer) in there.                     
    keys = line.split()  #split line at blanks (by default), 
                         #   and return a list of keys
    for key in keys:     #a for loop through the list of keys
        value = 1        
        mylog.write(key)
        print('{0}\t{1}'.format(key, value) ) #the {} is replaced by 0th,1st items in format list
                            #also, note that the Hadoop default is 'tab' separates key from the value


mylog.close() 
	