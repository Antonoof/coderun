import sys

def main():
    n = int(input())
    numbers = []

    for _ in range(n):
        broken_number = input()
        # добавляем только цифры
        phone_number = [d for d in broken_number if d.isdigit()]
        # объединяем цифры в строку
        phone_number = "".join(phone_number)
        # сохраняем длинну телефона, нужна для проверки 2 теста
        len_number = len(phone_number)
        # добавляем как кортеж значений
        numbers.append((phone_number, len_number))

    m = int(input())
    samples = []

    for _ in range(m):
        # разъединяем дефисом
        broken_sample, data = input().split('-')
        # для красивого вывода
        data = '-' + data
        # также проверка как во 2 тесте
        len_sample = len(broken_sample) - 6
        # префикс необходим для правильного вывода
        # когда будем сравнивать мы потеряем COUNTRY_CODE и OPERATOR_CODE
        pre = broken_sample.split()
        prefix_number = pre[0] + ' ' + pre[1]
        # проверка 0-9
        phone_sample = [d for d in broken_sample if d.isdigit()]
        phone_sample = "".join(phone_sample)
        # Если не указать будет падать 4 тест из 7
        # 123X in 4123 даст True, а 123 != 412 -> False 
        len_to_number = len(phone_sample)

        samples.append((phone_sample, len_sample, data, prefix_number, len_to_number))

    for number, len_number in numbers:
        for sample, len_sample, data, pref, len_to_number in samples:
            if sample == number[:len_to_number] and len_number == len_sample:
                # +()' ' то что необходимо убрать
                to_del = len(pref) - 4
                res_number = number[to_del:]
                print(pref, res_number, data)


if __name__ == '__main__':
    main()
