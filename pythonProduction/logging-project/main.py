import logging

logging.basicConfig(level=logging.INFO)


logging.info("Program started")



def checkNumbers(numbers: list[int]) -> str:
    negative = 0 
    if len(numbers) == 0:
        logging.warning("list is empty")

    for num in numbers:
        if num < 0 :
            logging.warning("Number is negative")
            negative = negative + 1 
    if negative == 0 :
        return "No negative numbers"
    else:
        return f"{negative} negative numbers"


print(checkNumbers([1,2,4,4,-5]))
print(checkNumbers([]))
print(checkNumbers([1,3,-2,34,1,-2,-21,-5,-5,6,2,-4]))