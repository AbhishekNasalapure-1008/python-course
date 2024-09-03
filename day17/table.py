from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Programming language", "Founded in","Founded by"]
table.add_row  (["Python", 1991, "Guido van Rossum"])
table.add_row  (["JavaScript", 1995, "Brendan Eich"])
table.add_row  (["C language", 1972, "Dennis Ritchie"])
table.add_row  (["C+ language",  1979, "Bjarne Stroustrup"])
print(table)