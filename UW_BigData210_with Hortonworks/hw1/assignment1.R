assignment1_out <- read.delim("~/Documents/d/Dropbox/Bigdata/AWS_HDP/assignment1_out.txt", header=FALSE, quote="")
assigment1_in <- read.table("~/Documents/d/Dropbox/Bigdata/AWS_HDP/assigment1_in.dat", quote="\"")

merge(assigment1_in,assignment1_out)
