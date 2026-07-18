import logging 

def parse_price(cost: str) -> float:
    try:
        logging.info("Successful conversion")
        return float(cost)
        
    except ValueError:
        logging.warning("Cannot parse")
        print(f"{cost} is not a valid number")
        return None
        


print(parse_price("4.60"))
print(parse_price("abc"))