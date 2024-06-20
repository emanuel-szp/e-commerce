import mysql.connector #Essa linha importa o módulo mysql.connector, que permite a conexão com o banco de dados MySQL.

class Produto: #Essas linhas definem a classe Produto, que possui um construtor __init__ que recebe os parâmetros nome e preco e os atribui aos atributos self.nome e self.preco, respectivamente.
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco 


class SistemaDeEcommerce: #Essas linhas definem a classe Produto, que possui um construtor __init__ que recebe os parâmetros nome e preco e os atribui aos atributos self.nome e self.preco, respectivamente.
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="he182555@",
            database="e_commerce"
        )
        self.cursor = self.conexao.cursor()
## Essas linhas definem o método adicionar_produto, que recebe um objeto produto como parâmetro. O método executa
        # uma instrução SQL para inserir os valores do produto na tabela "produto" do banco de dados. Em seguida, ele realiza o commit da transação para 
        # confirmar a inserção no banco de dados e exibe uma mensagem indicando que o produto foi adicionado com sucesso.
    def adicionar_produto(self,produto):
        sql = "INSERT INTO produto (nome,preco) VALUES (%s, %s)"
        valores = (produto.nome, produto.preco)
        self.cursor.execute(sql,valores)
        self.conexao.commit()
        print('produto adicionado.')
#Essas linhas definem o método listar_produto, 
# que executa uma consulta SQL para selecionar os campos "nome" e "preco" da tabela "produto". 
# Em seguida, ele recupera todas as linhas de resultado usando o método fetchall() e, para cada produto, imprime o nome e o preço.   
    def listar_produto(self): #
        self.cursor.execute("SELECT nome,preco FROM produto") 
        produto = self.cursor.fetchall()
        for produto in produto:
            print(f"nome:{produto[0]}, preco: {produto[1]}")
#Essas linhas definem o método fechar_conexao, que fecha o objeto cursor e a conexão com o banco de dados.

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()
       
#Essas linhas criam uma instância da classe SistemaDeEcommerce, solicitam ao usuário o nome e o preço de um produto,
# criam um objeto estoque da classe Produto com os valores informados e chamam o método adicionar_produto do sistema para adicionar o produto ao banco de dados.
#  Em seguida, ele lista todos os produtos chamando o método listar_produto e, por fim, 
sistema=SistemaDeEcommerce()

nome = input('nome do produto:')
preco = input('preco do produto: R$')
estoque = Produto(nome,preco)
sistema.adicionar_produto(estoque)


# fecha a conexão com o banco de dados chamando o método fechar_conexao.
print('produtos:')
sistema.listar_produto()

sistema.fechar_conexao()

