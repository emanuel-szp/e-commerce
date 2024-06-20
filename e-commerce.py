import mysql.connector

class Produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco 


class SistemaDeEcommerce:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="e_commerce"
        )
        self.cursor = self.conexao.cursor()

    def adicionar_produto(self,produto):
        sql = "INSERT INTO produto (nome,preco) VALUES (%s, %s)"
        valores = (produto.nome, produto.preco)
        self.cursor.execute(sql,valores)
        self.conexao.commit()
        print('produto adicionado.')
    
    def listar_produto(self):
        self.cursor.execute("SELECT nome,preco FROM produto") 
        produto = self.cursor.fetchall()
        for produto in produto:
            print(f"nome:{produto[0]}, preco: {produto[1]}")


    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
       

sistema=SistemaDeEcommerce()

nome = input('nome do produto:')
preco = input('preco do produto: R$')
estoque = Produto(nome,preco)
sistema.adicionar_produto(estoque)



print('produtos:')
sistema.listar_produto()

sistema.fechar_conexao()

