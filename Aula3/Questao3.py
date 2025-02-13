aluno = {'nome': input("Nome do aluno: "),
         'media': int(input("Média do aluno: ")),
         'situação': ''}  #dicionário

if aluno['media'] >= 50:
    print('AP')
    aluno['situação'] = 'AP'
else:
    print('RP')
    aluno['situação'] = 'RP'

print(aluno)