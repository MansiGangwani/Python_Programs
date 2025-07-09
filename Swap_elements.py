# Swap elements in String list - replace G with e and e with G
# The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

# Define the original list

list_string = ['Gfg', 'is', 'best', 'for', 'Geeks']

# Perform character swaps using a unique temporary placeholder

swapped_list = [
    s.replace("G", "__TEMP__")  # Temporarily replace "G" with "__TEMP__"
     .replace("e", "G")        # Replace "e" with "G"
     .replace("__TEMP__", "e") # Replace "__TEMP__" with "e"
    for s in list_string

]

# Print the original and swapped lists

print("The original list is :", list_string)
print("List after performing character swaps :", swapped_list)


swapped_list = []
for s in list_string:
    # Replace "G" with "e" and "e" with "G"
    swapped_s = s.replace("G", "e")
    # swapped_s = s.replace("G", "__TEMP__").replace("e", "G").replace("__TEMP__", "e")
    swapped_list.append(swapped_s)  # Add the swapped string to the new list
print("List after performing character swaps  :", swapped_list)




