# large Integers
#==================#
# print(12_3456_789)
#==================#

# type()  ====> gives the data type of a variable, used for type checking
# eg:- print(type("Hello")) ====> <class 'str'>
# print(type(123)) ====> <class 'int'>
# print(type("k")) ====> <class 'str'>
# print(type(1)) ====> <class 'int'>
# print(type(0.1)) ====> <class 'float'>
# print(type(False)) ====> <class 'bool'>

# Type casting / Type conversion
#===============================#
# int(var)
# float(var)
# bool(var)
# str(var)

#########
# 6 / 3 =====> 2.0 => float
# 6 // 3 ====> 2 => int
#########
# 3**2 ====> 3 to the power of 2 => the left to the power of the right
#########


#==================#
# round() ====> rounds the decimal number
# round(30.8251191) ====> 31
# round(number, round_to_how_many_decimal_points) ====> round(30.8251191,2) => 30.83
#==================#

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
percentage = (float(input("How much tip percentage would you like to give? 10 , 12 or 15? ")) + 100) / 100
people = float(input("How many people to splith the bill with? "))
result = (bill * percentage) / people
print(f"Each person sould pay : ${round(result,2)}")


