from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, data):
        simple_message = super().generate(data)
        new_part = ""
        products_by_company = (
            super().filter_informations(data)
        )['products_by_company']
        for key in sorted(products_by_company,
                          key=products_by_company.get,
                          reverse=True,
                          ):
            new_part += f"- {key}: {products_by_company[key]}\n"
        res = (
            f"{simple_message}\n"
            f"Produtos estocados por empresa:\n"
            f"{new_part}"
        )
        print(res)
        return res
