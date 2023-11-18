#!/usr/bin/env python
# coding: utf-8

# In[1]:


# *********************************************************************
#                                                                     *
# Program      : Challenge_001_v1_01.py                               *
# Written by   : George Ternent                                       *
# Date.        : 09-Nov-2023.                                         *
#                                                                     *
# Description : Ask  for the user’s first name and display the output *
#               message:                                              *
#                                                                     *
#               Hello [First Name].                                   *
#                                                                     *
# *********************************************************************
# Function(s)                                                         *
# *********************************************************************
#                                                                     *
# Name      Description                                               *
# ****      ***********                                               *
# alpha     Returns just the alpha characters in  the string that was *
#           passed (i.e. a-Z and A-Z).                                *
#                                                                     *
# *********************************************************************
# History                                                             *
# *********************************************************************
#                                                                     *
# Ref   Changed by        Date          Change(s)                     *
# ****  ***********       ****         **********                     *
# 0.01  George Ternent.   09-Nov-2023. Initial Version.               *
#                                                                     *
# *********************************************************************

# *********************************************************************
# F U N C T I O N S
# *********************************************************************

# –—------------------------------------------------------------------
# alpha
# –—------------------------------------------------------------------
def alpha(string):
    """
    Returns just the alpha characters in the string that was
    passed (i.e. a-Z and A-Z).
    
    Arg(s):
        String
        
    Returns:
        String that just has the alpha character of the string
        that was passed as an argument.
        
        For example:
        
        alpha('@28Al9)i [c]]e')
        
        returns Alice
    """
    alpha_string = ''
    for char in string:
        if char.upper() >= 'A' and char.upper() <= 'Z':
            alpha_string = alpha_string + char

    # -----------------
    return alpha_string
    # -----------------

# *********************************************************************
# M A I N  P R O G R A M
# *********************************************************************

name = input ('Enter your name : ')
name = alpha(name)
name = name.title()

print(f'Your name is {name}.')

