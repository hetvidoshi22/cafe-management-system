menu={
    'pizza':150,
    'sandwich':180,
    'frankie':70,
    'noodles':130,
    'oreoshake': 90}
print("Welcome To Hetu's Cafetaria")
print("Here you will get a free choco lava cake on total bill more than 300")
print("The menu is given below:")
print("pizza:rs 150\n'sandwich':rs 180\n'frankie':rs 70\n'noodles':rs 130\n'oreoshake':rs 90 ")

total=0

order1=str(input("enter food from menu:"))
if order1 in menu:
    total += menu[order1]
    print(total)
else:
    print("sorry order anything else")
print("------------------------")
order2=input("enter some other food from menu if needed")
if order2 in menu:
    total+=menu[order2]
    print(total)
else:
    print("order by seeing menu")
print("------------------------")
if total>300:
    print("congo you wil be getting a free choco lava cake")
else:
    print("order more food to get a free choco lava cake")
print("------------------------")     
print("bye bye")
print("have a nice day")
print("see you soon")    

