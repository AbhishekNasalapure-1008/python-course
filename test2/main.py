# 32/35
#1
print("Hello world")

#2
name=input("What is your name?")
print(name)

#3
fruits=['apple','mango','banana','pineapple','grapes']
# print(fruits)
for fruit in fruits:
    print(fruit) 

#4
age=int(input("What is your age?"))
if age>=18:
    print("You are allow ")
    
else:
    print("You are not allow ")

#5
list=[15,10,28,49,99,73,82]
high_num=0
for num in list:
    if num>high_num:
        high_num=num
print(f"the highest num is {high_num}")

#6
total=sum(list)
print(total)

sum=0
for number in list:
    sum += number 

#7
for i in list:
    if i%2==0:
        print(i)
