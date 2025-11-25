# Funcao auxiliar para escolher a proxima variavel
def pick_variable(phi):
    for clause in phi:
        for lit in clause:
            return lit.lstrip('-')  # remove o '-' se existir


# funcao auxiliar: reduzir a formula a partir da atribuicao da variavel atual
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

# Funcao principal
def backtrack(phi, assignment=None):
    if assignment is None:
        assignment = {}

    # Caso 1: fórmula vazia → solução encontrada
    if phi == []:
        return assignment

    # Caso 2: cláusula vazia → contradição
    if any(clause == [] for clause in phi):
        return None

    # variável escolhida
    x = pick_variable(phi)

    # Tenta x = True
    new_assign = assignment.copy()
    new_assign[x] = True
    result = backtrack(reduce_formula(phi, x, True), new_assign)
    if result is not None:
        return result

    # Tenta x = False
    new_assign = assignment.copy()
    new_assign[x] = False
    return backtrack(reduce_formula(phi, x, False), new_assign)


if __name__ == '__main__':
    # Exemplo de fórmula (em CNF)
    phi = [
        ["x1", "x2"],
        ["-x1"],
        ["-x2"]
    ]
    aux = [f"({' + '.join(x)})" for x in phi]
    print(f"phi = {' . '.join(aux)}")
    # Para essa entrada, o resultado deve ser falso
    print(False if backtrack(phi) is None else True)
    print()

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

            aux = [f"({' + '.join(x)})" for x in disjuncoes]
            print(f"{nome_formula} = {' . '.join(aux)}")

            solucao = backtrack(disjuncoes)

            if solucao is None:
                print("Insatisfatível")
            else:
                # imprime a solução formatada
                for var, val in solucao.items():
                    print(f"{var} = {val}")
            print()
