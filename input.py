# print("Enter a name:", end=" ")
# name = input()
# print(name)

# name = input("Enter a name: ")
# print(name)

# name = input("Enter a name: ")
# print(f"Hello {name}. How are you doing?")


# print(f"Hello Mr. {last_name}. Is your first name {first_name}?")
# """Using f string"""





def get_name():
    first_name = input("Enter a first name: ")
    last_name = input("Enter a last name: ")

    full_name = first_name + " " + last_name
    return full_name

def greet(full_name):
    print(f"Hello {full_name}. How are you doing?")  


print("Ask input from user")

name = get_name()
greet(name)

# get_name() properly called → get_name()
# greet() function defined before use
# greet(name) correctly passed argument
