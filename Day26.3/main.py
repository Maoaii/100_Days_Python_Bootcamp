with open("file1") as file1:
    file1_nums = file1.readlines()
with open("file2") as file2:
    file2_nums = file2.readlines()

result = [int(n) for n in file1_nums if n in file2_nums]

# Write your code above 👆

print(result)



