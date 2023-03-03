from datetime import datetime


class SimpleReport:
    def __init__(self):
        pass

    @staticmethod
    def generate(data):
        manufacturing_date = []
        expiration_date = []
        products_by_company = {}
        now_time = datetime.now().strftime("%Y-%m-%d")
        for product in data:
            manufacturing_date.append(product["data_de_fabricacao"])
            if product["data_de_validade"] >= now_time:
                expiration_date.append(product["data_de_validade"])
            if product["nome_da_empresa"] in products_by_company:
                products_by_company[product["nome_da_empresa"]] += 1
            else:
                products_by_company[product["nome_da_empresa"]] = 1
        return (
            "Data de fabricação mais antiga: "
            f"{min(manufacturing_date)}\n"
            "Data de validade mais próxima: "
            f"{min(expiration_date)}\n"
            "Empresa com mais produtos: "
            f"{max(products_by_company, key= products_by_company.get)}"
        )
