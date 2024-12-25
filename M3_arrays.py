"""
Scenarios:

1. Storing list of temperature readings per specific intervals
2. Storing list of stocks data
3. Storing list of speed information of car
4. Storing list of objects, list, tuple, dictionary in programming

In python lists can be used to store any other python objects. but they are generally inefficient in storage. lists are useful in following situations
To store multiple Mutable data, heterogeneous data.  Python Lists are a built in data structure.
Eg: x = [1,2,3,4]

Arrays are also used to store data, but of homogeneous or same type. they are efficient and can be mutable.
They perform best for numerical computations like ML. Array is not a built in datatype, but can be imported to use.
Eg: import array; array.array('i', 1,2,3,4,5)

Data type supported and its definitions
-----------------------
Code | Python type | min size in bytes
‘b’ int Signed char 1
‘B’ int Unsigned char 1
‘u’ Unicode character wchar_t 2
‘h’ Int Signed short 2
‘H’ int Unsigned short 2
‘i’ int Signed int 2
‘I’ int Unsigned int 3
‘l’ int signed long 4
‘L’ int Unsigned long 4
‘q’ int Signed long long 8
‘Q’ int Unsigned long long 8
‘f’ float float 4
‘d’ float double 8

Arrays need to know the datatype before its instantiated for it to allocate right size of memory.(List data type will not know the data type hence, python allocate memory for object's or references. hence they are referential arrays, so they use more memory for storing the memory locations of the referred element)

Real world Example with Array's operations and capabilities:
Storing average temperature of last couple of days
"""

import array
# create data set
temp_data = array.array('d', [72.1, 72.0, 65.0, 45.0, 55.0, 66.0, 72.0, 65.0, 74.0, 65.44, 66.5])

# Add another day's of reading
temp_data.append(74.0)

# printing 5th day's reading
print("5th day's reading", temp_data[4])

# printing last 7 days of reading
print("last 7 days of readings", temp_data[-8:-1])

# printing first 7 days of reading
print("first 7 days of readings", temp_data[:7])

# search first occurance of 65.0 temperature
print("65.0 occured first on ", temp_data.index(65.0) + 1, "th day")

# update 3rd days reading
temp_data[4] = 77.77

# merge old temperature reading data
old_temp_reading = array.array('d', [55.55, 66.66, 77.77, 88.88])
old_temp_reading.extend(temp_data)
print("complete data = ", old_temp_reading)
print("count of complete data = ", len(old_temp_reading))

# iterating through the data
for i, data in enumerate(old_temp_reading): print("day", i, "reading = ", data)

# convert to different data type
print("convert as list data type", temp_data.tolist())


