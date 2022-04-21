# Загрузка библиотек

from pandas import read_csv

# Загрузка датасета
url = "../datasetcreator/dataset.csv"
names = ['text', 'tag']
dataset = read_csv(url, names=names, engine='python', encoding='utf-8', error_bad_lines=False)

# shape
print(dataset.shape)

# Срез данных head
print(dataset.head(20))

# Стастические сводка методом describe
print(dataset.describe())

# Распределение по атрибуту class
print(dataset.groupby('tag').size())