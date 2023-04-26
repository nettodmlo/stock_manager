from PySimpleGUI import PySimpleGUI as sg
import sqlite3

#Layout
sg.theme("Reddit")
layout = [    [sg.Text("Qual item deve ser adicionado ao estoque?"), sg.Input()],
    [sg.Text("Digite o código de barras do item"), sg.Input()],
    [sg.Text("Diga-me a quantidade que deseja adicionar ao estoque"), sg.Input()],
    [sg.Button("Enviar")],
    [sg.Multiline("", size=(60, 10), key="-HISTORICO-")]
]

#Janela
janela = sg.Window("Stock Manager 1.0", layout)
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break
    if evento == "Enviar":
        nameItem = valores[0]
        barCode = valores[1]
        amountItem = valores[2]

        #DB
        conn = sqlite3.connect("stock.db")
        cur = conn.cursor()

        cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, code TEXT, amount INTEGER)")
        cur.execute("INSERT INTO items (name, code, amount) VALUES (?, ?, ?)",(nameItem.lower(), barCode, amountItem))
        conn.commit()
        conn.close()

        #Histórico de itens adicionados
        conn = sqlite3.connect("stock.db")
        cur = conn.cursor()
        consulta = "SELECT * FROM items ORDER BY ROWID DESC LIMIT 10"
        cur.execute(consulta)
        resultados = cur.fetchall()
        historico = ""
        for linha in resultados:
            historico += f"{linha[0]} - {linha[1]} - {linha[2]} - {linha[3]}\n"
        janela["-HISTORICO-"].update(historico)
        conn.close()

        total_stockItems = 0

        conn = sqlite3.connect("stock.db")
        cur = conn.cursor()
        consulta = "SELECT * FROM items"
        cur.execute(consulta)
        resultados = cur.fetchall()
        for linha in resultados:
            nome_item = linha[1]
            codigo_item = linha[2]
            quantidade_item = linha[3]
            if nome_item.lower() == nameItem.lower() and codigo_item == barCode:
                total_stockItems += quantidade_item
        conn.close()

        #DB
        print(f"O item {nameItem} foi adicionado! Ao total, há no estoque nesse momento {total_stockItems} itens dessa categoria!")
