a_list=[1,3,5,7,9,18]
b_list=[]

#regular method
for i in a_list:
    add_1=i+1
    b_list.append(add_1)

print(b_list)    

#new method

c_list=[item+1 for item in a_list]
print(c_list)


#for copy of list
copy_list=[item for item in a_list]
print(copy_list)


names=["Abhi","Tejas","Pranav","Mahadev","Sushant"]
Capital_names=[items.upper() for items in names]
print(Capital_names)


name="abhishek"
name_list=[letter for letter in name]
print(name_list)

#challenge

num=[i*2 for i in range(10)]
print(num)


#CONDITIONAL LIST COMPREHENTION

small_names=[name for name in names if len(name)<=5]
print(small_names)

big_names=[name for name in names if len(name)>=5]
print(big_names)