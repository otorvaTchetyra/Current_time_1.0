import time

# Функция для вывода текущего времени
def current_time():
    now = time.localtime()
    current_time = time.strftime("%H:%M:%S", now)
    print(current_time)

# Основной цикл
while True:
    current_time()
    time.sleep(5)  # Ждем 5 секунд перед следующим вызовом