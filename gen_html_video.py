import os


def generate_index(save_path, title):
    
    first =  """
            <!DOCTYPE html>
            <html lang="ru">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Учебник</title>
                <!-- Подключение Bootstrap CSS -->
                <link href="../../css/bootstrap.min.css" rel="stylesheet" />
                <link href="../../style.css" rel="stylesheet" />
                <link
                href="../../css/video-js.min.css"
                rel="stylesheet"
            />
                <!-- Подключение Material Icons -->
            </head>
            <body>
                <div class="container">
                <h4 class="mt-3 ml-5">
                    <strong
                    >{title}</strong
                    >
                </h4>
                <div class="video-container"> 
                <video
                        id="my-player"
                        class="video-js"
                        controls
                        preload="auto"
                        poster="../../icons/play.svg"
                        data-setup='{title}'>
    """
    second = """
            <p class="vjs-no-js">
                        To view this video please enable JavaScript, and consider upgrading to a
                        web browser that
                        <a href="https://videojs.com/html5-video-support/" target="_blank">
                            supports HTML5 video
                        </a>
                        </p>
                    </video>
                </div>
                </div>

                <!-- Подключение Bootstrap JS (необязательно, если не планируете использовать JavaScript-компоненты) -->
                <script src="../../js/bootstrap.bundle.min.js"></script>
                <script src="../../js/header.js"></script>
                <script src="../../js/footer.js"></script>
            
                <script src="../../js/video.min.js"></script>
            </body>
            </html>

    """

    midle ="""
             <source src="{val}" 
            type="video/mp4"></source>
    """
    src = title
    title = title.replace(".mp4", "")
    res = first.format(title=title) + midle.format(val=src) + second
    path = save_path.replace(".mp4", ".html")
    print(path)
    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(res)
        # print("HTML файл успешно создан по пути:", path)
    except Exception as e:
        print("Ошибка при создании HTML файла:", e)


    return res
        
    