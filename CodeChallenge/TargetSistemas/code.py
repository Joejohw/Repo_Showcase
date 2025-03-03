
# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA */


indice = 13      # Definição do índice
soma = 0         # Definição da soma
k = 0            # Definição do contador

while k < indice: # Loop para somar os valores de 1 a 13
    
    k =k + 1        # Incremento do contador
    soma = soma + k # Soma dos valores
    
print("Resultado Exercicio 1") # Exibição do título
print("Valor final de SOMA:", soma)  # Exibição da soma, Resultado esperado: 91





# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def pertence_fibonacci(num): # Função para verificar se o número pertence à sequência de Fibonacci
    a, b = 0, 1 # Definição dos valores iniciais
    while b < num: # Loop para calcular a sequência de Fibonacci
        a, b = b, a + b # Cálculo dos valores da sequência
    return b == num or num == 0 # Verifica se o número pertence à sequência


print("Resultado Exercicio 2") # Exibição do título

num = int(input("Digite um número: "))                                  # Entrada do número
if pertence_fibonacci(num):                                             # Verifica se o número pertence à sequência de Fibonacci
    print(f"O número {num} pertence à sequência de Fibonacci.")         # Exibe a mensagem
else:                                                                   # Caso contrário
    print(f"O número {num} não pertence à sequência de Fibonacci.")     # Exibe a mensagem






# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json # Importação da biblioteca json

arquivo_json = "\\CodeChallenge\\TargetSistemas\\dados.json" # Caminho do arquivo json, ## caso necessário direcione o caminho ##

def analisa_faturamento(arquivo): # Função para analisar o faturamento
    with open(arquivo, 'r') as file: # Abre o arquivo
        dados = json.load(file) # Carrega o arquivo json

    faturamento_dia = [dia["valor"] for dia in dados if dia["valor"]>0] # Lista com os valores de faturamento diário, Ignorar dias sem faturamento

    if not faturamento_dia:
        return "Não houve faturamento"
    
    menor_faturamento = min(faturamento_dia) # Menor valor de faturamento
    maior_faturamento = max(faturamento_dia) # Maior valor de faturamento
    media_mensal = sum(faturamento_dia) / len(faturamento_dia) # Média de faturamento diário
    dias_acima_media = sum(1 for faturamento in faturamento_dia if faturamento > media_mensal) # Dias em que o faturamento foi superior à média

    return{
        "Menor faturamento": menor_faturamento,
        "Maior faturamento": maior_faturamento,
        "Dias acima da média": dias_acima_media
    }

# Exemplo de uso
resultado = analisa_faturamento(arquivo_json) # Análise do faturamento

print("Exercicio 3") # Exibição do título
print("Resultado da análise de faturamento:", resultado) # Exibição do resultado da análise de faturamento


# 4)4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
#• SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  


#Dados Faturamento
Faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
#Calculo do percentual somatório total de faturamento, e percentual de representação de cada estado
total = sum(Faturamento.values()) # Soma de todos os valores
percentuais = {estado: (faturamento / total) * 100 for estado, faturamento in Faturamento.items()} # Calculo do percentual de representação de cada estado

print("Resultado Exercicio 4") # Exibição do título
print("Percentual de representação de cada estado:")
for estado, percentual in percentuais.items(): 
    print(f"{estado}: {percentual:.2f}%")# Exibição dos percentuais





# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_texto(texto): # Função para inverter o texto
  invertido = ""                                   # Variável para armazenar o texto invertido
  for letra in texto:                              # Loop para percorrer cada letra do texto
    invertido = letra + invertido                  # Inverte a ordem das letras
  return invertido                                 # Retorna o texto invertido

entrada = input("Digite um texto para inverter: ") # Entrada do texto

print("Resultado Exercicio 5") # Exibição do título
print("Texto invertido:", inverter_texto(entrada)) # Exibição do texto invertido

## Aguarde para avaliação do teste prático. Obrigado! ##

import time # Importação da biblioteca time
time.sleep(120) # Aguarda 10 segundos para finalizar o programa
