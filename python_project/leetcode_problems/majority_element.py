#https://leetcode.com/problems/majority-element/
import collections


def majority_elements(user_input):
    occurences=collections.Counter(user_input)
    item_values=occurences.values()
    max_items=max(item_values)
    for key,value in occurences.items():
        if value==max_items:
            return key



user_input = [3, 2, 3]
print(majority_elements(user_input))
