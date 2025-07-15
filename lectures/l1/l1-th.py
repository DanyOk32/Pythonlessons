# integer, float, boolean, none, string

# -methods for lists
"""
[1,3,5,'hello']
append( add new)
 insert( add new increase size)
 pop(delete and initialization)
 copy(smthing)
 remove(First Value)
 extend(list 1 + list 2, extension)
 index(arg1= Value, arg2 = from index, arg3 = end index), if withou arg2 - find first occurence)
 reverse(reverse sides)
 sort() - ex. reverse=True (descending)
 count(Value) how many times prg match Value
 clear - clear list

 slice for lists [1:3:arg3] new list from 1 index till 3 index, without last. Arg3 - step
"""
# tuple (кортедж)
"""
(1,2,3,'hello')
index(same as lists)
count(same as lists)
list(tuple) - convert to list
"""
#dicionary(словники)
"""
{'key1':1, 'key2':'value2'}
address - dictionary['key']
dicionary.get('key', arg2) - arg2 can be indicate default value
dictionary.clear
dictionary.copy
dict.fromkeys(list, arg2) - convert list to keys in dictionary, arg2 - can me indicate default value
dictionary.items() - convert to [(key,value),(key,value)...]
values - to take values ['value1', 'value2', ...]
keys - to take key ['key1', 'key2', ...]

pop (same as list)
popitem (last added value)

setdefault(key, value) - meth check for coincidence, if it is, do nothing. If the key is not present, add it 
update - like extend. combine 2 dictionaries

-----
for k, v in d.items():
    print(f'{k=} = {v=}')   - =is not req
"""
#Set
"""
collection - delete duplicates
set - create new set
add - add new value (duplicates not be added)
pop - delere random value (coz all values in collection will сompare by hash)
issuperset/issubset - comparing 2 sets, to compare values
isdisjoint - compare values for identical value False | True 
union - to union 2 sets
intersection - return set with values that have both sets
difference - return values that have only one set
update - update set by adding another
remove - remove value
discard - like remove but without error
"""
#string
"""
string = f'text te{key1}xt text text{key2}'

index(value, startIndex, endIndex)
find - same like index, without error
count - how many times meet value
capitalize - first letter
upper - all letter
lower - all
isalnum - only letter and numb
usaplpha - only letter
isascii - ascii code
isdigit - only diigt
startswith orendswith - first letter
strip - delete 'value' from left and right, default - backspace
lstrip - left, rstrip - right
split - separate
partition - separate without deleting by first matching
replace(target, on that target)
"""
#another function
"""
min/max()
sum()
sorted() - create new array
range(a,b,c) - a-start, b-finis, c - step'
'smthin'.join() - from list to str
"""
