from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    class_report = ColoredReport(SimpleReport)
    products_list = [
        {
            "id": 1,
            "nome_do_produto": "CADEIRA",
            "nome_da_empresa": "Forces of Nature",
            "data_de_fabricacao": "2022-04-04",
            "data_de_validade": "2024-02-09",
            "numero_de_serie": "FR48",
            "instrucoes_de_armazenamento": "Conservar em local fresco"
        }
    ]
    report = class_report.generate(products_list)

    assert "\033[32mData de fabricação mais antiga:\033[0m" in report
    assert "\033[32mData de validade mais próxima:\033[0m" in report
    assert "\033[32mEmpresa com mais produtos:\033[0m" in report

    assert f"\033[36m{products_list[0]['data_de_fabricacao']}\033[0m" in report
    assert f"\033[36m{products_list[0]['data_de_validade']}\033[0m" in report

    assert f"\033[31m{products_list[0]['nome_da_empresa']}\033[0m" in report
