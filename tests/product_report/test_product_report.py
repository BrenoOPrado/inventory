from inventory_report.inventory.product import Product


def test_relatorio_produto():
    data = dict({
        "id": 3,
        "nome_do_produto": "barra de chocolate",
        "nome_da_empresa": "Nestle",
        "data_de_fabricacao": "2023-02-06",
        "data_de_validade": "2023-03-22",
        "numero_de_serie": "EX11 244 789 735",
        "instrucoes_de_armazenamento": "em lugar refrigerado"
    })
    result = str(Product(
        data["id"],
        data["nome_do_produto"],
        data["nome_da_empresa"],
        data["data_de_fabricacao"],
        data["data_de_validade"],
        data["numero_de_serie"],
        data["instrucoes_de_armazenamento"],
    ))
    expect = (
        f"O produto {data['nome_do_produto']}"
        f" fabricado em {data['data_de_fabricacao']}"
        f" por {data['nome_da_empresa']} com validade"
        f" até {data['data_de_validade']}"
        f" precisa ser armazenado {data['instrucoes_de_armazenamento']}."
    )
    assert expect == result
    # pass  # Seu teste deve ser escrito aqui
