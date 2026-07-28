# Corrija o programa a seguir:
# media = input('Digite sua média: ')
# if media < 4:
#   print('Infizmente você reprovou')
# if media < 7:
#   print('Você ficou de recuperação')
# if media > 7:
#   print('Você passou de ano')

media = int(input('Digite sua média: '))
if media < 4:
    print('Infelizmente você reprovou.')
elif media >= 4 and media <= 7:
    print('Você ficou de recuperação.')
else:
    print('Você passou de ano')