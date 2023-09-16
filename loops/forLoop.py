numbers = [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print("The sum is:", sum)
for i in range(1, 11):
    print(i, end=" ")  # Use the 'end' parameter to specify the separator

step = 3
for i in range(0, 10, step):
    print(i , end=" ")
