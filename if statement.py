#if statement = a block of code that will execute it's conditions is true
# IF (a = True, then B, else C, End F)

age = int(input("How old are you?: "))

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adault!")
elif age < 0:
    print("You have not been born yet!")
else:
    print("You are a child!")

