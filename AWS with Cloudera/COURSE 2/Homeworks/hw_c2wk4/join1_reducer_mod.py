#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
#This reducer code will input a <word, value> input file, and join words together
# Note the input will come as a group of lines with same word (ie the key)
# As it reads words it will hold on to the value field
#
# It will keep track of current word and previous word, if word changes
#   then it will perform the 'join' on the set of held values by merely printing out 
#   the word and values.  In other words, there is no need to explicitly match keys b/c
#   Hadoop has already put them sequentially in the input 
#   
# At the end it will perform the last join
#
#
#  Note, there is NO error checking of the input, it is assumed to be correct, meaning
#   it has word with correct and matching entries, no extra spaces, etc.
#
#  see https://docs.python.org/2/tutorial/index.html for python tutorials
#
#  San Diego Supercomputer Center copyright
# --------------------------------------------------------------------------

prev_word          = "  "                #initialize previous word  to blank string
months             = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Nov','Dec']

dates_to_output    = [] #an empty list to hold dates for a given word
day_cnts_to_output = [] #an empty list of day counts for a given word
# see https://docs.python.org/2/tutorial/datastructures.html for list details

line_cnt           = 0  #count input lines


lis = \
["burger\t15",
"burger\tFeb-23 5",
"burger\tMar-08 2"]

lis = ['Hourly_Show\tABC',
       'Hourly_Show\tABd',
       'Hourly_Show2\tABd',
       'Hourly_Show3\tABC',
       'Hourly_Show\t1','Hourly_Show\t9',
       'Hourly_Show3\t13']

ABC_shows = []
input_standard = sys.stdin.readlines() # save the sys.stdin
#input_standard = sys.stdin.read() # only get one line
#input_standard = sys.stdin.readline() # get all file as one string


# input_standard = ['Baked_News\t641\n', 'Baked_News\t655\n', 'Baked_News\t673\n', 'Baked_News\t677\n', 'Baked_News\t68\n', 'Baked_News\t683\n', 'Baked_News\t694\n', 'Baked_News\t73\n', 'Baked_News\t74\n', 'Baked_News\t75\n',
#                   'Baked_News\t760\n', 'Baked_News\t768\n', 'Baked_News\t771\n', 'Baked_News\t785\n', 'Baked_News\t788\n', 'Baked_News\t806\n', 'Baked_News\t81\n', 'Baked_News\t816\n', 'Baked_News\t836\n', 'Baked_News\t837\n', 'Baked_News\t843\n', 'Baked_News\t858\n', 'Baked_News\t865\n', 'Baked_News\t873\n',
#                   'Baked_News\t876\n', 'Baked_News\t883\n', 'Baked_News\t886\n', 'Baked_News\t89\n', 'Baked_News\t893\n', 'Baked_News\t907\n', 'Baked_News\t908\n', 'Baked_News\t92\n', 'Baked_News\t922\n', 'Baked_News\t925\n',
#                   'Baked_News\t935\n', 'Baked_News\t946\n', 'Baked_News\t988\n', 'Baked_News\t99\n', 'Baked_News\tABC\n', 'Baked_News\tBAT\n', 'Baked_News\tBAT\n', 'Baked_News\tBOB\n', 'Baked_News\tCNO\n', 'Baked_News\tDEF\n',
#                   'Baked_News\tDEF\n', 'Baked_News\tMAN\n', 'Baked_News\tNOX\n', 'Baked_News\tXYZ\n', 'Baked_Show\t1001\n', 'Baked_Show\t1004\n']

for line in input_standard:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1
    # print(line)
    #note: for simple debugging use print statements, ie:
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item

    import re
    t = re.search('ABC',value_in)
    # t = re.search('[a-zA-Z]',value_in)
    # t is not None ## value_in is three leters
    # print(t is not None)
    if (t is not None):
        ABC_shows.append(curr_word)
# print(ABC_shows)
# ABC_shows
shows_ct = []
# array_shows_ct = ct[][]
for line in input_standard:
    line       = line.strip()       #strip out carriage return
    key_value  = line.split('\t')   #split line, into key and value, returns a list
    line_cnt   = line_cnt+1
    # print(line)
    #note: for simple debugging use print statements, ie:
    curr_word  = key_value[0]         #key is first item in list, indexed by 0
    value_in   = key_value[1]         #value is 2nd item
    import re
    # print(value_in)
    t = re.search('[0-9]',value_in)
    if ((curr_word in ABC_shows) & (t is not None)):
        # print((curr_word,value_in))
        shows_ct.append((curr_word,value_in))
        # print(curr_word)

name_arr = [x[0] for x in shows_ct]
ct_arr = [x[1] for x in shows_ct]

for show in ABC_shows:
    # show = 'Hourly_Show'
    ### contains select list by true false
    tmr = filter(lambda x: x[0] in show,shows_ct)
    ct_show = sum([int(x[1]) for x in tmr])
    print('{0} {1}'.format(show,ct_show))
