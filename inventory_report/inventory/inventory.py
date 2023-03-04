import csv
import json
import xml.etree.ElementTree as et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(cls, path, type):
        if '.csv' in path:
            res = cls.import_data_csv(path, type)
        elif '.json' in path:
            res = cls.import_data_json(path, type)
        elif '.xml' in path:
            res = cls.import_data_xml(path, type)
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

    @classmethod
    def import_data_xml(cls, path, type):
        xml_data = et.parse(path).getroot()
        data = [{item.tag: item.text for item in elem}
                for elem in xml_data]
        # Encontrei a solução na internet e acho que entendi
        # xml_data == [[{...}, ...], ...]
        # elem = [{...}, ...]
        # item = {tag: *algo*, text: *algo*, ...}
        # data = [{tag: texto}, ...]
        return cls.generate_report(data, type)

    @staticmethod
    def generate_report(data, type):
        if type == "simples":
            res = SimpleReport.generate(data)
        elif type == "completo":
            res = CompleteReport.generate(data)
        return res
