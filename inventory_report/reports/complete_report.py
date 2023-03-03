from simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def __init__(self):
        pass

    @staticmethod
    def generate(data):
        simple_message = super().generate(data)
        new_part = "\nProdutos estocados por empresa: \n"
        products_by_company = (
            super().filter_informations(data)
        )['products_by_company']
        for chave, valor in products_by_company:
            new_part += (
                f" - {chave}: {valor}\n"
            )
        res = simple_message + new_part
        return res
