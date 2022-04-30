arr = [1,2,3,4,5,6,7,8]
summ = 0
for i in range(0, len(arr)):
    if arr[i] % 2 == 0:
            summ = summ + arr[i]
print("Sum of odd number is " + str(summ))
