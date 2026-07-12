def square(num):
    return num * num 

print (square(12))
print (square(11))
print (square(10))

def is_even(num):
    if num % 2 == 0 :
        return True 
    else :
        return False 



print (is_even(5))
print (is_even(4))


def average(numbers):
    return sum(numbers) / len(numbers)
numbers= [5,4,3,9]
print ( average(numbers))
      