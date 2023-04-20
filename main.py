import sqlite3

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

conn = sqlite3.connect("estoque.db")
cur = conn.cursor()

# Criar tabela "items" caso não exista
cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, code TEXT, amount INTEGER)")

# Inserir dados na tabela "items"
cur.execute("INSERT INTO items (name, code, amount) VALUES (?, ?, ?)",(stock_item.name, stock_item.code, stock_item.amount))
conn.commit()
conn.close()

conn = sqlite3.connect("estoque.db")
cur = conn.cursor()
consulta = "SELECT * FROM items ORDER BY ROWID DESC LIMIT 10"
cur.execute(consulta)
resultados = cur.fetchall()
for linha in resultados:
    print(linha)
conn.close()

total_stockItems = 0

conn = sqlite3.connect("estoque.db")
cur = conn.cursor()
consulta = "SELECT * FROM items"
cur.execute(consulta)
resultados = cur.fetchall()
for linha in resultados:
    nome_item = linha[1]
    codigo_item = linha[2]
    quantidade_item = linha[3]
    if nome_item == nameItem and codigo_item == barCode:
        total_stockItems += quantidade_item
conn.close()
print(f"O item {nameItem} foi adicionado! Ao total, há no estoque nesse momento {total_stockItems} itens dessa categoria!")
