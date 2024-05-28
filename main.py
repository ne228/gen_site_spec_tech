import os

import shutil

import gen_root_index
import gen_html_pdf

import gen_html_video
import gen_theme_index
import gen_part_index
import gen_html_zip

   

def get_folder_name(full_path):
    folder_name = os.path.basename(full_path)
    return folder_name
 
 
 
paths = [ "D:\\Work\\Учебник для СПЕЦ ТЕХНИКИ\\38.01.05 ЭБ 2024",
         "D:\\Work\\Учебник для СПЕЦ ТЕХНИКИ\\38.05.01 ФИН 2024",
         "D:\\Work\\Учебник для СПЕЦ ТЕХНИКИ\\40.05.01 ПР 2024",
         "D:\\Work\\Учебник для СПЕЦ ТЕХНИКИ\\40.05.03 СЭ 2024"]

book_names = [
    "Электронное учебное пособие «Теория, методика и практика разработки учебно-методического обеспечения образовательного процесса по дисциплине «Специальная техника органов внутренних дел» по специальности 38.05.01 Экономическая безопасность (специализация экономико-правовое обеспечение экономической безопасности).",
    "Электронное учебное пособие «Теория, методика и практика разработки учебно-методического обеспечения образовательного процесса по дисциплине «Специальная техника органов внутренних дел» по специальности 38.05.01 Экономическая безопасность (специализация финансовый учет и контроль в правоохранительных органах).",
    "Электронное учебное пособие «Методическая подготовка педагогов к профессиональной деятельности в системе профессионального и дополнительного образования по дисциплине «Специальная техника органов внутренних дел»» по специальности 40.05.01 Правовое обеспечение национальной безопасности (специализация Уголовно-правовая, узкая специализация предварительное следствие в органах внутренних дел).",
    "Электронное учебное пособие «Методическая подготовка педагогов к профессиональной деятельности в системе профессионального и дополнительного образования по дисциплине «Специальная техника органов внутренних дел»» «Специальная техника органов внутренних дел» по специальности 40.05.03 Судебная экспертиза (специализация Криминалистические экспертизы)."
]
num_book = 3

template_path = "www"

book_root = paths[num_book]
book_name = get_folder_name(book_root)
save_root = "E:\htmls"
save_root = os.path.join(save_root, book_name)
save_root = os.path.join(save_root, "www")

if (os.path.exists(save_root) == True):
    shutil.rmtree(save_root)

if (os.path.exists(save_root) == False):
    shutil.copytree(template_path, save_root)



# if (os.path.exists(save_root) == False):
#     os.makedirs(save_root)
    



themes = os.listdir(book_root)
save_themes = []
book_themes = []
name_themes = []
for theme in themes:
    book_theme = os.path.join(book_root, theme)

    if os.path.isfile(book_theme):
        continue
        print("Файл:", book_theme)        
    
    if os.path.isdir(book_theme):
        save_theme = os.path.join(save_root, theme)
        
        book_themes.append(book_theme)  
        name_themes.append(theme)
        save_themes.append(save_theme)
        
        # print(save_theme)
        if (os.path.exists(save_theme) == False):
            os.makedirs(save_theme)
        
gen_root_index.generate_index(name_themes, save_root, book_names[num_book])


# print(book_themes)
for i in range(len(book_themes)):
    book_theme = book_themes[i]
    parts = os.listdir(book_theme)
    book_parts = []
    save_parts = []
    name_parts = []
    for part in parts:
        book_part = os.path.join(book_root, book_themes[i] ,part)
        # print(book_part)
        if os.path.isfile(book_part):
            continue
            print("Файл:", book_part)        
    
        if os.path.isdir(book_part):
            save_part = os.path.join(save_root, name_themes[i], part)
            book_parts.append(book_part)
            save_parts.append(save_part)
            name_parts.append(part)          
              
            if (os.path.exists(save_part) == False):
                os.makedirs(save_part) 
   
            
    # print(save_parts)     
   
    save_theme_root = os.path.join(save_root, name_themes[i]) 
    gen_theme_index.generate_index(name_parts, save_theme_root, name_themes[i])
    
 
                
for i in range(len(book_themes)):
    book_theme = book_themes[i]
    theme = get_folder_name(book_theme)
    parts = os.listdir(book_theme)
    book_parts = []
    save_parts = []
    name_parts = []
    for part in parts:
        book_part = os.path.join(book_theme ,part)
        if os.path.isfile(book_part):
            continue
            print("Файл:", book_part)        
    
        if os.path.isdir(book_part):
            save_part = os.path.join(save_root, theme, part)
            book_parts.append(book_part)
            save_parts.append(save_part)
            name_parts.append(save_part)          
            book_files = []
            save_files = []
            name_files = []
            files = os.listdir(book_part)
            for i in range(len(files)):
                file = files[i]
               
                # for file in files:                   
                if file.endswith(".html"):
                    book_file = os.path.join(book_part, file)
                    save_file = os.path.join(save_part, file)
                    
                    book_files.append(book_file)
                    save_files.append(save_file)
                    name_files.append(file)
                    gen_html_pdf.generate_index(save_path=save_file, book_path=book_file)                        

                    
                if file.endswith(".mp4"):
                    book_file = os.path.join(book_part, file)
                    save_file = os.path.join(save_part, file)
                    
                    book_files.append(book_file)
                    save_files.append(save_file)
                    name_files.append(file.replace(".mp4", ".html"))
                    shutil.copy(book_file, save_file)
                    gen_html_video.generate_index(save_file, title=file)
                    
                if file.endswith(".zip"):
        
                    book_file = os.path.join(book_part, file)
                    save_file = os.path.join(save_part, file)
                    
                    book_files.append(book_file)
                    save_files.append(save_file)
                    name_files.append(file)
                    shutil.copy(book_file, save_file)
                    gen_html_zip.generate_index(save_file.replace(".zip", ".html"), title=file.replace(".zip", ".html"))

                        
                
            if (i == len(files) - 1):
                gen_part_index.generate_index(name_files, save_part, part)

                