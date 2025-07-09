no = int(input("Enter Numbers count: "))
print("Numbers: ", no)
numbers = []

for i in range(no):
    number = input("Enter Number: ")
    numbers.append(number)
print("numbers:", numbers)

sort_no = []
def sort_no():
    numbers.sort()
    sort_no = numbers
    print("sort_no:", sort_no)

sort_no()

reverse_no = []
def reverse_no():
    numbers.reverse()
    reverse_no = numbers
    print("reverse_no:", reverse_no)
reverse_no()
