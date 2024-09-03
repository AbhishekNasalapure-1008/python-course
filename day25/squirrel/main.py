import pandas


data=pandas.read_csv('squirrel-data.csv')
# print(data)

red=[]
gray=[]
black=[]

colors=data['Primary Fur Color']

for color in colors:
    if color=="Gray":
        gray.append(color)
    if color=='Cinnamon':
        red.append(color)
    if color=='Black':
        black.append(color)

print(gray)

df=pandas.DataFrame(
    {
        'squirrels':['red','gray','black'],
        'numbers':[len(red),len(gray),len(black)]
    }
    )

df.to_csv('squirrel-data_analyser.csv')


