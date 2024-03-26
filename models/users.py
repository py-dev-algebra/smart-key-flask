


class User:
    def __init__(self, first_name: str, last_name: str, pin_code: str, is_active: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.pin_code = pin_code
        self.is_active = is_active

    def __str__(self):
        if self.is_active:
            is_active = 'Aktivan'
        else:
            is_active = 'Deaktiviran'
        return f'{self.first_name};{self.last_name};{self.pin_code};{is_active}'