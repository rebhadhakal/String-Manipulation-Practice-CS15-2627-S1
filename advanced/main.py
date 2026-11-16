print("1. Format a Name")
print("2. Format a Title")
print("3. Format a List")
print("4. Process Numbers")
choice = input("enter your choice(1,2,3, or 4):")
string_to_process = input("enter the string to process:")
if choice == "1":
    stripped = string_to_process.strip()
    last_name, first_name = stripped.split(",")
    last_name = last_name.strip().title()
    first_name = first_name.strip().title()
    name = first_name +" " +last_name
    print(name)
elif choice == "2":
    title =string_to_process.replace(" ", "")
    title =title.replace(",", " ")
    title= title.replace("::", " ")
    format_title = title.title()
    print(format_title)
elif choice == "3":
    items = string_to_process.split(",")
    format = " | ".join(items).upper()
    print(format)
elif choice== "4":
    total=0
    calculated=0
    numbers = string_to_process.strip().split(",")
    for number in numbers:
        value = int(number)
        total = total +value
        calculated = calculated+1
        average =total/calculated
        print("total:", total)
        print("average:", average)
else:
    print("invalid")