# DT = DYNAMIC TYPING
# ST = STATIC TYPING


## VARIABLES --------------------------------------
# - DT - DYNAMIC TYPING
var_dt_name     = "Example of a name typed with DT"
var_dt_age      = 25
var_dt_name_2   = "John John"
var_dt_hobby    = "Basquete"
var_dt_number   = 0
var_dt_number_2 = 0

# - ST - STATIC TYPING
var_st_name: str = "Jack Jack"
var_st_age: int  = 99

## ------------------------------------------------


## CONSTANTS --------------------------------------
# - DT - DYNAMIC TYPING
CONST_DT_NAME      = "Keanu"
CONST_DT_LONG_NAME = "Keanu Rivis"

# - ST - STATIC TYPING
CONST_ST_NAME      = "Post"
CONST_ST_LONG_NAME = "Post Marrone"

## ------------------------------------------------


## TYPES ------------------------------------------
t_String: str = "String Type"
t_Int: int = 100
t_Float: float = 100.20
t_Boolean: bool = 0
t_Tuple: tuple = ["Coke", 5.99]
t_List: list = [1,2,3,4]
t_Dictionary: dict = {var_dt_name_2: "Morpheus", var_dt_hobby: "COME C DE CURIOSOS"}

## ------------------------------------------------


## INPUTS + CONCAT --------------------------------
part_1: str = input()
part_2: str = input()

all_parts = part_1 + part_2

fcknf = 'F'
print(f"FUCK {fcknf}")

## ------------------------------------------------


## OPERATORS --------------------------------------

# - COMPARISON
# EQUAL (==)
if var_dt_number == 0:
    print("Zero")

# GREATER THAN (>)
if var_dt_number > 0:
    print("Greater then zero")

# LESSER THEN (<)
if var_dt_number < 0:
    print("Lesser then zero")

# GREATER OR EQUAL THEN (>=)
if var_dt_number >= 0:
    print("Greater or equal then zero")

# LESSER OR EQUAL THEN (<=)
if var_dt_number <= 0:
    print("Lesser or equal then zero")

# - LOGICAL
# AND
if var_dt_number == 0 and var_dt_number_2 == 0:
    print("Zero")

# OR
if var_dt_number == 0 or var_dt_number_2 == 0:
    print("Zero")

## ------------------------------------------------


## IF, ELIF, ELSE ---------------------------------

if var_dt_number == 0:
    print("zero")
elif var_dt_number > 0 and var_dt_number <= 10:
    print("between 1 and 10")
else:
    print("bigger than 10")

## ------------------------------------------------


## DATA STRUCTURES --------------------------------
# - TUPLE (FIXED SIZE AND CAN HAVE MULTIPLE-TYPES)
# DT - DYNAMIC TYPING
dt_tuple = (1, "Name")

# ST - STATIC TYPING
st_tuple: tuple[int, str] = (1, "Name")

# - ARRAY (LIST OF A VALUES FROM THE SAME TYPE)
empty_array = []
int_array   = [1, 2, 3, 4]

# ACCESS BY INDEX
# ARRAY ALWAYS START AT INDEX 0
int_array[0]   #1 SLOT

# ACCESS BY INDEX RANGE
int_array[0:2] #1,2,3

# ACCESS THE LAST ELEMENT
int_array[-1]  #4

# STATIC TYPING
int_array: list[int] = [1, 2, 3, 4]

# - DICTIONARY (ARE A KEY:VALUE PAIR DATA TYPE)
person = {1: "one", 2: "two"}

# ACCESS VALUE BY KEY
person[1] # "one"

# STATIC TYPING
person: dict[int,str]

## ------------------------------------------------


## LOOPS ------------------------------------------
# - FOR
name_list = ["Jack","John","Jhone"]

for name in name_list:
    print(f"HELLO {name}!")

# - WHILE
flag = True

while flag {
    flag = true
}
## ------------------------------------------------

# - LIST COMPREHENSION
# Multiply every number in a given range and put the result inside the array
lc = [x * 2 for x in range(10)]

# lc = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

## ------------------------------------------------


## FUNCTIONS --------------------------------------
def add(n1, n2):
    return n1 + n2

# ST - STATIC TYPING
def add(n1: int, n2: int) -> int:
    return n1 + n2

## ------------------------------------------------

## CLASSES ----------------------------------------


## ------------------------------------------------

