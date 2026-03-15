set_name = set()
while True:
    name = input("Enter a name:")
    if name == "":
        break
    if name in set_name:
        print("Existing name")
    else:
        print("New name")
    set_name.add(name)
print("List of entered names:")
for i in set_name:
    print(i)