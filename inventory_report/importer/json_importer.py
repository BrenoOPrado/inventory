from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if '.json' in path:
            with open(path) as file:
                data = json.load(file)
                return data
        else:
            raise ValueError("Arquivo inválido")
