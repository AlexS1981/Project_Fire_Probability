import os
import math
import random

os.chdir(os.getcwd())

f = open("City_map.txt", 'r')
list_a = []
list_b = []
list_c = []
for line in f:
    list_a.append(line)
for i in list_a:
    list_b.append(i.replace(" \t> ", "*"))
for i in list_b:
    ind = 0
    str_1 = str()
    for j in range(len(i) - 1):
        if i[j] == "*":
            ind = 1
        while i[j] and ind == 1:
            str_1 += i[j]
            break
    list_c.append(str_1.replace("*",""))



# # 4. Расстояние между точками. На вход поступает два значение (кортежа) с
# # координатами - широта и долгота.
# # Найти расстояние между этими точками. cos(d) = sin(φА)·sin(φB) +
# # cos(φА)·cos(φB)·cos(λА − λB), где φА и φB — широты, λА, λB — долготы
# # данных пунктов, d — расстояние между пунктами, измеряется в
# # радианах длиной дуги большого круга земного шара. Расстояние между
# # пунктами, измеряемое в километрах, определяется по формуле: L = d·R,
# # где R = 6371 км — средний радиус земного шара.

float_R = 6371
# tuple_place = 48.4676804,35.0406599,\
#               48.5676804,35.1406599
tuple_place = 0,0,\
              0.00025,0

# tuple_place = (0, 0, 0, 180)  #Проверка: Половина длины "экватора" = math.pi * R
# print (math.pi * float_R)

float_fi_a, float_lambda_a, float_fi_b, float_lambda_b = tuple_place

def func_d(float_fi_a, float_lambda_a, float_fi_b, float_lambda_b):
    d = math.acos(math.sin(math.radians(float_fi_a)) *
    math.sin(math.radians(float_fi_b)) +
    math.cos(math.radians(float_fi_a)) *
    math.cos(math.radians(float_fi_b)) *
    math.cos(math.radians(float_lambda_a - float_lambda_b)))
    return d
print(
      'Расстояние между пунктами =',
      float_R * func_d(float_fi_a, float_lambda_a, float_fi_b, float_lambda_b),
      'км'
      )

list_city_map_1 = [["street", "num_house", "float_latitude", "float_longitude"]]

list_d_1 = ['\t"address_data": {']

center = [48.4676804,35.0406599]

for s in list_c:
    street_start_latitude = random.uniform(48.3826804, 48.5526804)
    street_start_longitude = random.uniform(34.9556599, 35.1256599)
    num_houses_odd = random.randrange(10, 50, 1)
    num_houses_even = random.randrange(10, 50, 1)
    street_vector = random.uniform(0, math.pi/4)
    last_latitude = street_start_latitude
    last_longitude = street_start_longitude
    last_lat_odd = street_start_latitude
    last_lat_even = street_start_latitude
    last_lon_odd = street_start_longitude
    last_lon_even = street_start_longitude

    for nh in range(1, num_houses_odd):
        houses_distance_odd = random.uniform(0.00025, 0.0025)
        if street_start_latitude >= center[0]\
                and street_start_longitude >= center[1]:
            last_lat_odd += houses_distance_odd * math.sin(street_vector)
            last_lon_odd += houses_distance_odd * math.cos(street_vector)
        elif street_start_latitude >= center[0]\
                and street_start_longitude < center[1]:
            last_lat_odd += houses_distance_odd * math.sin(street_vector)
            last_lon_odd -= houses_distance_odd * math.cos(street_vector)
        elif street_start_latitude < center[0]\
                and street_start_longitude < center[1]:
            last_lat_odd -= houses_distance_odd * math.sin(street_vector)
            last_lon_odd -= houses_distance_odd * math.cos(street_vector)
        else:
            last_lat_odd -= houses_distance_odd * math.sin(street_vector)
            last_lon_odd += houses_distance_odd * math.cos(street_vector)
        if nh % 2 > 0:
            list_d_1.append('\t\t"{}, {}": '.format(s, nh)\
                            + '[{}, {}, {}],'.format(random.randrange(1, 9, 1), last_lat_odd, last_lon_odd))

    for nh in range(2, num_houses_even):
        houses_distance = random.uniform(0.00025, 0.0025)
        if street_start_latitude >= center[0] \
                and street_start_longitude >= center[1]:
            last_lat_even += houses_distance * math.sin(street_vector)
            last_lon_even += houses_distance * math.cos(street_vector)
        elif street_start_latitude >= center[0] \
                and street_start_longitude < center[1]:
            last_lat_even += houses_distance * math.sin(street_vector)
            last_lon_even -= houses_distance * math.cos(street_vector)
        elif street_start_latitude < center[0] \
                and street_start_longitude < center[1]:
            last_lat_even -= houses_distance * math.sin(street_vector)
            last_lon_even -= houses_distance * math.cos(street_vector)
        else:
            last_lat_even -= houses_distance * math.sin(street_vector)
            last_lon_even += houses_distance * math.cos(street_vector)
        if nh % 2 == 0:
            list_d_1.append('\t\t"{}, {}": '.format(s, nh) \
                            + '[{}, {}, {}],'.format(random.randrange(1, 9, 1), last_lat_even, last_lon_even))

str_tp = list_d_1[len(list_d_1) - 1]
list_d_1[len(list_d_1) - 1] = str_tp[0: len(str_tp) - 1]
list_d_1.append('\t}')


str_wr = str()
for i in list_d_1:
    str_wr += i + "\n"
f = open('City_map_res.txt', 'w')
f.write(str_wr)
f.close()