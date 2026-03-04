'''
4. O Crachá do Funcionário (Multiplicação de Strings e Limpeza) 
Faça um programa que leia o nome de um funcionário e seu cargo para gerar um crachá digital. Como os usuários às vezes digitam espaços sem querer no início ou fim, use o método .strip() para limpar a entrada. Para criar as bordas superior e inferior do crachá, utilize o operador de multiplicação de strings (ex: "-" * 30).

Exemplo de Entrada: 
Nome: Harry 
Cargo: Caixa 

Exemplo de Saída:
------------------------------ 
CRACHÁ DE IDENTIFICAÇÃO 
Nome: Harry 
Cargo: Caixa 
------------------------------
'''

nome = ' Harry '
cargo = 'caixa'

print('-' * 30)
print('Nome:', nome.strip().capitalize)
print('Cargo:', cargo.strip().capitalize)
print('-' * 30)
