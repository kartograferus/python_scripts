input_height = float(input('Введите высоту, с которой вы пускаете попрыгунчик:'))

bounces = 0
height_now = input_height
while bounces < 10:
    height_now = round(height_now * 0.6, 2)
    bounces += 1
    print(bounces, ': ', height_now)

