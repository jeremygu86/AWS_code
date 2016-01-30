## For fileA

def split_fileA(line):
    # split the input line in word and count on the comma
    list_string = line.split(",")
    # turn the count to an integer
    out = tuple(list_string[0],str(list_string[1]))

    return out
# line = "able,991"
# split_fileA(line)