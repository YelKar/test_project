import pyautogui as pg


# Получение позиции мыши и вывод в консоль
print(pg.position())

# Передвижение мыши
pg.move(50, 50, duration=0.5)
pg.moveTo(150, 200, 0.5) # Передвигаем к точке относительно экрана

# Нажатие мышкой по определенной точке
pg.click(769, 101)
pg.doubleClick(769, 101) # двойное нажатие
pg.rightClick(769, 101) # нажатие правой кнопкной мыши
pg.leftClick(769, 101) # нажатие левой кнопкной мыши

# Ввод текста
pg.typewrite("itproger.com")

# Выполнения нажатия на клавишу
pg.typewrite(["enter"])

# Выполнения нажатия на сочетание клавиш
pg.hotkey("winleft")
pg.hotkey("winleft", "up")
pg.hotkey("ctrl", "t")

# Вызов различных всплывающих окон
pg.alert("Окно с информацией", "Название окна", button="Текст на кнопке")
age = pg.prompt("Укажите возраст: ", "Название окна")
print(age)
pg.confirm("Вам больше 18?", "Название окна", ("Да, точно", "Нет"))
pg.password("Введите пароль", "Название окна")

# Создание скриншота
pg.screenshot("yourPic.png")

# Мини программа
website = pg.prompt("Введите название сайта:", "Веб сайт", "https://")
pg.click(769, 101)
pg.typewrite(website)
pg.typewrite(["enter"])
pg.screenshot("yourPic.png")