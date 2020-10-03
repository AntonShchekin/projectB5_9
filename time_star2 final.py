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
            for _ in range(self.num_runs):  # i не используется поэтому можно заменить на _
                t0 = time.time()
                func(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs  
            print("Выполнение заняло %.5f секунд" % avg_time)
     # Возвращаем обёртку
        return wrap

    def __enter__(self):
        """
        в вашем случае with Timer() as t: ничего не возвращет t = None

        вот можно использовать return self
        тогда можно использовать Timer вот так
        with Timer() as decor:
            b = decor(sleep_3s)
        """
        self.t0 = time.time()
        
    def __exit__(self, *args):
        t1 = time.time()
        avg_time = (t1-self.t0)
        print(f"Среднее время выполнения - {avg_time:.5f}")

@Timer(2)  # Timer можно создать тут не используя отдельную переменную
def sleep_3s():
    """
    функция эталон - задержка 3 секунды
    """
    time.sleep(3)

if __name__ == '__main__':
    with Timer():
        sleep_3s()