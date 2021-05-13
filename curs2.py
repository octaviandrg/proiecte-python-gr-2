print("Acesta este cursul al 2-lea!")

name = "Ana"
if name:
    print(name)
    print(type(name))
else:
    print("Nu avem def niciun nume")


first_person = {"Name": "John"}
second_person = {"Name": "John"}

if first_person is second_person:
    print("They are the same")
else:
    print("They are not the same")

if first_person == second_person:
    print("They are the same")
else:
    print("They are not the same")

my_str = r"Owner\"s manual"
print(my_str)

print("""adsda dsadasdas dsadasdsa
dsadasd dasdas das
dasdasdasdas das
das dasdasdasdasdasds""")


name = "Ion"
age = 21
msg = "{} has {:.2f} years".format("Ion",18.4567)
msg_2 = f"{name} has {age + 2} years"

print(msg)
print(msg_2)

l = [1, 2, 3, "Ana are mere", True, False, None, [4, 5, 6]]

print(l[2])

l[2] = '99'

print(l[2])

inventar = ["faina", "drojdie", "apa", "sare"]
for item in inventar:
    print(item)

for index, value in enumerate(inventar):
    print(f"{value} cu indexul {index}")

print(inventar[-1])
print(inventar[len(inventar)-1])

l1 = [2, 3, 0, 9]
l2 = [12, 13, 10, 19]


l1.extend(l2)
print(l1)

my_dict = {1: "Home", 2:"Office", 3: "Restaurant"}
for key, value in my_dict.items():
    print(f"{key} => {value}")

print(my_dict.get(22,"Nu exista cheia"))

