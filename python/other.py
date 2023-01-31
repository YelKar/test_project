from turtle import *  # Подключим модуль черепашка

color('black', 'red')  # устанавливаем цвет пера и цвет заливки
speed(100)
lt(90)
k = 20  # коэффициент для настраивания более удобного масштаба
begin_fill()
for i in range(12):  # указываем число циклов необходимое до полного завершения фигуры
    rt(60)
    fd(2 * k)
    rt(60)
    fd(2 * k)
    rt(270)
end_fill()
cnt = 0
canvas = getcanvas()
up()
for x in range(-7 * k, 10 * k, k):
    for y in range(-2 * k, 15 * k, k):
        s = canvas.find_overlapping(x, y, x, y)
        goto(x, -y)
        if len(s) == 1 and s[0] == 5:
            cnt += 1
            dot(3, "yellow")
        else:
            dot(3)
print(cnt)
done()
exit()
