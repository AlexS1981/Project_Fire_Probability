import random
import os

list_1 = list()
# list_2 = list()
# dict_2 = dict()

for i in range(75):
    list_1.append(random.randrange(2, 9111, 1))

f = open("Archive/City_map_res.txt", 'r')
count = 0
for line in f:
    for i in list_1:
        if count == int(i):
            print("{}, {}, {}, {}, {}, {}],"\
                  .format(line[0: len(line) - 3],\
                    1,\
                    random.randrange(1, 4, 1),\
                    random.randrange(0, 3, 1),\
                    random.randrange(1, 3, 1),\
                    random.randrange(0, 2, 1)))
    count += 1

# print(list_2)