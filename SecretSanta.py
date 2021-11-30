# -*- coding: utf-8 -*-
"""
Author : Daniel Lindberg
Description: Edit the dictionary to be the people in your secret santa group. This script mixes up the dictionary so that each person gets their own secret santa person.
"""
# python modules
import subprocess
import random

family_dict = {"Person1": "email1@gmail.com",
               "Person2": "email2@gmail.com",
               "Person3": "email3@gmail.com",
               "Person4": "email4@gmail.com"}

# Get two dictionaries of the people
original_list = family_dict.keys()
same_list = family_dict.keys()
repeat_shuffle = False
# Keep on shuffling until no dictionaries have people matching
while (repeat_shuffle == False):
    random.shuffle(same_list)
    repeat = False
    for x in range(0, len(original_list)):
        if original_list[x] == same_list[x]:
            repeat = True
    if not repeat:
        repeat_shuffle = True
# Email everyone in the dictionary who they got
for x  in range(0, len(original_list)):        
    p = subprocess.Popen(["mail", "-s", "Secret Santa for: {0}".format(original_list[x]), family_dict[original_list[x]] ], stdin=subprocess.PIPE)
    p.communicate("You are the secret santa for: {0}".format(same_list[x]))
    p.wait()

