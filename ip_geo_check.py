import requests
import time

# Открываем файл с IP-адресами
with open(r'C:\Users\whoami\Documents\ip_adresses.txt', 'r') as f:
    # Читаем все строки из файла и убираем символы переноса строк
    ip_addresses = [line.strip() for line in f]

# Открываем файл для записи результатов
with open(r'C:\Users\whoami\Documents\result.txt', 'w') as result_file:
    # Открываем файл для записи ошибок
    with open(r'C:\Users\whoami\Documents\errors.txt', 'w') as error_file:
        # Проходим по каждому IP-адресу в списке
        for ip_address in ip_addresses:
            try:
                # Отправляем GET-запрос на сервис ipinfo.io, передавая IP-адрес в качестве параметра
                response = requests.get(f'https://ipinfo.io/{ip_address}?token=<ENTER_YOUR_TOKEN>')
                
                # Получаем данные о местоположении IP-адреса в формате JSON
                data = response.json()

                # Проверяем, относится ли IP-адрес к RU
                if data["country"] == "RU":
                    # Собираем строку с информацией об IP-адресе
                    result_str = f'{data["ip"]}; {data["city"]}; {data["country"]}; {data["org"]}'
                    # Записываем строку в файл
                    result_file.write(result_str + '\n')
                    
                    # Печатаем строку на экран
                    print(result_str)
                else:
                    print(f'{data["ip"]}; {data["city"]}; {data["country"]}; {data["org"]}')

            except Exception as e:
                error_str = f'{ip_address}: {str(e)}'
                print(error_str)
                
                # Записываем ошибку в файл
                error_file.write(error_str + '\n')

# Закрываем файлы для записи результатов и ошибок
result_file.close()
error_file.close()
