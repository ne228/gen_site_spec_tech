import os


def generate_index(path_to_folders, path_to_generate, title):
    
    first =  """
        <!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>{title}</title>
                <!-- Подключение Bootstrap CSS -->
                <link
                href="../../css/bootstrap.min.css"
                rel="stylesheet"
                />
                <link href="../../style.css" rel="stylesheet" />
                <!-- Подключение Material Icons -->
                <link
                href="https://fonts.googleapis.com/icon?family=Material+Icons"
                rel="stylesheet"
                />
            </head>
            <body>
                <!-- Шапка страницы -->

                <div class="my-container">
                <h7 class="ml-5 mt-5"
                    ><strong
                    >{title}
                    </strong></h7
                >

                <div class="list-group mt-3">
    """
    second = """
                </div>
            </div>

            <!-- Подключение Bootstrap JS (необязательно, если не планируете использовать JavaScript-компоненты) -->
            <script src="../../js/bootstrap.bundle.min.js"></script>
            <script src="../../js/header.js"></script>
        </body>
        </html>

    """
    template = """
     <div>
          <a href="{href}" class="list-group-item list-group-item-action" aria-current="true">
           <img class="list-item-icon" src="../../icons/file.svg" alt="hashtag">
          {val}</a>
        </div>
    """
    midle = ""
    for path in path_to_folders:
        insert = template
        path = path.replace("\\", "/")
        midle += insert.format(href=path, val=path.replace(".html", "")) + "\n"
        
    res = first.format(title=title) + midle + second
    path = os.path.join(path_to_generate, "index.html")
    print(path)
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(res)
        # print("HTML файл успешно создан по пути:", path)
    except Exception as e:
        print("Ошибка при создании HTML файла:", e)


    return res
        
    