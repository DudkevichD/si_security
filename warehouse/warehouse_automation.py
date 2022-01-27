def analyse(requests):
    """
    Первым циклом анализируем, что сегодня будет отгружаться!
    Второй цикл считывает затраченную энергию.
        Если мы принимаем ящик и он есть на отгрузку мы укладываем его в начало очереди
        увеличивая энергию на 1,
        в ином случае добавляем в конец увеличивая энергию на 1.
        Если ящик отгружается то отбираются все ящики пока не найдется нужный
        эти ящики считаются за 2 энергии, нужный ящик з 1 энергию.

    :param requests: операции дня
    :return: затраченная энергия
    """
    dict_operations = {
        'выгрузить': [],
        'очередь': [],
        }
    energy_counter = 0
    for request in requests:
        if request[0] == 'выгрузить':
            dict_operations['выгрузить'].append(request[1])
    for request in requests:
        if request[0] == 'принять' and request[1] in dict_operations['выгрузить']:
            dict_operations['очередь'].insert(0, request[1])
            energy_counter += 1
        elif request[0] == 'принять' and request[1] not in dict_operations['выгрузить']:
            dict_operations['очередь'].append(request[1])
            energy_counter += 1
        elif request[0] == 'выгрузить':
            for operation in dict_operations['очередь']:
                if operation == request[1]:
                    energy_counter += 1
                    dict_operations['очередь'].remove(operation)
                    break
                else:
                    energy_counter += 2

    return energy_counter

