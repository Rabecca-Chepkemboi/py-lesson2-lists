# define a function that accepts a string as input and uses the for loop to
# iterate through the string and count the vowels

def det (str):
   vow = 0
   vowels = ['a', 'e', 'i', 'o', 'u']
#    for x.tolowercase in str:
   for x in str:
      for b in vowels:
         if x == b:
            vow += 1
   return vow
print(det("chepkemboi"))   


# Write a Python function that takes two arguments (a and b) and returns their sum

def num_addition(a, b):
  return (a + b)
a = 20
b = 10
print(num_addition(a, b))  


# Write a Python function that takes a string as input and returns the string reversed.

# def name(string):
string = "hello chep"
reversed_string = string[::-1]
print(reversed_string)


# Write a Python function that takes a list of integers as input and returns the sum of all 
# the integers in the list.

def add_numbers(number):
   sums = 0
   for x in number:
      sums += x
   return sums   
print (add_numbers([5, 3, 2]))



# Write a Python function that takes a list of integers as input and returns a new list with 
# all the even numbers removed.

def even_numbers(numbers):
   new = []
   for x in numbers:
      if x % 2 != 0:
         new.append(x)
   return new
print(even_numbers([2, 3, 5, 9, 1]))   



# Write a Python function that takes a list of integers as input and returns the highest value 
# in the list.

def highest(number):
   x = max(number)
   return x
print(highest([5, 7, 1, 10, 2, 9, ]))



# Write a Python function that takes a list of strings as input and returns a new list with all
# the strings capitalized.
          
def capitalise(name):
   return [x.capitalize() for x in name]
name = ["clarah", "ambrose", "vince"]
print(capitalise(name))