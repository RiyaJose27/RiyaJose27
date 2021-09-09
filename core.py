# x = [[5, 2, 3], [10, 8, 9]]
# x[1][0] = 15
# print(x)
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# students[0]['last_name'] = 'Bryant'
# print(students[0])

# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# sports_directory['soccer'][0] = 'Andre'
# print(sports_directory)

# z = [{'x': 10, 'y': 20}]
# z[0]['y'] = 30
# print(z)

# # \\2 . iterate

students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"},
    {"first_name": "Mark", "last_name": "Guillen"},
    {"first_name": "KB", "last_name": "Tonel"},
]

# iterateDictionary(students)
# # should output: (it's okay if each key-value pair ends up on 2 separate lines;
# # bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


def iterateDictionary(some_list):
    for i in some_list:
        name = []
        k = []
        for key, value in i.items():
            k.append(key)
            name.append(value)
        print(f"{k[0]} - {name[0]}, {k[1]} - {name[1]}")


iterateDictionary(students)


# 3 q
# print('3. Get values From a List of Dictionaries')
def iterateDictionary2(key_name, some_list):
    for d in some_list:
        for key, value in d.items():
            if key == key_name:
                print(value)


iterateDictionary2("first_name", students)

iterateDictionary2("last-name", students)


# 4 code
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael","Amy","Eduardo","Josh","Graham","Patrick","Minh", "Devon",],
}


def printInfo(d):
    for x in d:
        print(f"{len(d[x])} {x.upper()}")
        for y in d[x]:
            print(y)


printInfo(dojo)
