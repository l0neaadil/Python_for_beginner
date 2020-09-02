# The join() method takes all items in an iterable and joins them into one string. 
# A string must be specified as the separator.
# syntax:   string.join(iterable)


list = ['hope', 'is', 'a', 'good', 'thing']
print(list)
print(' '.join(list))             
print('_'.join(list))


# Note: When using a dictionary as an iterable, the returned values are the keys, not the values.