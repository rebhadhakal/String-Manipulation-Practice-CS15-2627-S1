string_to_process = "  18,27,35,20  "

# Expected Output:
# "Total: 100"
# "Average: 25.0"
total=0
calculated=0
numbers= string_to_process.strip().split(",")
for number in numbers:
    value=int(number)
    total= total+value
    calculated=calculated+1
average=total/calculated
print("total:",total)
print("average:", average)
