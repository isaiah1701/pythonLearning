from shapes import area_of_rectangle

def main():
    print("Hello from shape-project!")


if __name__ == "__main__":
    main()


print(area_of_rectangle(2,6))


def greet(name: str) -> str:
    return f"Hi, {name}"

def total(numbers: list[int]) -> int:
    return sum(numbers)

def is_adult(age: int) -> bool:
    if age >= 18:
        return True 
    else : 
        return  False 


print (greet("Isaiah"))
print (total([2,5,6,7,8]))
print (is_adult(23))
    