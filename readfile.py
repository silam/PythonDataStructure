import json

filename = 'car.py'

with open(filename) as f_obj:
    contents = f_obj.read()

# with open(filename) as f_obj:
#     for line in f_obj:
#         print(line.rstrip())

# with open(filename) as f_obj:
#     lines = f_obj.readlines()
#     for line in lines:
#         print(line.rstrip())

filen = 'programming1.txt'

# try:
#     with open(filen, 'a') as f:
#         f.write('I love programming\n')
#         f.write('I love game too\n')

    
#     with open(filen) as f:
#         contents = f.readlines()
# except FileNotFoundError:
#     print('File not Found!')
# else:
#     print(contents)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print('Can not divide by 0')


#print(contents)


print("Enter two numbers to divide\n")
print("Enter q to quit\n")

while True:
    x = input("\nFirst number: ")

    if x == 'q':
        break

    y = input("\nSecond Nubmer: ")
    if y == 'q':
        break

    try:
        res = int(x) / int(y)
    except Exception as e:
        print('Can not divide by 0 ')
        print(e, type(e))
    else:
        print(res)


numbers = [2,3,4,5,6]

filename = 'numbers.json'

with open(filename,'w') as f_obj:
    json.dump(numbers, f_obj)

