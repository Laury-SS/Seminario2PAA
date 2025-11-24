def pick_variable(phi):
    for clause in phi:
        for lit in clause:
            return lit.lstrip('-')  # remove o '-' se existir


def reduce_formula(phi, var, value):
    new_formula = []

    for clause in phi:
        new_clause = []
        clause_satisfied = False

        for lit in clause:
            if lit == var:  # literal positivo
                if value is True:
                    clause_satisfied = True
                    break
                else:
                    continue  # literal falso → ignora
            elif lit == f"-{var}":  # literal negativo
                if value is False:
                    clause_satisfied = True
                    break
                else:
                    continue
            else:
                new_clause.append(lit)

        # se a cláusula foi satisfeita, simplesmente a removemos
        if clause_satisfied:
            continue

        new_formula.append(new_clause)

    return new_formula


def backtrack(phi):
    # Caso 1: fórmula vazia (todas as cláusulas satisfeitas)
    if phi == []:
        return True

    # Caso 2: cláusula vazia presente (contradição)
    if any(clause == [] for clause in phi):
        return False

    # Escolha de variável (pega o primeiro literal da primeira cláusula)
    x = pick_variable(phi)

    # Tenta atribuir x = True
    if backtrack(reduce_formula(phi, x, True)):
        return True

    # Tenta atribuir x = False
    return backtrack(reduce_formula(phi, x, False))


if __name__ == '__main__':
    # Exemplo de fórmula (em CNF)
    phi = [
        ["x1", "x2"],
        ["-x1"],
        ["-x2"]
    ]
    # Para essa entrada, o resultado deve ser falso
    print(backtrack(phi))

    # Resolução das instâncias apresentadas
    # o formato de cada problema é -> nome_da_formula:disjunção1;disjunção2;...
    # cada disjunção é no formato: Literal1,Literal2, ...
    # cada literal é uma variável ou sua negação: A,-B,C ...
    # Não é obrigatório usar A, B, C, etc para variáveis. (Ex: x,y,z,etc)

    # Ler o arquivos de exemplos:

    with open('exemplos.txt', 'r+') as exemplos:
        for line in exemplos:
            nome_formula, disjuncoes = line.split('\n')[0].split(':')
            disjuncoes = [y.split(",") for y in disjuncoes.split(";")]

            aux = [ f"({' + '.join(x)})" for x in disjuncoes]
            print(f"{nome_formula} = {' . '.join(aux)}")
            print(backtrack(disjuncoes))


