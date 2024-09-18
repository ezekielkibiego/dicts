# file_object = open('file_name', 'mode)

# file = open('hello.txt', 'r')
# print(file)


with open('mbox.txt', 'r') as file:
    content = file.read()
    # print(content)
    
# with open('mbox.txt', 'r') as file:
#     for line in file:
#         print(line.strip())
        
with open('mbox.txt', 'r') as file:
    lines = file.readlines()
    # print(lines)
    
with open('hello.txt', 'w') as file:
    file.write('Hello, world!\n')
    file.write('This is a new line.')