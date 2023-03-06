from inventory_report.inventory.product import Product


def test_cria_produto():
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
    assert data["nome_do_produto"] in result
    assert data["data_de_fabricacao"] in result
    assert data["nome_da_empresa"] in result
    assert data["data_de_validade"] in result
    assert data["instrucoes_de_armazenamento"] in result
    # pass  # Seu teste deve ser escrito aqui
