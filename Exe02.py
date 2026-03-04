'''
2. A Padaria (Casas Decimais e Operadores Aritméticos) 
Elabore um programa para ajudar no caixa de uma padaria. O programa deve solicitar o nome do cliente, o nome do doce comprado, a quantidade e o preço unitário. Calcule o valor total a pagar e exiba um mini-recibo. Os valores monetários devem obrigatoriamente aparecer com duas casas decimais e o nome do cliente deve ser exibido com a primeira letra maiúscula (usando o método .title() ou .capitalize()). 

Exemplo de Entrada: 
Cliente: jonin 
Doce: Croissant 
Quantidade: 3 
Preço Unitário: 5.5 

Exemplo de Saída:
--------- RECIBO --------- 
Cliente: Jonin 
Item: Croissant x3 
Total a pagar: R$ 16.50 
--------------------------
'''

cliente = input('Informe o nome:')
doce = input('Qual o pedido:')
quantidade = int(input('Quantos :'))
preço = float(input('Preço unitario:'))

print('-' * 9,'Recibo','-'*9)
print('Nome:',cliente)
print('item:',doce, 'x'+str(quantidade))
print('Total a se pagar: R$', preço * quantidade)
print('-' * 26)
      
