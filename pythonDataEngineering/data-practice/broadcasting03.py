import numpy as np 


numbers = np.array([[3, 4,2],
                    [5, 6,1],
                    [7, 8,0]],dtype=np.int8)

numbers = numbers + 5 

print (numbers)



add_array = np.array([[1,2,3]], dtype=np.int8)

numbers = numbers + add_array

print(numbers)

print(numbers.nbytes)