# Импорт необходимых модулей
import json
import os

# Константы
DATA_FILE = "fishes.json"
operations_count = 0

# ====== ФУНКЦИИ РАБОТЫ С ФАЙЛАМИ ======

def initialize_file():
    """Инициализация файла с начальными данными"""
    if not os.path.exists(DATA_FILE):
        initial_data = [
            {
                "id": 1,
                "name": "Окунь",
                "latin_name": "Perca fluviatilis",
                "is_salt_water_fish": False,
                "sub_type_count": 3
            },
            {
                "id": 2,
                "name": "Лосось",
                "latin_name": "Salmo salar",
                "is_salt_water_fish": True,
                "sub_type_count": 5
            },
            {
                "id": 3,
                "name": "Щука",
                "latin_name": "Esox lucius",
                "is_salt_water_fish": False,
                "sub_type_count": 7
            },
            {
                "id": 4,
                "name": "Тунец",
                "latin_name": "Thunnus",
                "is_salt_water_fish": True,
                "sub_type_count": 15
            },
            {
                "id": 5,
                "name": "Карп",
                "latin_name": "Cyprinus carpio",
                "is_salt_water_fish": False,
                "sub_type_count": 12
            }
        ]
        
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)
        print("Файл данных инициализирован с начальными записями.")

def load_data():
    """Загрузка данных из файла"""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка загрузки данных: {e}")
        return []

def save_data(data):
    """Сохранение данных в файл"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Ошибка сохранения данных: {e}")
        return False

# ====== ФУНКЦИИ ВАЛИДАЦИИ ======

def validate_id(fish_id, data):
    """Проверка корректности ID"""
    try:
        fish_id = int(fish_id)
        if fish_id <= 0:
            return False, "ID должен быть положительным числом"
        
        # Проверка на уникальность (при добавлении)
        for fish in data:
            if fish["id"] == fish_id:
                return False, f"ID {fish_id} уже существует"
        return True, fish_id
    except ValueError:
        return False, "ID должен быть целым числом"

def validate_name(name):
    """Проверка корректности названия"""
    if not name or not name.strip():
        return False, "Название не может быть пустым"
    if len(name.strip()) < 2:
        return False, "Название должно содержать минимум 2 символа"
    return True, name.strip()

def validate_latin_name(latin_name):
    """Проверка корректности латинского названия"""
    if not latin_name or not latin_name.strip():
        return False, "Латинское название не может быть пустым"
    if len(latin_name.strip()) < 2:
        return False, "Латинское название должно содержать минимум 2 символа"
    return True, latin_name.strip()

def validate_water_type(input_str):
    """Проверка и преобразование типа воды"""
    input_str = input_str.strip().lower()
    if input_str in ["да", "yes", "1", "true", "y", "д"]:
        return True, True
    elif input_str in ["нет", "no", "0", "false", "n", "н"]:
        return True, False
    else:
        return False, "Введите 'да' или 'нет'"

def validate_subtype_count(count):
    """Проверка корректности количества подвидов"""
    try:
        count = int(count)
        if count < 0:
            return False, "Количество подвидов не может быть отрицательным"
        if count > 1000:
            return False, "Количество подвидов слишком большое (максимум 1000)"
        return True, count
    except ValueError:
        return False, "Количество подвидов должно быть целым числом"

# ====== ФУНКЦИИ ОСНОВНОГО ФУНКЦИОНАЛА ======

def display_all_records():
    """Вывод всех записей"""
    global operations_count
    data = load_data()
    
    operations_count += 1
    
    if not data:
        print("\nБаза данных пуста!")
        return
    
    print("\n" + "=" * 60)
    print(f"ВСЕ ЗАПИСИ О РЫБАХ (всего: {len(data)})")
    print("=" * 60)
    
    for i, fish in enumerate(data, 1):
        water_type = "морская" if fish["is_salt_water_fish"] else "пресноводная"
        print(f"\n--- Рыба #{i} ---")
        print(f"ID: {fish['id']}")
        print(f"Название: {fish['name']}")
        print(f"Латинское название: {fish['latin_name']}")
        print(f"Тип: {water_type}")
        print(f"Количество подвидов: {fish['sub_type_count']}")

def find_record_by_id():
    """Поиск и вывод записи по ID"""
    global operations_count
    data = load_data()
    
    if not data:
        print("\nБаза данных пуста!")
        return
    
    fish_id_input = input("Введите ID рыбы для поиска: ").strip()
    
    # Валидация ID для поиска
    try:
        fish_id = int(fish_id_input)
        if fish_id <= 0:
            print("Ошибка: ID должен быть положительным числом!")
            return
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return
    
    operations_count += 1
    
    found = False
    for index, fish in enumerate(data):
        if fish["id"] == fish_id:
            found = True
            water_type = "морская" if fish["is_salt_water_fish"] else "пресноводная"
            
            print("\n" + "=" * 40)
            print("НАЙДЕНА ЗАПИСЬ:")
            print("=" * 40)
            print(f"Позиция в списке: {index}")
            print(f"ID: {fish['id']}")
            print(f"Название: {fish['name']}")
            print(f"Латинское название: {fish['latin_name']}")
            print(f"Тип: {water_type}")
            print(f"Количество подвидов: {fish['sub_type_count']}")
            break
    
    if not found:
        print(f"\n⚠️  Рыба с ID {fish_id} не найдена!")

def add_new_record():
    """Добавление новой записи"""
    global operations_count
    data = load_data()
    
    print("\nДОБАВЛЕНИЕ НОВОЙ ЗАПИСИ О РЫБЕ")
    print("=" * 30)
    
    # Находим максимальный ID для генерации нового
    max_id = max([fish["id"] for fish in data]) if data else 0
    new_id = max_id + 1
    
    # Ввод и валидация названия
    while True:
        name = input("Введите название рыбы: ").strip()
        is_valid, result = validate_name(name)
        if is_valid:
            name = result
            break
        else:
            print(f"Ошибка: {result}")
    
    # Ввод и валидация латинского названия
    while True:
        latin_name = input("Введите латинское название: ").strip()
        is_valid, result = validate_latin_name(latin_name)
        if is_valid:
            latin_name = result
            break
        else:
            print(f"Ошибка: {result}")
    
    # Ввод и валидация типа воды
    while True:
        water_input = input("Морская рыба? (да/нет): ").strip()
        is_valid, result = validate_water_type(water_input)
        if is_valid:
            is_salt_water_fish = result
            break
        else:
            print(f"Ошибка: {result}")
    
    # Ввод и валидация количества подвидов
    while True:
        sub_type_input = input("Введите количество подвидов: ").strip()
        is_valid, result = validate_subtype_count(sub_type_input)
        if is_valid:
            sub_type_count = result
            break
        else:
            print(f"Ошибка: {result}")
    
    # Создание новой записи
    new_fish = {
        "id": new_id,
        "name": name,
        "latin_name": latin_name,
        "is_salt_water_fish": is_salt_water_fish,
        "sub_type_count": sub_type_count
    }
    
    # Добавление и сохранение
    data.append(new_fish)
    if save_data(data):
        operations_count += 1
        print(f"\n✅ Запись успешно добавлена с ID {new_id}!")
    else:
        print("\n❌ Ошибка при сохранении записи!")

def delete_record_by_id():
    """Удаление записи по ID"""
    global operations_count
    data = load_data()
    
    if not data:
        print("\nБаза данных пуста!")
        return
    
    # Ввод и валидация ID
    while True:
        fish_id_input = input("Введите ID рыбы для удаления: ").strip()
        try:
            fish_id = int(fish_id_input)
            if fish_id <= 0:
                print("Ошибка: ID должен быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка: ID должен быть числом!")
    
    operations_count += 1
    
    # Поиск записи
    found_index = -1
    fish_to_delete = None
    
    for index, fish in enumerate(data):
        if fish["id"] == fish_id:
            found_index = index
            fish_to_delete = fish
            break
    
    if found_index != -1 and fish_to_delete:
        # Подтверждение удаления
        confirm = input(f"Удалить рыбу '{fish_to_delete['name']}' (ID: {fish_id})? (да/нет): ").strip().lower()
        
        if confirm in ["да", "yes", "y", "д"]:
            # Удаление записи
            deleted_fish = data.pop(found_index)
            
            if save_data(data):
                print(f"\n✅ Рыба '{deleted_fish['name']}' успешно удалена!")
            else:
                print("\n❌ Ошибка при сохранении изменений!")
        else:
            print("Удаление отменено.")
    else:
        print(f"\n⚠️  Рыба с ID {fish_id} не найдена!")

def display_menu():
    """Отображение главного меню"""
    print("\n" + "=" * 40)
    print("МЕНЮ УПРАВЛЕНИЯ БАЗОЙ ДАННЫХ РЫБ")
    print("=" * 40)
    print("1. Вывести все записи")
    print("2. Найти запись по ID")
    print("3. Добавить запись")
    print("4. Удалить запись по ID")
    print("5. Выйти из программы")
    print("=" * 40)

def exit_program():
    """Выход из программы"""
    global operations_count
    print("\n" + "=" * 40)
    print("ВЫХОД ИЗ ПРОГРАММЫ")
    print("=" * 40)
    print(f"Всего выполнено операций: {operations_count}")
    print("До свидания!")
    return False

# ====== ГЛАВНАЯ ФУНКЦИЯ ======

def main():
    """Основная функция программы"""
    global operations_count
    
    # Инициализация файла с данными
    initialize_file()
    
    # Основной цикл программы
    running = True
    while running:
        display_menu()
        
        choice = input("Выберите пункт меню (1-5): ").strip()
        
        if choice == "1":
            display_all_records()
        elif choice == "2":
            find_record_by_id()
        elif choice == "3":
            add_new_record()
        elif choice == "4":
            delete_record_by_id()
        elif choice == "5":
            running = exit_program()
        else:
            print("\n❌ Ошибка: выберите пункт от 1 до 5!")

# ====== ТОЧКА ВХОДА ======

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nПрограмма прервана пользователем.")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
