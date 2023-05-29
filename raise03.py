class ErroDeConexao(Exception):
    def __init__(self, servidor):
        self.servidor = servidor
    
    def __str__(self):
        return f"Erro de conexão com o servidor: {self.servidor}"
    
    @staticmethod
    def conectar(servidor):
        if servidor != "servidor_correto":
            raise ErroDeConexao(servidor)
        else:
            print("Conectado ao servidor.")
        
try:
    ErroDeConexao.conectar("servidor_errado")
except ErroDeConexao as erro:
    print(erro)
