# Problema de Satisfação Booleana (SAT)
Este repositório contém os materiais do segundo seminário da disciplina Projeto e Análise de Algoritmos, abordando o Problema de Satisfação Booleana (Satisfiability Problem – SAT).

# Apresentação
O vídeo da apresentação do seminário está disponível no YouTube:
👉 

# Conteúdo do Repositório
Slides: ProblemadeSatisfaçãoBooleana_Lauryane.pdf
Código-fonte: implementação de um resolvedor de SAT em Python usando backtracking.
Instâncias do problema: fórmulas booleanas testadas no estudo de caso.
Resultados: saída do algoritmo para cada fórmula.

# Descrição do Problema
O Problema de Satisfação Booleana (SAT) consiste em determinar se existe alguma atribuição de valores True/False para as variáveis de uma fórmula booleana que torne toda a expressão verdadeira.

Exemplo de fórmula:
(A∨B)∧(¬A∨C)

SAT foi o primeiro problema provado NP-Completo (Cook–Levin), e é fundamental para diversas áreas:

verificação formal
inteligência artificial
criptografia
compiladores
otimização e modelagem

Qualquer fórmula booleana pode ser convertida para CNF (Forma Normal Conjuntiva), formato padrão utilizado por algoritmos de SAT.

# Pseudocodigo do algoritmo
backtrack(ϕ):

    if ϕ = ∅: return True
    
    if ε ∈ ϕ: return False
    
    let x = pick_variable(ϕ)

    return backtrack(ϕ|x) OR backtrack(ϕ|¬x)
    
fontes:
https://www.cis.upenn.edu/~cis1890/files/Lecture3.pdf
https://scispace.com/pdf/handbook-of-satisfiability-2dsvkz551d.pdf

# Implementação
A implementação foi feita em Python, utilizando um algoritmo de backtracking com redução dinâmica de cláusulas.

# Formato de entrada
A fórmula / expressão deve estar na forma conjuntiva normal (CNF).

É possível utilizar esta ferramenta para CNF:
https://www.learnmathclass.com/logic/propositional-logic/syntax/normal-forms

Para testar mais de uma fórmula, é possivel adicionar no arquivo exemplos.txt.
o formato é:

nome_da_formula:disjunção1;disjunção2;...

cada disjunção é no formato: Literal1,Literal2, ...

cada literal é uma variável ou sua negação: A,-B,C ...

# Instância 
[exemplos.txt](exemplos.txt)

# Resultado Obtido
Para cada fórmula, o resolvedor retornou uma atribuição satisfatória (quando possível).
Exemplos:

🔹 Fórmula Y

Solução:
A = True  
B = True  
C = True  

🔹 Fórmula F

Solução:
A = True

🔹 Fórmula Z

Solução:
A = True  
B = True  



