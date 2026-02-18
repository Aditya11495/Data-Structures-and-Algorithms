arr = [12,5,8,45,3,5,19]
min_num = arr[0]
max_num = arr[0]

for i in arr:
        if i < min_num:
            min_num = i
        elif i > max_num:
            max_num = i
print("Minimum number:", min_num)
print("Maximum number:", max_num)