import os
import sys

def list_files_to_file(output_file, directory, extension):
    try:
        # Открываем файл для записи
        with open(output_file, 'w') as file:
            # Проходимся по всем файлам в заданном каталоге
            for root, _, files in os.walk(directory):
                for name in files:
                    # Проверяем расширение файла
                    if name.endswith(extension):
                        # Записываем полный путь к файлу
                        file.write(os.path.join(root, name) + '\n')
        print(f"Список файлов записан в {output_file}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    # Проверяем количество аргументов
    if len(sys.argv) != 4:
        print("Использование: python script.py <output_file> <directory> <extension>")
        sys.exit(1)

    # Получаем аргументы
    output_file = sys.argv[1]
    directory = sys.argv[2]
    extension = sys.argv[3]

    # Вызываем функцию
    list_files_to_file(output_file, directory, extension)
