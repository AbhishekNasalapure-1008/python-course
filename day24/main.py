# f=open('text.txt','r')
# print(f.read())

with open("text.txt","r") as f:
    print(f.read())

with open("text.txt","w") as f:
    f.write("hello")   

with open("text.txt","a") as f:
    f.write("\nhello world")