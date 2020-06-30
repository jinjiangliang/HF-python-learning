"""This file includes the idle session in chapter 5
"""

"""
# test list comprehension
mins = [1, 2, 3]
secs = [m*60 for m in mins]
print(secs)
"""

"""
lower = ['I', 'like', 'python']
upper = [s.upper() for s in lower]
print('lower is ', lower, '\n', 'upper is ', upper)
"""

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins,secs) = time_string.split(splitter)
    return(mins+'.'+secs)

dirty = ['2-22', '2:22', '2.22']
clean = [float(sanitize(t)) for t in dirty]
print('dirty is', dirty, '\nclean is ', clean)