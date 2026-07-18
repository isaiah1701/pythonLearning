import numpy as np 

numbers = np.array([2,32,4,75,3,1])

multiple = numbers * 10

print(f"{multiple}")

print(numbers.max())
print(numbers.min())
print(numbers.mean())
print(numbers.std())



temperaturesC = np.array([2,34,55,1,45,22,1,21,3,11,3,5,66,2])

temperaturesF = temperaturesC * 9 /5 + 32 
total = 0 
for temperature in temperaturesF:
    if temperature > temperaturesF.mean():
        total = total + 1 


print(f"{total} above the average of {temperaturesF.mean()}")

