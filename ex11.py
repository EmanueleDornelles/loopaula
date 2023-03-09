usuario_palavra = input('Entre com uma palavra: ')
usuario_palavra = usuario_palavra.upper()
palavra_sem_vogais=''
for letra in usuario_palavra:
    if letra == 'A':
        continue
    elif letra == 'E':
        continue
    elif letra == 'I':
        continue
    elif letra == 'O':
        continue
    elif letra == 'U':
        continue
    else:
        palavra_sem_vogais += letra
        
print(palavra_sem_vogais)