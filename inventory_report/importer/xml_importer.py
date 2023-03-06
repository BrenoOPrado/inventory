from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as et


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if '.xml' in path:
            xml_data = et.parse(path).getroot()
            data = [{item.tag: item.text for item in elem}
                    for elem in xml_data]
            return data
        else:
            raise ValueError("Arquivo inválido")
