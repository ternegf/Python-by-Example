#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# *********************************************************************
#                                                                     *
# Program      : Challenge_011_v1_01.py                               *
# Written by   : George Ternent                                       *
# Date.        : 19-Nov-2023.                                         *
#                                                                     *
# Description : Task  the  user  to enter a number over a hundred and *
#               then  a  number under 10 and then tell how many times *
#               the  smaller  number goes into the larger number in a *                
#               user friendly format.                                 *
#                                                                     *
# *********************************************************************
# Function(s)                                                         *
# *********************************************************************
#                                                                     *
# Name         Description                                            * 
# ****         ***********                                            *
# get_minmax   Get  the  minimum  and  maximum  permitted values of a *
#              of numbers.                                            *
#                                                                     *
# get_integer  Ask  the user to enter an integer in a range, ignoring *
#              any non numeric characters that are entered.           *
#                                                                     *
# *********************************************************************
# History                                                             *
# *********************************************************************
#                                                                     *
# Ref   Changed by        Date          Change(s)                     *
# ****  ***********       ****         **********                     *
# 0.01  George Ternent.   19-Nov-2023. Initial Version.               *
#                                                                     *
# *********************************************************************

# *********************************************************************
# F U N C T I O N S
# *********************************************************************

# –—------------------------------------------------------------------
# get_minmax(range)
# –—------------------------------------------------------------------
def get_minmax(range):
    """
    Input a range and return the minimum and maximum permitted values.
    
    Arg(s):
        Range. e.g. 1-10, <10, >10
        
    Returns:
        A dictionary containing the minimum and maximum permitted values
        for the range entered.
        
    """
    range = range.replace('to','-')
    
    operators = '-<>'
    integer_values = '0123456789'
    HI_VALUE = 999999
    numbers = []
    number  = ''
    operator = ''
    min = 0
    max = 0
    minmax = {}
    
    for i, char in enumerate(range):
        if char in operators:
                operator = char
                if operator == '<' or operator == '>':
                    if range[i+1] == '=':
                        operator = operator + '='
                operators = ''
                if len(number) > 0:
                    numbers.append(int(number))
                    number = ''
                continue
                
        if char in integer_values:
            number = number + char
            continue
    
    if len(number) > 0:
        numbers.append(int(number))
                
    #print(f'{numbers=}')
    #print(f'{operator=}')
    
    if operator == '-':
        if len(numbers) == 1:
            minmax['MIN'] = numbers[0]
            minmax['MAX'] = HI_VALUE
        elif len(numbers) > 1:
            minmax['MIN'] = numbers[0]
            minmax['MAX'] = numbers[1]
 
        # -----------
        return minmax
        # -----------
    
    if operator == '>':
        if len(numbers) == 1:
            minmax['MIN'] = numbers[0] + 1
            minmax['MAX'] = HI_VALUE
  
        # -----------
        return minmax
        # -----------
        
    if operator == '>=':
        if len(numbers) == 1:
            minmax['MIN'] = numbers[0]
            minmax['MAX'] = HI_VALUE
  
        # -----------
        return minmax
        # -----------
    
    if operator == '<':
        if len(numbers) == 1:
            minmax['MIN'] = 0
            minmax['MAX'] = numbers[0] - 1

        # -----------
        return minmax
        # -----------
    
    if operator == '<=':
        if len(numbers) == 1:
            minmax['MIN'] = 0
            minmax['MAX'] = numbers[0]
            
        # -----------
        return minmax
        # -----------
       
    minmax['MIN'] = numbers[0]
    minmax['MAX'] = numbers[0]
    
    # -----------
    return minmax
    # -----------
    
    
# –—------------------------------------------------------------------   
# parse_number
# –—------------------------------------------------------------------
    """
    Parse a string and just return the integer characters in it.
        
    Arg(s):
        String e.g. £66
        
    Returns:
        Number e.g. 66
        
    """
def parse_number(number):
    integer_values = '0123456789'
    parsed_number = ''
    
    for char in number:
        if char in integer_values:
            parsed_number = parsed_number + char
        
    # ------------------       
    return parsed_number
    # ------------------

# –—------------------------------------------------------------------
# get_number
# –—------------------------------------------------------------------
def get_number(range):
    """
    Input a number in a given range.
        
    Arg(s):
        Range. e.g. 1-10, <10, >10
        
    Returns:
        The number entered.
        
    """
    
    minmax = get_minmax(range)
    
    min = minmax['MIN']
    max = minmax['MAX']
    

    parsed_number  = ''
    
    number = input(f'Enter a number [{range}] : ')
    number = int(parse_number(number))
    
    while not (number >= min and number <= max):
        print (f'\n{number} is not in range, please re-enter.\n')
        
        number = input(f'Enter a number [{range}] : ')
        number = int(parse_number(number))

 
    # -----------
    return number
    # -----------

# *********************************************************************
# M A I N  P R O G R A M
# *********************************************************************

#range_1 = input('Enter range of first number: ')
#range_2 = input('Enter range of second number: ')

number_1 = get_number('>100')
number_2 = get_number('<10')

print(f'{number_1=}')
print(f'{number_2=}')

number_of_times = number_1//number_2

if number_1/number_2 == number_1//number_2:
    print(f'\nThe number {number_2:,} goes into {number_1:,} exactly {number_of_times:,} times.')
else:
    print(f'\nThe number {number_2:,} goes into {number_1:,} {number_of_times:,} times.')

#print(f'{minmax_1=}')
#print(f'{minmax_2=}')


