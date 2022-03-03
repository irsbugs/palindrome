#!/usr/bin/env python3
#
# palindrome.py
#
# palindrome - same forward as backwards
# 
# Ian Stewart - 2022-03-01 - CC0
#

def get_integer(prompt, default=100):
    """
    Get input from user while providing prompt and a default integer value.
    Users input must be zero or a positive integer.
    """
    while True:
        string = input(prompt.format(default))
        if string == "":
            string = str(default) 
        if string.isdecimal():
            return int(string)
        else:
            print("Invalid input: {}\nPlease try again...".format(string))
            continue            


def calculate_palindrome(start, span, iteration):
    """
    Calculate the palindromes from start value for a range of span value.
    The iteration is a filter. It determines how many iterations are required
    for there to be output displayed.
    """
    for value in range(start, start + span):
        value_1 = value       
        count = 0      
        while True:
            if str(value_1) == str(value_1)[::-1]:  
                if count >= iteration:
                    print("{:>10} {:>5} {}".format(value, count, value_1))
                break
            count +=1            
            value_2 = int(str(value_1)[::-1])
            value_total = value_1 + value_2   
            value_1 = value_total
            if count == 300:
                print("{:>10} {:>5} Not found".format(value, count))                          
                break
            else:
                continue

 
if __name__=="__main__":
    
    prompt = "Start integer [{}]: "
    start = get_integer(prompt)

    prompt = "Range integer [{}]: "
    span = get_integer(prompt)

    prompt = "Display iterations from [{}]: "
    default = 0
    iteration = get_integer(prompt, default)


    print("\n   Integer Iter. Palindrome" )        
    calculate_palindrome(start, span, iteration)
    

"""
Example of generating a palindrome number...
Let's pick a number: 174
The reverse order of 174 is 471.
Repeatedly add forward order to reverse order...
174 + 471 = 654 (1)
654 + 456 = 1191 (2)
1191 + 1911 = 3102 (3)
3102 + 2013 = 5115 (4)

5115 <--- is a palindrome number
It took 4 iterations to reach the palindrome number

Largest: 1999291987030606810 with 261 iterations.
"""
