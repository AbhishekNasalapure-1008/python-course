# # import pandas
# # csv_file = pandas.read_csv("data.csv")

# # # print(csv_file)

# # import pandas as pd

# # df = pd.read_csv('data.csv')

# # print(df)

# # with open('weather_data.csv') as data_files:
# #     data = data_files.readlines()
# #     print(data)


# import csv
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temprature=[]

#     for row in data:
#         # print(row)
#         if row[1]!='temp':
#             temprature.append(row[1])
#     monday=[]
#     for columns in data:
#         # print(columns[1])
#         monday.append(columns[1])
#     print(monday)


    

# print(temprature)    
        
import pandas

weather=pandas.read_csv('weather_data.csv')
print(weather.day)
print(weather.temp)
print(weather.condition)

data=pandas.read_csv('data.csv')
print(data.name)
print(data.scores)