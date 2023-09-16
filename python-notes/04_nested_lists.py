'''
    # Nested lists
'''

list_a = [1,2,3,4,5,6,7,8,9,10]
list_b = [11,12,13,14,15,16,17,18,19,20]
list_c = [list_a,list_b] # [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
print(list_c)

list_d = list_a+list_b
print(list_d) # [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]

dict_a = {
    "flash" : "Fastest man alive"
}

dict_b = {
    "reverse" : "Strongest flash enemy"
}

list_flash_characters = [dict_a, dict_b]

print(list_flash_characters)