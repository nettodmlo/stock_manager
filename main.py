nameItem = str(input("Qual item deve ser adicionado ao estoque? "))
barCode = str(input("Digite o código de barras do item: "))
amountItem = int(input("Digite a quantidade que deseja adicionar ao estoque: "))
directory = r'C:\Users\TREMINAL\Desktop\Netto\stock_project'

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

with open("database.txt", "r") as f:
    linhas = f.readlines()

total_stockItems = 0
for linha in linhas:
    dados = linha.strip().split(", ")
    nome_item = dados[0]
    codigo_item = dados[1]
    quantidade_item = int(dados[2])
    if nome_item == nameItem and codigo_item == barCode:
        total_stockItems += quantidade_item

print(f"O item {nameItem} foi adicionado! Ao total, há no estoque nesse momento {total_stockItems} itens dessa categoria!")
