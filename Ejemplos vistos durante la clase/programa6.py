"""
Diccionario en python
"""

dic1 = {"hidrogeno": 1, "helio": 2, "carbon": 6}

print(dic1)

print(dic1['hidrogeno'])

dic2 = {1: "hidrogeno", 2: "helio", 6: "carbon", 3: 450}

print(dic2)
print(dic2[2])
print(dic2[3])
#Un diccionario no tiene ordenado los datos

dic3 = {}
dic3 ['H'] = {'name': 'Hidrogeno', 'number': 1, "weight": 1.963}
print(dic3)
print(dic3['H'])
print(dic3['H']['number'])