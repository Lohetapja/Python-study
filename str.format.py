#srt.format =   Optional method that gives users
#               more control when displaying output

##item = "moon"

#print("The "+animal+" jumped over the "+item)
#print("The {} jumped over the {}".format("cow","moon"))
#print("The {} jumped over the {}".format(item,animal))
#print("The {0} jumped over the {1}".format(item,animal))        #positional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))        #keyword argument

#print("kasutaja "+person+" hakkas "+item)

#text = "The {} jumped over the {}"
#print(text.format(animal,item))

person = "Lohetapjal"
item = "puhkus!"

#text = "Kasutaja {} hakkas {}"
#print(text.format(person,item))

print(f"Kasutaja {person} hakkas {item}")
