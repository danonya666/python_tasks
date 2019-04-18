import csv
import cars

csv_filename = '_af3947bf3a1ba3333b0c891e7a8536fc_coursera_week3_cars.csv'


def get_car_list(filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            car_type = ''
            try:
                car_type = row[0]
            except IndexError:
                print('row is passed')
                pass

            if car_type == 'car':
                vehicle = cars.Car(row[1], row[3], row[5], row[2])
            elif car_type == 'truck':
                vehicle = cars.Truck(row[1], row[3], row[5], row[4])
            elif car_type == 'spec_machine':
                vehicle = cars.SpecMachine(row[1], row[3], row[5], row[6])
                print(row[1])
            else:
                print(f'Unknown car type {car_type}; row is not added to database!')
                pass

            car_list.append(vehicle)

    return car_list


print(get_car_list(csv_filename))
