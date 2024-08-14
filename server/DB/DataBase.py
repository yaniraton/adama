import firebase_admin
from firebase_admin import db, credentials
from server import Constants
from server.DB.Plant import Plant


class DataBase:
    instance = None

    def __init__(self):
        cred = credentials.Certificate("credentials.json")
        firebase_admin.initialize_app(cred, {"databaseURL": Constants.FB_URL})

        self.ref = db.reference("/")

    def get_plant_column(self, plant_id):
        snapshot = self.ref.get()

        if snapshot is not None:
            for column in list(snapshot):
                for plant in column:
                    if plant is not None:
                        current_dict = dict(plant)

                        if current_dict["plant_id"] == plant_id:
                            return current_dict["column"]

        return -1

    def delete_plant(self, column, plant_id):
        self.ref.child(str(column)).child(str(plant_id)).set({})

    def save_plant(self, plant):
        plant_id = plant.get_id()
        old_column = self.get_plant_column(plant_id)

        # If plant already exists in different column
        if old_column != plant.get_column():
            self.delete_plant(old_column, plant_id)  # Deletes the old plant

        self.ref.child(str(plant.get_column())).child(str(plant.get_id())).set(plant.to_dict())

    def get_plant_data(self, column, plant_id):
        plant_dict = self.ref.child(str(column)).child(str(plant_id)).get()

        if plant_dict is None:
            return None
        else:
            return Plant(dict(plant_dict))
        
    def get_plant_data(self, plant_id):
        snapshot = self.ref.get()

        if snapshot is not None:
            for column in list(snapshot):
                for plant in column:
                    if plant is not None:
                        current_dict = dict(plant)

                        if current_dict["plant_id"] == plant_id:
                            return Plant(current_dict)

        return None

    def get_instance():
        if DataBase.instance is None:
            DataBase.instance = DataBase()

        return DataBase.instance
