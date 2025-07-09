# def maximum():
#     a = int(input("Enter A: "))
#     b = int(input("Enter B: "))
#     c = int(input("Enter C: "))
#     if (a > b) and (a > c):
#         print("Maximum no(A): ", a)
#     elif (b > c) and (b > a):
#         print("Maximum no(B): ", b)
#     else:
#         print("Maximum no(C): ", c)
# maximum()


l1 = [2,5,3,7,1]

for i in l1:
    print (i)

maxi = max(l1)
print ("max:",maxi)

mini = min(l1)
print("mini:",mini)

# Initialize variables for maximum and minimum
maxi = l1[0]  # Start with the first element as the maximum
mini = l1[0]  # Start with the first element as the minimum

# Iterate through the list to find the maximum and minimum
for i in l1:
    if i > maxi:  # Compare current element with maxi
        maxi = i
    if i < mini:  # Compare current element with mini
        mini = i

# Print the maximum and minimum values
print("max:", maxi)
print("mini:", mini)

