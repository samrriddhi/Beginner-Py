x = 57
max_attempts = 5
print(f"You have {max_attempts} attempts to guess the number.")

for attempt in range(1, max_attempts + 1):
    num = int(input("Enter any number: "))
    if num > x:
        print("Too big!!")
    elif num < x:
        print("Too small!!")
    else:
        print("Correct guess!")
        break  
else:
   
    print(f"Sorry, you've used all {max_attempts} attempts. The correct number was {x}.")
