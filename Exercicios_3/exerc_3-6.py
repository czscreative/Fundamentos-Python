# Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores ou iguais a 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada nas seguintes variáveis: materia1, materia2, materia3
materia1 = 7
materia2 = 8
materia3 = 10
aprovacao = 7

media = (materia1 + materia2 + materia3)/3

print(f"Aprovado = {media >= aprovacao} - Média Total = {media:5.2f}")