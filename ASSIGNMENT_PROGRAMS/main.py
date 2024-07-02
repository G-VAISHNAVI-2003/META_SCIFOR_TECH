"""import requests
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
if response.status_code == 200:
    print("Data received")
    print(response.text)
else:
    print("Not received Data")
"""

import requests
url = "https://restcountries.com/v3.1/all"
res = requests.get(url)
data = res.json()
names = [country["name"]["common"] for country in data]
for i in names:
    print(i)


"""import random
x = [1,2,3,4,5,6]
print(random.choice(x))
y = random.randint(1,10)
print(y)
"""

import datetime
x = datetime.datetime.now()
print(x.year)

import math
x = math.sqrt(16)
print(x)

