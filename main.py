nameItem = (input("Qual item deve ser adicionado ao estoque? "))
barCode = (input("Digite o código de barras do item: "))
amountItem = (input("Digite a quantidade que deseja adicionar ao estoque: "))

class Stock:
    def __init__(self, name, code, amount):
        self.name = name
        self.code = code
        self.amount = amount

    def processing(self):
        print("Processando o armazenamento dos itens...")

stock_item = Stock(nameItem, barCode, amountItem)
stock_item.processing()

with open("database.txt", "a") as arquivo:
    arquivo.write(f"{stock_item.name}, {stock_item.code}, {stock_item.amount}\n")
with open("database.txt", "r") as arquivo:
    conteudo = arquivo.read()
