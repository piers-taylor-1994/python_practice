import pandas
with open("Practice/data.txt") as file:
    document = pandas.read_csv(file, sep="\t")

with open("Practice/long_data.txt") as file:
    long_document = pandas.read_csv(file, sep="\t")

name_list = long_document.drop_duplicates()
print(name_list)
# values = {name:long_document[long_document.person == name].sale.sum().item() for name in name_list}
# print(values)

# new_csv = pandas.DataFrame(values, index=values)
# print(new_csv)