def conver_hora(hora, minutos):
    periodo = "A.M", "P.M"
    if hora < 12:
        return(f'{hora}:{minutos} {periodo[0]}')
    elif hora > 12 and hora < 24:
        return (f'{hora - 12}:{minutos} {periodo[1]}')
    elif hora == 24:
        return (f'{hora - 24}:{minutos} {periodo[0]}')
    elif hora >= 12 and hora < 24:
        return (f'{hora}:{minutos} {periodo[1]}')

while True:
    hora = int(input('Informe a hora: '))
    if hora > 24 or hora < 0:
        print("\nDigite um horario entre 24 e 0 horas\n")
        continue
    minutos = int(input('Informe os minutos: '))
    if minutos > 59 or minutos < 0:
        print("\nDigite minutos entre 0 e 59\n")
        continue
    print(conver_hora(hora,minutos))
    controle = input('Digite uma letra se deseja sair ou um número se deseja continuar: ')
    if controle.isnumeric():
        continue
    else:
        break