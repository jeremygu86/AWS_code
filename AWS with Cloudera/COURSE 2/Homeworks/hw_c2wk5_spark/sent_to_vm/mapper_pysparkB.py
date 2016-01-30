## For fileB

def split_fileB(line):
    # split the input line into word, date and count_string
    import re
    line = 'Dec-15 able,100'
    # line.split(","|" ")
    out = re.split(' |,',line)
    word = out[1]
    date = out[0]
    count_string = str(out[2])
    return (word, date + " " + count_string)

#line = "able,991"
#split_fileA(line)

# lineB = 'Dec-15 able,100'
# split_fileB(lineB)