string_to_process = "   sMitH, aLeX    "

# Expected output: "Alex Smith"

stripped = string_to_process.strip()
last_name, first_name = stripped.split(",")
last_name = last_name.strip().title()
first_name = first_name.strip().title()
name = first_name +" " + last_name
print(name)


