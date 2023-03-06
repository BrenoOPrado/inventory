from datetime import datetime


class SimpleReport:
    @staticmethod
    def filter_informations(data):
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

        return dict({
            "manufacturing_date": min(manufacturing_date),
            "expiration_date": min(expiration_date),
            "products_by_company": max(
                products_by_company,
                key=products_by_company.get
            ),
        })

    @classmethod
    def generate(cls, data):
        filtered_data = cls.filter_informations(data)
        return (
            "Data de fabricação mais antiga: "
            f"{filtered_data['manufacturing_date']}\n"
            "Data de validade mais próxima: "
            f"{filtered_data['expiration_date']}\n"
            "Empresa com mais produtos: "
            f"{filtered_data['products_by_company']}"
        )
