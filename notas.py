'Faça um algoritmo que verifique a aprovação de alunos com base em suas notas e presenças. O algoritmo deve receber três notas (AP1, AP2 e AS) e o número de presenças de um aluno (valor entre 1 e 24). A partir desses dados, o algoritmo deve calcular a nota final (PS) do aluno (soma das três notas) e verificar se o número de faltas é inferior ou igual a 5. O aluno poderá ser aprovado, realizar a Avaliação Final (AF) ou ser reprovado, conforme as regras a seguir.'

'Regras:'

'Se a nota final (PS) for igual ou superior a 6 e o número de faltas for igual ou inferior a 5, o aluno está aprovado.'
'Se a nota final (PS) for inferior a 6, mas o número de faltas for igual ou inferior a 5, o aluno deverá fazer a Avaliação Final (AF).'
'Se o número de faltas for superior a 5, o aluno estará reprovado, independentemente da nota.'
'O algoritmo deve ser capaz de receber e testar as notas de diversos alunos usando a estrutura WHILE. Após cada verificação, o algoritmo deve voltar para o menu inicial.'

'Menu de entrada:'

'1- VERIFICAR APROVAÇÃO'

'0- SAIR'

while True:
    print('------------------------------------')
    nome = input('Qual o nome do aluno? ')
    ap1 = float(input('Qual foi a nota de AP1? '))
    ap2 = float(input('Qual foi a nota de AP2? '))
    semestral = float(input('Qual foi a nota de AS? '))
    faltas = int(input('Qual foi o número de faltas do aluno? '))
    print('------------------------------------')
    
   
    
    soma = ap1 + ap2 + semestral
    sair = int(input('Digite 1 para verificar a nota ou 0 para sair:'))
    
    if sair == 0:
        break
    elif sair == 1:
        if soma >=6 and faltas <=5:
            print(f"Parabéns, {nome}, você foi aprovado!")
        elif soma <6 and faltas <=5:
            print(f"{nome}, você deverá fazer a Avaliação Final.")
        elif faltas >5:
            print(f"Infelizmente, {nome}, você rodou por faltas...")
        else:
         continue