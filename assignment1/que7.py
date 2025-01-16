#7.1
with open("example.txt","w") as file:
    file.write("hello world")
with open("example.txt","r") as file:
    content=file.read()
    print(content)

#7.2
with open("example.txt","a") as file:
    file.write("\nAppended text")
with open("example.txt","r") as file:
    content=file.read()
    print(content)

#7.3
with open("example.txt","r") as file:
    lines= file.readlines()
    print("number of lines",len(lines))