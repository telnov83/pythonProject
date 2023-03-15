s = int(input('Введите число в секундах: '))

m = s / 60
#m = (n - (h * 3600)) % 24
h = m / 60

print(f'{int(h)}:{int(m)}:{int(s)}')

