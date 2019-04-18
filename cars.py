class BaseCar:
    def __init__(self, photo_file_name, brand, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        split = self.photo_file_name.split('.')
        return split[1]

    def __repr__(self):
        return str(str(self.__class__.__qualname__) + ' ' + self.brand)


class Car(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(photo_file_name, brand, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(photo_file_name, brand, carrying)
        split = body_whl.split('x')
        try:
            self.width = float(split[0])
            self.height = float(split[1])
            self.length = float(split[2])
        except ValueError:
            self.width, self.height, self.width = None, None, None

    def get_body_volume(self):
        return self.width * self.height * self.length


class SpecMachine(BaseCar):
    def __init__(self, brand, photo_file_name, carrying, extra=None):
        super().__init__(photo_file_name, brand, carrying)
        self.extra = extra or 'Описание отсутствует'



