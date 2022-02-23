
#conexão com container e storage account
storage_name = "nome_do_storage" #o storage geralmente é o nome do recurso do azure
storage_key = "chave_de_acesso" #basta ir em: Chaves de acesso -> mostrar chaves de acesso
container = "nome_do_conteiner" #nome do container onde você deseja trabalhar


#diretório onde os arquivos são armazenados
source =f"wasbs://{container}@{storage_name}.blob.core.windows.net/"


#configuração de acesso global utilizando spark
spark.conf.set(
    f"fs.azure.account.key.{storage_name}.blob.core.windows.net", storage_key
)

