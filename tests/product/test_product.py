from inventory_report.inventory.product import Product


def test_cria_produto():
    data = {
        "id": 3,
        "nome_do_produto": "sorvete",
        "nome_da_empresa": "trybe",
        "data_de_fabricacao": "2023-02-06",
        "data_de_validade": "2023-03-22",
        "numero_de_serie": "EX52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "guardar em lugar gelado"
    }
    result = Product.__repr__(data.items)
    expect = (
        f"O produto {data['nome_do_produto']}"
        f" fabricado em {data['data_de_fabricacao']}"
        f" por {data['nome_da_empresa']} com validade"
        f" até {data['data_de_validade']}"
        f" precisa ser armazenado {data['instrucoes_de_armazenamento']}."
    )
    assert expect in result
    # pass  # Seu teste deve ser escrito aqui
