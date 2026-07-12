# exercise one : personal profile 

profile = { 
    "name": "isaiah",
    "age": "23",
    "city": "London"
}

print (f"This is a profile for {profile["name"]} who is {profile["age"]} years old and lives in {profile["city"]}")

profile["hobbies"] = ["football", "gym", "boxing"]


for hobby in profile ["hobbies"]:
    print (hobby)

# Exercise 2 : Number Cruncher 

numbers= [4,6,21,44,1,4,56,3,11,54,6,21,48]
total = 0 
for number in numbers:
    total = total + number 

average = total / len (numbers)


even = 0 
for number in numbers:
    if number % 2 == 0:
        even = even + 1 

odd = len (numbers) - even 

print (odd)
print (even)


# Exercise 3 : Word counter 

sentence = "this is my sentence "

print (sentence.split())

print ( len (sentence.split()))



for word in sentence.split():
    print (word.upper())




word_count = {}


for word in sentence.split():
    if word in word_count:
        word_count = word_count[word] + 1 
    else :
        word_count [word] = 1 

print (word_count)





# Exercise 4 : Grade Checker function


grades = [78,68,98,7,81]


def checkGrade(numbers):
    
    result = []
    for number in numbers:
        if number >= 90:
             result.append("A")

       
        elif number >= 80:
             result.append("B")
        
        elif number >= 70:
              result.append("C")
       
        else:
             result.append("Fail")
    return result


print(checkGrade(grades))



# Exercise 5 : Health check 


server = {
    "name": "Lenny",
    "memory_gb": 2,
    "is_online": False
}

def checkServer(box):
    
    if box["is_online"] == False:
        return "Warning , offline"
    elif box["memory_gb"] < 4 :
        return "low memory"
    else : 
        return "OK"



print(checkServer(server))