#  How to get current working directory
~~~
import os
os.getcwd()
# Output: dhananjaya.singhar/Library/CloudStorage/OneDrive-MaerskGroup/Data_Science_Class/test.py
~~~

# Variable Declaration
~~~
num=10        # VALID
num123=20     # VALID
NUM=70        # VALID
num_123=200   # VALID

#num$123=100   # INVALID
#num 123=300   # INVALID
~~~

- Variables are case sinsetive
- Variables can be capital and small letter
- Variabbles doesnot allow special char
- Only '_' can be variable
- Variable doesn't contain any space between words
- Variable cannot prefix with numbers
- Variable can suffix with numbers
- variable cannot contain any keywords like if, for etc...

# Check type of Variable
~~~
num=234;
type(num)
~~~ 

- In Python we no need to define datatype while defining variable
- type(variableName) used to check the type of variable

# Types of Datatypes
- int
- str
- complex
- list
- tuple
- range
- bytes
- bytearray
- dict
- set
- frozenset
- bool
- None

## DataType: int

~~~
Decimal: 37
Binary: 0b0b100101
Octal: 0o45
Hexadecimal: 0x25
~~~

### Number System
![numberSystem.png](numberSystem.png)


### Number conversion

![binaryToDecimalConversion.png](binaryToDecimalConversion.png)

![conversion.png](conversion.png)



~~~
print(bin(37)) # 0b100101
print(oct(37)) # 0o45
print(hex(37)) # 0x25
~~~


## DataType: bool
~~~
isAvailable = True
# isAvailable = TRUE # INVALID
# isAvailable = true # INVALID

print(type(isAvailable)) # <class 'bool'>
~~~

## Type Cast functions
~~~
num = 100
num_float = float(num)   ## Convert Integer to float
num_str = str(num)  ## Convert Integer to String
bool_int = int(True) # 1 Convert boolean to int
bool_value = bool(0) # false
bool_value = bool('') # false
num = str('100.25') #  [invalid literal for int() with base 10: '100.25']
~~~
####  While converting string with float value to int , we will above get error.

---

## How to import a package in python
~~~
import random

print(dir(random)) # Show all methods inside package
# help(random.randint) # Show the method definition
~~~
### How to call methods / parameters inside package
~~~

import sys
import random
import math
import time
import keyword


print(random.randint(0, 1000)) # 780
print(sys.executable) # /opt/anaconda3/bin/python
print(keyword.kwlist) # ['False', 'None', 'True', ...]
print(math.sqrt(144))  #12
print(math.pi)  # 3.141592653589793
time.sleep(5)
print(time.time_ns()) # 1716957146486703000

~~~
























