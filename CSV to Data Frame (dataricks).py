#nesse exemplo eu levo em consideração que você ja fez a config básica  
#seguindo esse exemplo: https://github.com/LucasBonfimPires/Azure/blob/main/Conectando%20em%20um%20container%20azure

#diretório onde os arquivos são armazenados
source =f"wasbs://{container}@{storage_name}.blob.core.windows.net/"

#nome completo do seu arquivo
nome_arquivo = "arquivoX.csv" #informe o nome completo do seu arquivo

#path do arquivo concatenando as 2 variaveis -> source container + dolar_csv para leitura com spark
path_csv_dolar = source + dolar_csv

#criando DataFrame com Spark
#data frame with spark: armazena o conteudo do .csv dentro de "spark_df"
spark_df = spark.read.format("csv").load(path_csv_dolar, inferSchema = True, header = True)
display(spark_df)
