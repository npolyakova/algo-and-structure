# Задача 2
# Необходимо найти самые релевантные объекты (с наибольшим значением формулы релевантности)

class Relevance:
    __characteristics__ = []
    __parameters__ = []
    __queries__ = []

    def __init__(self):
        # 1. кол-во параметров в формуле ранжирования
        n = int(input("Введите кол-во параметров - n, больше 1 и меньше 100 "))

        if n > 100 or n < 1:
            print("Число должно быть больше 1 и меньше 100")
            exit()
        else:
            # 2. параметры
            print("Введите параметры через пробел")
            nums1 = input().split()
            i = 0

            while i < n:
                self.__parameters__.append(int(nums1[i]))
                print(self.__parameters__[i])
                i += 1

            # 3. кол-во объектов
            print("Введите кол-во объектов")
            d = int(input())

            if (d < 10 or d > 100_000) or (d * n > 100_000):
                print("Введено неверное кол-во объектов")
                exit()
            else:
                # числовые признаки
                i = 0
                while i < d:
                    print("Введите характеристики объекта " + str(i + 1))
                    nums3 = input().split()
                    j = 0
                    sub_chars = []
                    while j < n:
                        sub_chars.append(int(nums3[j]))
                        j += 1
                    self.__characteristics__.append(sub_chars)
                    i += 1
                print(self.__characteristics__)

                # кол-во запросов к системе ранжирования
                print("Введите кол-во запросов")
                query = int(input())

                if query < 1 or query > 100_000:
                    print("Введено неверное кол-во запросов")
                    exit()
                else:
                    # запросы
                    i = 0
                    while i < query:
                        print("Введите запрос " + str(i + 1))
                        nums4 = input().split()
                        if len(nums4) == 2:
                            if int(nums4[0]) == 1 and (1 <= int(nums4[1]) <= 10):
                                self.__queries__.append(nums4)
                                i += 1
                            else:
                                print("Введен некорректный запрос, попробуйте ещё раз")

                        if len(nums4) == 4:
                            if (int(nums4[0]) == 2 and
                                    (1 <= int(nums4[1]) <= d) and
                                    (1 <= int(nums4[2]) <= n) and
                                    int(nums4[3]) >= 0):
                                    self.__queries__.append(nums4)
                                    i += 1
                            else:
                                print("Введен некорректный запрос, попробуйте ещё раз")

                        if len(nums4) != 2 and len(nums4) != 4:
                            print("Введен некорректный запрос, попробуйте ещё раз")

    def execute_query(self):
        for i in range(len(self.__queries__)):
            if self.__queries__[i][0] == '1':
                self.print_relevance(int(self.__queries__[i][1]))
                print()
            if self.__queries__[i][0] == '2':
                self.__change_chars__(int(self.__queries__[i][1]), int(self.__queries__[i][2]), int(self.__queries__[i][3]))
                print()

    def __sum_relevance__(self):
        # умножаем параметры на характеристики
        rel = []
        for i in range(len(self.__characteristics__)):
            res = 0
            for j in range(len(self.__characteristics__[0])):
                res += self.__parameters__[j] * self.__characteristics__[i][j]
            rel.append(int(res))
        return rel

    def sort(self):
        rel = self.__sum_relevance__()

        # складываем значения в словарь для последующей сортировки
        objects_with_relevance = dict.fromkeys(range(0, len(self.__characteristics__)))
        for i in range(len(objects_with_relevance) - 1, -1, -1):
            objects_with_relevance[i] = rel.pop()

        # сортируем и возвращаем результат
        return sorted(objects_with_relevance.items(), key=lambda x:x[1], reverse=True)

    def print_relevance(self, count: int = 0):
        sorted_objects_with_relevance = self.sort()
        if count == 0:
            for i in range(len(sorted_objects_with_relevance)):
                print(sorted_objects_with_relevance[i][0] + 1, sorted_objects_with_relevance[i][1])
        else:
            for i in range(0, count):
                print(sorted_objects_with_relevance[i][0] + 1, sorted_objects_with_relevance[i][1])

    def __change_chars__(self, object_number: int, param: int, value: int):
        self.__characteristics__[object_number - 1][param - 1] = value

# результаты
relevance = Relevance()
relevance.execute_query()