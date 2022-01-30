#import da biblioteca com apelido
import pandas as pd

#leitura do arquivo
dados_sao_luis = pd.read_excel(r'C:\Users\rudij_cx4b0ag\Documents\PROJETOS\PROGRAMAÇÃO\PYTHON\ARTIGO\DADOS\EXEMPLO\SAO_LUIS.xlsx')
#informado qual o separador para decimais
#Separator(sep='.')
print(dados_sao_luis)