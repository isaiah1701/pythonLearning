def is_even(num: int) -> bool:
    if num % 2 == 0 :
        return True
    else:
        return False 

def average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers) 