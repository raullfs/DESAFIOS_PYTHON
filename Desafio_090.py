aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] < 5:
    aluno['Situação'] = 'Reprovado'
elif aluno['Média'] >= 5 and aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Média'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')