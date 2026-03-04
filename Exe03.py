'''

3. Ingresso VIP de Heavy Metal (Centralização de Strings) 
Desenvolva um programa que leia o nome de uma banda e a cidade do show. O programa deve gerar o layout de um ingresso na tela. O nome da banda deve ser transformado para letras maiúsculas (.upper()) e exibido centralizado em uma linha de 40 caracteres, preenchida com o símbolo de igual (=). 

Exemplo de Entrada: 
Banda: Iron Maiden 
Cidade: São Paulo 

Exemplo de Saída:
==============IRON MAIDEN=============== 
Local: São Paulo
Ticket: VIP - Acesso Liberado
========================================
'''

banda = input('Fale a banda:')
cidade = input('rio de janeiro')

print('='*20 + banda.upper() +'='*20)
print('Local', cidade.title())
print('Ticket: Vip - Acesso Liberado')
print('='*40 + '=' * len(banda))