# tuple =   collection witch is ordered and unchangeble
#            used to group together related data

student = ("Lohe","36","male")

print(student.count("Lohe"))
print(student.index("male"))

for x in student:
    print(x)

if "Lohe" in student:
    print("Lohe is here!")