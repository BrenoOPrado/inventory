from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if '.csv' in path:
            with open(path) as file:
                csv_file = csv.DictReader(file)
                data = []
                for item in csv_file:
                    data.append(item)
                return data
        else:
            raise ValueError("Arquivo inválido")
