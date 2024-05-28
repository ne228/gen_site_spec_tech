import os
import re

def generate_index(save_path, book_path):
    # Открываем исходный HTML-файл
    with open(book_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Строка, которую нужно вставить
    str_to_insert = """
    <link href="../../style.css" rel="stylesheet" />
    <script src="../../js/header.js"></script>
    """
    html_content = re.sub(r'(<body.*?>)', r'\1' + str_to_insert, html_content, flags=re.DOTALL)

    # Сохраняем изменения в новом HTML-файле
    path = save_path
    with open(path, "w", encoding="utf-8") as f:
        f.write(html_content)
    