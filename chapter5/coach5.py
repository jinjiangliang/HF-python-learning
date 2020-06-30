
def sanitize(time_string):
    # record different splitter for replacement
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

def get_coach_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File Error: '+ioerr)
        # to indicate the failure
        return(None)

sarah = get_coach_file('sarah.txt')

# sort the first 3 fastest; set() to ensure the uniqueness of the list [].
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
