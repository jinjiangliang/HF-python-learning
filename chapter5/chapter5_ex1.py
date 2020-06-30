"""ShenRuQianChu Chapter 5 excise 1
Let’s begin by reading the data from each of the files into its own list. Write a short program to
process each file, creating a list for each athlete’s data, and display the lists on screen.

"""

## read james.txt as james;
with open("james.txt", 'r') as james:
    data = james.readline()

james_record = data.strip().split(',')

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

# create new empty list
clean_james=[]

# take each item in the record
for each_t in james_record:
    clean_james.append(sanitize(each_t))

print(sorted(clean_james))
#print(sorted(james_record))

"""
with open("james.txt",'r') as james:
    for each_line in james:
        print('James Record' )
        james_list=each_line.split(',')
        for each_record in james_list:
            each_record=each_record.strip()
            print(each_record)
"""
