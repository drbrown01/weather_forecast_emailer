my_varible = []

try:
    get_names = open('name2.txt', 'r')
    for line in get_names:
        
        count = line.count(line)
        my_varible.append(line.strip().capitalize())
        
except FileNotFoundError as err:
    print(err)

    
print(my_varible)


