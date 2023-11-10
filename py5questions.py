#Python QUESTIONS:

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
#The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(username):
    print("hello_" + username + "!")

def hello_name(JeniJ):
    print("hello_" + JeniJ + "!")

    #Output = hello JeniJ!


#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
def first_odds():
    for number in range(1, 101):
        if number % 2 != 0:
            print(number)

#Output = 1
#3
#5
#7
#...
#97
#99



#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    if len(a_list) == 0:
        return None
    else:
        max_num = a_list[0]
        for num in a_list:
            if num > max_num:
                max_num = num
        return max_num
#Output: numbers = [10, 5, 25, 17, 9]
max_number = max_num_in_list(numbers)
print(max_number)
#Output = 25



#Question 4
#Write a function to return if the given year is a leap year. 
#A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#Output    
#print(is_leap_year(2020))  # Output: True
#print(is_leap_year(1900))  # Output: False
#print(is_leap_year(2000))  # Output: True



#Question 5

#Write a function to check to see if all numbers in the list are consecutive numbers. 
#For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
#The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    sorted_list = sorted(a_list)  # Sort the list in ascending order
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i-1] + 1:
            return False
    return True
#Output
#print(is_consecutive([2, 3, 4, 5, 6, 7]))  # Output: True
#print(is_consecutive([1, 2, 4, 5]))  # Output: False
#print(is_consecutive([1, 2, 3, 4, 5]))  # Output: True
