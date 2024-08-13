class Plant:
    
    def __init__(self, id: int, is_tomato: bool, humidities: dict, capture_url: str, column: int) -> None:
        self.id = id
        self.is_tomato = is_tomato
        self.humidities = humidities
        self.capture_url = capture_url
        self.column = column


    def __init__(self):
        self.id = -1
        self.is_tomato = True
        self.humidities = {}
        self.capture = ""
        self.column = -1


    def get_id(self):
        return self.id
    

    def get_is_tomato(self):
        return self.is_tomato
    

    def get_humidities(self):
        return self.humidities
    

    def get_capture_url(self):
        return self.capture_url
    

    def get_column(self):
        return self.column
    

    def set_id(self, id: int):
        self.id = id
    

    def set_is_tomato(self, is_tomato: bool):
        self.is_tomato = is_tomato
    

    def set_humidities(self, humidities: dict):
        self.humidities = humidities
    

    def set_capture_url(self, capture_url: str):
        self.capture_url = capture_url
    

    def set_column(self, column: int):
        self.column = column
