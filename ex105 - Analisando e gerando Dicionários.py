def notas(*nota, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param nota: Uma ou mais notas dos alunos (aceita várias)
    :param sit: (opcional) situação da média de notas
    :return: Dicionário com várias informações sobre a situação da turma
    """
    n = dict()
    n['total'] = len(nota)
    n['maior'] = max(nota)
    n['menor'] = min(nota)
    n['média'] = sum(nota) / len(nota)
    if sit:
        if n['média'] >= 7:
            n['situação'] = 'BOA'
        elif n['média'] >= 5:
            n['situação'] = 'RAZOAVEL'
        else:
            n['situação'] = 'RUIM'
    return n


# Programa Principal
resp = notas(5.5, 2.5, 1, 6.5, sit=True)
print(resp)
# help(notas)
