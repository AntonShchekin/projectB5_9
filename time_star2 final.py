import time
class Timer:
    # Определяем класс
    # Пишем конструктор класса
    def __init__(self, num_runs = 1000):
        # Конструктор принимает аргумент num_runs - количество запусков функции при замере
        self.num_runs = num_runs
        # Конструктор
    def __call__(self, func):
    # декоратор
        def wrap(*args, **kwargs):
            avg_time = 0
            for i in range(self.num_runs):
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs  
            print("Выполнение заняло %.5f секунд" % avg_time)
     # Возвращаем обёртку
        return wrap

    def __enter__(self):
        self.t0 = time.time()
        
    def __exit__(self, *args):
        t1 = time.time()
        avg_time = (t1-self.t0)
        print(f"Среднее время выполнения - {avg_time:.5f}")

# Создаём объект класса
timer_10 = Timer(num_runs = 1000)
# Используем объект, как декоратор
 


@timer_10
def f():
    for i in range(10000):
        pass
# Вызываем функцию
print("Тестируем объект класса в качестве декоратора")
f()

print("Тестируем в качетве контекстного менеджера")
with Timer() as t:
    a = list(range(1000000, 1, -1))
    a.sort()