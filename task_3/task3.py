#Даниил

# Импорт необходимых модулей
import json  # для работы с JSON файлами
import os    # для проверки существования файла

# Константа с именем файла для хранения данных
DATA_FILE = "fishes.json"

# Счетчик операций с записями
operations_count = 0

# ====== БЛОК ИНИЦИАЛИЗАЦИИ ФАЙЛА ======
# Проверяем, существует ли файл с данными
if not os.path.exists(DATA_FILE):
    # Если файла нет, создаем начальные данные (5 записей)
    initial_data = [
        {
            "id": 1,  # уникальный номер записи
            "name": "Окунь",  # общее название
            "latin_name": "Perca fluviatilis",  # научное название
            "is_salt_water_fish": False,  # тип воды: False = пресноводная
            "sub_type_count": 3  # количество подвидов
        },
        # ... еще 4 аналогичные записи
    ]
    
    # Записываем начальные данные в файл
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(initial_data, f, ensure_ascii=False, indent=2)

# ====== ОСНОВНОЙ ЦИКЛ ПРОГРАММЫ ======
# Бесконечный цикл, пока пользователь не выберет выход
while True:
    # Вывод меню на экран
    print("\n" + "=" * 40)
    print("МЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ РЫБ")
    print("=" * 40)
    print("1. Вывести все записи")
    print("2. Вывести запись по полю (id)")
    print("3. Добавить запись")
    print("4. Удалить запись по полю (id)")
    print("5. Выйти из программы")
    print("=" * 40)
    
    # Обработка возможных ошибок ввода
    try:
        # Получаем выбор пользователя
        choice = input("Выберите пункт меню (1-5): ").strip()
        
        # ====== ПУНКТ 1: ВЫВЕСТИ ВСЕ ЗАПИСИ ======
        if choice == "1":
            # Открываем и читаем файл с данными
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)  # загружаем все записи в переменную data
            
            # Увеличиваем счетчик операций
            operations_count += 1
            
            # Проверяем, есть ли записи в файле
            if not data:
                print("\nБаза данных пуста!")
            else:
                # Выводим заголовок с количеством записей
                print("\n" + "=" * 60)
                print(f"ВСЕ ЗАПИСИ О РЫБАХ (всего: {len(data)})")
                print("=" * 60)
                
                # Перебираем все записи с помощью enumerate
                # enumerate(data, 1) дает пары: (номер_начиная_с_1, запись)
                for i, fish in enumerate(data, 1):
                    # Определяем тип воды на основе булевого значения
                    water_type = "морская" if fish["is_salt_water_fish"] else "пресноводная"
                    
                    # Форматированный вывод информации о рыбе
                    print(f"\n--- Рыба #{i} ---")
                    print(f"ID: {fish['id']}")
                    print(f"Название: {fish['name']}")
                    print(f"Латинское название: {fish['latin_name']}")
                    print(f"Тип: {water_type}")
                    print(f"Количество подвидов: {fish['sub_type_count']}")
        
        # ====== ПУНКТ 2: ВЫВЕСТИ ЗАПИСЬ ПО ID ======
        elif choice == "2":
            try:
                # Пытаемся преобразовать ввод в число
                fish_id = int(input("Введите ID рыбы для поиска: "))
            except ValueError:
                # Если введено не число, выводим ошибку
                print("Ошибка: ID должен быть числом!")
                continue  # возвращаемся в начало цикла
            
            # Читаем данные из файла
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Увеличиваем счетчик операций
            operations_count += 1
            
            # Флаг для отслеживания, найдена ли запись
            found = False
            
            # Ищем запись с нужным ID
            # enumerate(data) дает пары: (индекс_в_списке, запись)
            for index, fish in enumerate(data):
                if fish["id"] == fish_id:
                    found = True  # запись найдена
                    
                    # Определяем тип воды
                    water_type = "морская" if fish["is_salt_water_fish"] else "пресноводная"
                    
                    # Выводим найденную запись
                    print("\n" + "=" * 40)
                    print("НАЙДЕНА ЗАПИСЬ:")
                    print("=" * 40)
                    print(f"Позиция в словаре: {index}")  # позиция в списке
                    print(f"ID: {fish['id']}")
                    print(f"Название: {fish['name']}")
                    print(f"Латинское название: {fish['latin_name']}")
                    print(f"Тип: {water_type}")
                    print(f"Количество подвидов: {fish['sub_type_count']}")
                    break  # прерываем цикл поиска
            
            # Если запись не найдена, выводим предупреждение
            if not found:
                print(f"\n⚠️  Предупреждение: Рыба с ID {fish_id} не найдена!")
        
        # ====== ПУНКТ 3: ДОБАВИТЬ ЗАПИСЬ ======
        elif choice == "3":
            print("\nДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ О РЫБЕ")
            print("=" * 30)
            
            # Читаем текущие данные
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Находим максимальный ID среди существующих записей
            # Если data пуст, возвращаем 0
            max_id = max([fish["id"] for fish in data]) if data else 0
            
            try:
                # Новый ID на 1 больше максимального
                new_id = max_id + 1
                
                # Получаем данные от пользователя
                name = input("Введите название рыбы: ").strip()
                latin_name = input("Введите латинское название: ").strip()
                
                # Определяем тип воды на основе ответа пользователя
                water_input = input("Морская рыба? (да/нет): ").strip().lower()
                # Если ответ "да", "yes", "1" или "true" - морская рыба
                is_salt_water_fish = water_input in ["да", "yes", "1", "true"]
                
                # Получаем количество подвидов (преобразуем в число)
                sub_type_count = int(input("Введите количество подвидов: "))
                
                # ====== ПРОВЕРКА ВВЕДЕННЫХ ДАННЫХ ======
                # Проверяем, что названия не пустые
                if not name or not latin_name:
                    print("Ошибка: название и латинское название не могут быть пустыми!")
                    continue
                
                # Проверяем, что количество подвидов не отрицательное
                if sub_type_count < 0:
                    print("Ошибка: количество подвидов не может быть отрицательным!")
                    continue
                
                # Создаем новую запись (словарь)
                new_fish = {
                    "id": new_id,
                    "name": name,
                    "latin_name": latin_name,
                    "is_salt_water_fish": is_salt_water_fish,
                    "sub_type_count": sub_type_count
                }
                
                # Добавляем новую запись в список
                data.append(new_fish)
                
                # Сохраняем обновленные данные в файл
                with open(DATA_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                # Увеличиваем счетчик операций
                operations_count += 1
                
                # Сообщаем об успешном добавлении
                print(f"\n✅ Запись успешно добавлена с ID {new_id}!")
                
            # Если введены некорректные данные (например, буквы вместо числа)
            except ValueError:
                print("Ошибка: некорректный ввод данных!")
        
        # ====== ПУНКТ 4: УДАЛИТЬ ЗАПИСЬ ПО ID ======
        elif choice == "4":
            try:
                # Получаем ID для удаления
                fish_id = int(input("Введите ID рыбы для удаления: "))
            except ValueError:
                print("Ошибка: ID должен быть числом!")
                continue
            
            # Читаем данные из файла
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Увеличиваем счетчик операций
            operations_count += 1
            
            # Ищем индекс записи с нужным ID
            found_index = -1  # -1 означает "не найдено"
            
            for index, fish in enumerate(data):
                if fish["id"] == fish_id:
                    found_index = index  # сохраняем индекс найденной записи
                    break  # прерываем поиск
            
            # Если запись найдена (индекс не -1)
            if found_index != -1:
                # Получаем запись для удаления
                fish_to_delete = data[found_index]
                
                # Запрашиваем подтверждение удаления
                confirm = input(f"Удалить рыбу '{fish_to_delete['name']}' (ID: {fish_id})? (да/нет): ").strip().lower()
                
                # Если пользователь подтверждает удаление
                if confirm in ["да", "yes", "y"]:
                    # Удаляем запись по индексу и сохраняем удаленную запись
                    deleted_fish = data.pop(found_index)
                    
                    # Сохраняем обновленные данные в файл
                    with open(DATA_FILE, "w", encoding="utf-8") as f:
                        json.dump(data, f, ensure_ascii=False, indent=2)
                    
                    # Сообщаем об успешном удалении
                    print(f"\n✅ Рыба '{deleted_fish['name']}' успешно удалена!")
                else:
                    # Если удаление отменено
                    print("Удаление отменено.")
            else:
                # Если запись не найдена
                print(f"\n⚠️  Предупреждение: Рыба с ID {fish_id} не найдена!")
        
        # ====== ПУНКТ 5: ВЫХОД ИЗ ПРОГРАММЫ ======
        elif choice == "5":
            print("\n" + "=" * 40)
            print("ВЫХОД ИЗ ПРОГРАММЫ")
            print("=" * 40)
            # Выводим количество выполненных операций
            print(f"Всего выполнено операций: {operations_count}")
            print("До свидания!")
            break  # прерываем цикл, программа завершается
        
        # ====== НЕКОРРЕКТНЫЙ ВЫБОР ======
        else:
            print("\n❌ Ошибка: выберите пункт от 1 до 5!")
    
    # ====== ОБРАБОТКА ОШИБОК ======
    except Exception as e:
        # Если произошла любая ошибка, выводим сообщение
        print(f"\n❌ Произошла ошибка: {e}")
        print("Попробуйте еще раз.")