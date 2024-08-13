class Plant:

    def __init__(self, plant_id: int, is_tomato: bool, humidities: dict, capture_url: str, column: int) -> None:
        self.plant_id = plant_id
        self.is_tomato = is_tomato
        self.humidities = humidities
        self.capture_url = capture_url
        self.column = column

    def __init__(self) -> None:
        self.plant_id = -1
        self.is_tomato = True
        self.humidities = {}
        self.capture_url = ""
        self.column = -1

    def __init__(self, data_dict: dict):
        self.plant_id = data_dict["id"]
        self.is_tomato = data_dict["is_tomato"]
        self.capture_url = data_dict["capture_url"]
        self.column = data_dict["column"]

        if "humidities" in data_dict.keys():
            self.humidities = data_dict["humidities"]

    def get_id(self):
        return self.plant_id

    def get_is_tomato(self):
        return self.is_tomato

    def get_humidities(self):
        return self.humidities

    def get_capture_url(self):
        return self.capture_url

    def get_column(self):
        return self.column

    def set_id(self, plant_id: int):
        self.plant_id = plant_id

    def set_is_tomato(self, is_tomato: bool):
        self.is_tomato = is_tomato

    def set_humidities(self, humidities: dict):
        self.humidities = humidities

    def set_capture_url(self, capture_url: str):
        self.capture_url = capture_url

    def set_column(self, column: int):
        self.column = column

    def to_dict(self):
        return {
            'plant_id': self.plant_id,
            'is_tomato': self.is_tomato,
            'humidities': self.humidities,
            'capture_url': self.capture_url,
            'column': self.column,
        }
