import collections
a=input("Введите текст:")
data=collections.Counter(a)
print(data.most_common())
