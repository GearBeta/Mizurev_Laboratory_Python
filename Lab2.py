disk_value = 1.44 #MB объем дискеты в мегабайтах
number_of_pages = 100 #Количество страниц в книге
strings_in_page = 50 #Число строк на странице
symbols_in_string = 25 #Число символов в строке
bytes_per_symbol = 4 #число байтов для хранения одного символа

volume_of_one_book = bytes_per_symbol * symbols_in_string * strings_in_page * number_of_pages
disk_value_in_bytes = disk_value * 1024 * 1024
number_of_books = disk_value_in_bytes // volume_of_one_book

print("Количество книг, помещающихся на дискету:", int(number_of_books))
