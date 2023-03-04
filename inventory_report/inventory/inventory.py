import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path, type):
        with open(path) as file:
            csv_file = csv.DictReader(file)
            data = []
            for item in csv_file:
                data.append(item)
            if type == "simples":
                res = SimpleReport.generate(data)
            elif type == "completo":
                res = CompleteReport.generate(data)
            return res
