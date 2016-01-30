# Goal of the programming assignment

# gennum files contain show names and their viewers, genchan files contain show names and their channel. We want to find out the total number of viewer across all shows for the channel BAT.
# Read shows files

# gennum files contains show names and number of viewers, you can read into Spark all of them with a pattern matching, see the ? which will match either A, B or C:

show_views_file = sc.textFile(
	"/user/cloudera/input_join_mod/join2_gennum?.txt")

show_views_file.take(2)

# Remember you can check what Spark is doing by copying some elements of an RDD back to the driver:

# show_views_file.take(2)

# will return the first 2 elements of the dataset:

# [u'Hourly_Sports,21', u'PostModern_Show,38']

# Parse shows files

# Next you need to write a function that splits and parses each line of the dataset.

def split_show_views(line):
    # split the input line in word and count on the comma
    list_string = line.split(",")
    # turn the count to an integer
    out = list_string[0],list_string[1]
    return out # (show, views)
# line = [u'Hourly_Sports,21', u'PostModern_Show,38']
# split_show_views(line[0])



# Then you can use this function to transform the input RDD:

show_views = show_views_file.map(split_show_views)

# By now you should know how to check that the show_views RDD is how you expect.
# Read channel files

# genchan files contains show names and channel, you can read into Spark all of them with a pattern matching, see the ? which will match either A, B or C:

show_channel_file = sc.textFile("/user/cloudera/input_join_mod/join2_genchan?.txt")

# Parse channel files

# Write a function to parse each line of the dataset:

def split_show_channel(line):
    list_string = line.split(",")
    # turn the count to an integer
    out = list_string[0],list_string[1]
    return out # (show, channel)

# Use it to parse the channel files:
line = 'Hourly_Sports,DEF'
show_channel = show_channel_file.map(split_show_channel)
show_channel.take(2)



# Join the 2 datasets

# At this point you should use the join transformation to join the 2 dataset using the show name as the key.

# You can join the datasets in any order, as long as you are consistent, both are fine.

joined_dataset = show_channel.join(show_views)
joined_dataset.take(2)
# show_views_channel = joined_dataset.collect()


# Extract channel as key

# You want to find the total viewers by channel, so you need to create an RDD with the channel as key and all the viewer counts, whichever is the show.

def extract_channel_views(show_views_channel):

    show = show_views_channel[0]
    channel = show_views_channel[1][0]
    views = int(show_views_channel[1][1])
    return (channel, views)

# show_views_channel = (u'PostModern_Cooking', (u'DEF', u'415'))
# extract_channel_views(show_views_channel)


# Now you can apply this function to the joined dataset to create an RDD of channel and views:

channel_views = joined_dataset.map(extract_channel_views)
channel_views.take(2) ## key, value
# Sum across all channels

# Finally, we need to sum all of the viewers for each channel:

## Reduce @@@
def some_function(a, b):
    sum_out = a[1]+b[1]
    return sum_out

# This is the final stage of your analysis, so you can copy the results back to the Driver with collect:
channel_views.take(2)


test_reduce = [(u'DEF', 1038), (u'DEF', 415)]
## channel_views.collect()
test_reduce_res = reduce(some_function,test_reduce)
test_reduce_res

# data = channel_views.collect()
# test_reduce_sc = sc.parallelize(data)
# # test_reduce_sc.reduceByKey(sum)

channel_reduce_views = channel_views.reduceByKey(lambda x, y: x + y).collect()


# Submit one line for grading

# Finally, you need to create a text file with just one line for submission.

# From the Cloudera VM, open the text editor from Applications > Accessories > gedit Text Editor.

# Paste 1 single number into gedit, the number of viewers for the BAT channel, with no punctuation, spaces, commas. Just the digits of the number.

# In gedit, click on the Save button and save it in the default folder (/home/cloudera) with the name bat_viewers.txt

# Open now the browser within the Cloudera VM, login to coursera, and upload that file for grading.
# How to submit

# When you're ready to submit, you can upload files for each part of the assignment on the "My submission" tab.
# Spark Lesson 3
# Previous Item
# Back to Course Outline
# Outline