import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту add с параметром json
    zipcode = int(input('Введите zipcode: '))
    sqft = float(input('Введите sqft: '))
    mean_school_rating = float(input('Введите средний ретинг школы: '))
    year_built = int(input('Введите год постройки: '))
    propertyType_condo = (input('Введите тип объекта: '))
    mean_distance_to_school = float(input('Введите среднее расстояние до школы: '))
    lotsize = float(input('Введите площадь участка: '))
    stories = float(input('Введите этажность дома: '))
    schools_count = float(input('Введите количество школ возле дома: '))
    remodeling_yes = input('была ли реконструкция дома?: ')

    r = requests.post('http://localhost:5000/predict', json=[zipcode, sqft, mean_school_rating, year_built, propertyType_condo,
                                                             mean_distance_to_school, lotsize, stories, schools_count, remodeling_yes])
    # выводим статус запроса
    print('Status code: {}'.format(r.status_code))
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print('Prediction: {}'.format(r.json()['prediction']))
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)