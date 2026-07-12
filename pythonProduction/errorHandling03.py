def self_divide(a,b):
    if a == 0  or b == 0:
        raise ValueError("None")
    return a / b 

print(self_divide(10,2))



def to_number(string):
    try:
        return int(string)
    except ValueError:
        print(f"{string} is not a valid number")
        return None


print(to_number("4"))
print(to_number("int"))


def set_age(num):
    if num < 0:
        raise ValueError ("age cannot be negative ")
    return num


print(set_age(90))
print(set_age(-5))