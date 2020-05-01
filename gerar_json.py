import json


class JSON:

    @staticmethod
    def gerar_json(nome, idade, altura):
        try:
            dados = dict(nome = nome, idade = idade, altura = altura)
            dados_salvar = {"dados": dados}
            dados_salvar = json.dumps(dados_salvar, indent = 4, sort_keys = False)
            arquivo = open('json.json', 'w')
            arquivo.write(dados_salvar)

            return print("O Arquivo foi gerado com sucesso.")
            
        except():
            print("Erro ao tentar gerar o arquivo JSON.")
        finally:
            if arquivo.closed is False:
                arquivo.close()
        
    def ler_file_json(self, nome_arquivo):
           try:
               json_file = open(nome_arquivo+'.json', 'r')
               linhas = json.load(json_file)
               dict_dados = linhas
               for chave_principal in dict_dados.keys():
                  nome_json  = dict_dados[chave_principal]['nome']
                  idade_json = dict_dados[chave_principal]['idade']
                  altura_json = dict_dados[chave_principal]['altura']

                  self.insert_pessoa(nome_json, idade_json, altura_json)
                     
           except():
                print("Erro ao tentar ler o arquivo json.")
           finally:
                  json_file.close()

    def insert_pessoa(self,nome, altura, idade):
         try:
             sql = "insert into pessoa(nome, idade, altura) values('{0}',{1}, {2});".format(nome, idade, altura)
             print(sql)
         except():
             print("Erro ao tentar inserir na tabela pessoa.")



nome = "teste"
idade = 22
altura = 1.87
nome_arquivo = "json"

test_json = JSON()
test_json.gerar_json(nome, idade, altura)
test_json.ler_file_json(nome_arquivo) 
