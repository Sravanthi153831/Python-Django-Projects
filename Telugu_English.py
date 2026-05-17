telugu = int(input("Enter telugu marks: "))
english = int(input("Enter English marks: "))
total = telugu + english 
for i in range(1, total + 1):
    if total % i == 0:
        print(f"{total} is divisible by {i}")
else:
    print("Loop completed! Final Total 
