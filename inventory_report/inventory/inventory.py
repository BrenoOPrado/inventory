import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if '.csv' in path:
            res = cls.import_data_csv(path, type)
        elif '.json' in path:
            res = cls.import_data_json(path, type)
        return res

    @classmethod
    def import_data_csv(cls, path, type):
        with open(path) as file:
            csv_file = csv.DictReader(file)
            data = []
            for item in csv_file:
                data.append(item)
            return cls.generate_report(data, type)

    @classmethod
    def import_data_json(cls, path, type):
        with open(path) as file:
            data = json.load(file)
            return cls.generate_report(data, type)

    @staticmethod
    def generate_report(data, type):
        if type == "simples":
            res = SimpleReport.generate(data)
        elif type == "completo":
            res = CompleteReport.generate(data)
        return res
