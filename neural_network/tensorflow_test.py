import numpy as np
from tensorflow import keras
from telebot import TeleBot


bot = TeleBot("5553841032:AAE4adRQ2gctEbgV6lL-ACgOxuiXq6HKU6s")

my_id = 1884965431

model = keras.Sequential([
    keras.layers.Dense(20, input_shape=[1]),
])


model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array(list(map(float, range(40))), dtype=float)
ys = np.array([((x - 32) * 5 / 9) for x in xs], dtype=float)

model.fit(xs, ys, epochs=100000)

par = [68, 32, 86]


for x, y in zip(par, model.predict(par)):
    print(bot.send_message(my_id, f"{x} => {np.mean(y)}").text)

# print(ys)
