#Даниил 

import json  # Импортируем модуль для работы с JSON файлами

# Чтение файла
with open('dump.json', 'r', encoding='utf-8') as f:  # Открываем файл для чтения
    data = json.load(f)  # Загружаем JSON данные в переменную data

# Ввод кода
code = input("Введите номер квалификации: ").strip()  # Получаем код от пользователя

# Поиск
found = False  # Флаг для отслеживания, найдена ли квалификация
for item in data:  # Перебираем все элементы в данных
    if item.get('model') == 'data.skill':  # Проверяем, что это нужный тип данных
        fields = item.get('fields', {})  # Получаем поля элемента
        if fields.get('code') == code:  # Сравниваем код с введенным
            # Нашли квалификацию
            qual_name = fields.get('title', '')  # Получаем название квалификации
            specialty_id = fields.get('specialty')  # Получаем ID специальности
            
            # Ищем специальность
            spec_code = ""
            spec_name = ""
            if specialty_id:  # Если есть ID специальности
                for spec_item in data:  # Ищем специальность в данных
                    if (spec_item.get('model') == 'data.skill' and 
                        spec_item.get('pk') == specialty_id):  # Нашли специальность по ID
                        spec_fields = spec_item.get('fields', {})
                        spec_code = spec_fields.get('code', '')  # Код специальности
                        spec_name = spec_fields.get('title', '')  # Название специальности
                        break  # Прерываем поиск
            
            # Вывод результата
            print("\n" + "=" * 15 + " Найдено " + "=" * 15)
            if spec_code:  # Если нашли специальность
                print(f"{spec_code} >> Специальность \"{spec_name}\", ПТО")
            print(f"{code} >> Квалификация \"{qual_name}\"")
            
            found = True  # Устанавливаем флаг "найдено"
            break  # Прерываем цикл поиска

if not found:  # Если квалификация не найдена
    print("\n" + "=" * 15 + " Не найдено " + "=" * 15)