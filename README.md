# Seminario2PAA
Implementação do algoritmo de backtrack para solução do SAT

# Pseudocodigo do algoritmo


backtrack(ϕ):

    if ϕ = ∅: return True
    
    if ε ∈ ϕ: return False
    
    let x = pick_variable(ϕ)

    return backtrack(ϕ|x) OR backtrack(ϕ|¬x)
    
fontes:

https://www.cis.upenn.edu/~cis1890/files/Lecture3.pdf

https://scispace.com/pdf/handbook-of-satisfiability-2dsvkz551d.pdf

# Formato de entrada
A fórmula / expressão deve estar na forma conjuntiva normal (CNF).

Para testar mais de uma fórmula, é possivel adicionar no arquivo exemplos.txt.
o formato é:

nome_da_formula:disjunção1;disjunção2;...

cada disjunção é no formato: Literal1,Literal2, ...

cada literal é uma variável ou sua negação: A,-B,C ...

Não é obrigatório usar A, B, C, etc para variáveis. (Ex: x,y,z,etc)
