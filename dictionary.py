# dictionary = A changeable, unordered collection of unique key: value pairs
#                Fast because they use hashing, allow a value quickly

capitals = {"USA":"Washington DC",
            "india":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"})
capitals.pop("China")
capitals.clear()

#print(capitals["Russia"])
#print(capitals.get("Germany"))
#print(capitals.keys())
#print(capitals.values())
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)