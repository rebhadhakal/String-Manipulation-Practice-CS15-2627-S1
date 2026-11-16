string_to_process = "eggs,cheese,milk,bread,cereal"

# Expected Output: "EGGS | CHEESE | MILK | BREAD | CEREAL"

items = string_to_process.split(",")
format = " | ".join(items).upper()
print(format)
