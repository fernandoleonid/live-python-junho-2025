# Dicionário

produtos = [
    {
        "codigo": "12",
        "nome": "teclado",
        "descricao": "Teclado logitec ABNT2 usb",
        "preco": 45.99
    },
    {
        "codigo": "23",
        "nome": "mouse",
        "descricao": "mouse logitec ABNT2 usb",
        "preco": 145.99
    }
]

for produto in produtos:
    valor = produto['preco'] - 10
    print (f"{produto['nome']} - {valor}")