
# 1. Write a Python program to get a single string from two given strings,
#  separated by a space, and swap the first two characters of each string

def get_single_string(string1, string2):
    my_strings1 = string1[:2] + string2[2:]
    my_strings2 = string2[:2] + string2[2:]

    return my_strings1+" "+ my_strings2
string1 = "kitale"
string2 = "nairobi"

ans = (get_single_string(string1, string2))
print(ans)

# 2.  Write a Python function that takes a list of words and returns the
#  longest word and the length of the longest one

def find_longest(word):
    longest = ""
    longest_len = 0
    for x in word:
        if len (x)> longest_len:
            longest = x
            longest_len = len(x)
    return longest, longest_len
word = ["kiwi", "mamgoo", "banana"]  
longest, length = find_longest(word)
print(longest)
print(length)      


# 3. Write a Python program that accepts a comma-separated sequence of words
#  as input and prints the distinct words in sorted form (alphanumerically).

def sorted_words(words):
    words_list = words.split(",")
    distinct_words = list(set(words_list))
    distinct_words.sort()
    for word in distinct_words:
        print(word.strip())

words = "hello there, it'me, again"
print(sorted_words(words))



# 4.. Write a Python function that takes two lists and returns True if they 
# have at least one common member.

def common_member(num1, num2):
    for numbers in num1:
        if numbers in num2:
            return True
        return False
num1 = [4, 3, 6, 2]
num2 = [3, 1, 8, 3]
ans = common_member(num1, num2)
print(ans)    


# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]

keys = ["color_name", "color_code"]
values = ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
ans = []
for x in range(len(values[0])):
    my_dict = {}
    for i in range(len(keys)):
        my_dict[keys[i]] = values[i][x]
    ans.append(my_dict)
print(ans)  


# 6. Write a Python program to check whether all dictionaries in a list are empty or not

def empty_dict(lists):
    for dictionary in lists:
        if bool(dictionary):
            return False
        return True
lists1 = [{}, {}, {}]
lists2 = [{"name":"Chep"}, {}]
print(empty_dict(lists1))    
print(empty_dict(lists2)) 


# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]

numbers = [3,5,45,97,32,22,10,19,39,43]
odd_nums = [i for i in numbers if x % 2 == 0]
print(odd_nums)


# 8. Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5

list_a = 1, 2, 3, 4, 
list_b = 2, 3, 4, 5
similar_nums = []
for numbers in list_a:
    if numbers in list_b and numbers not in similar_nums:
        similar_nums.append(numbers)
print(similar_nums)        


# 9. Use a nested list comprehension to find all of the numbers from 1-1000 that
#  are divisible by any single digit besides 1 (2-9)

divisible_digit = [number for number in range(1, 1001)if any (number % numbers == 0 and numbers != 1 and numbers !=number for number in range(2, 10))]
print(divisible_digit)


# 10. Write a Python function to remove all vowels in a string

def eliminate_vowels(name):
    vowels = "a,e,i,o,u,A,E,I,OU"
    new = ""
    for x in name:
        if x not in vowels:
            new += x
    return new
me_name = "hello chep"
my_name = eliminate_vowels(me_name)
print(my_name)        