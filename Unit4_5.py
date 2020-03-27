a = ['2018-01-01', 'yandex', 'cpc', 100]
i = 0
el = {a[-2] : a[-1]}
while i < (len(a) - 2):
    res = {a[-3 - i]: el}
    el = res
    i += 1
print(res)