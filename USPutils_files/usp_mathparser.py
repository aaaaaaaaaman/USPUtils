
import math

def traduzir(expr: str):
    expr = expr.replace('^', '**')
    expr = expr.replace('pi', str(math.pi))
    expr = expr.replace('e', str(math.e))

    while 'root_' in expr:
        i = expr.find('root_')
        j = i + 5
        while j < len(expr) and expr[j].isdigit():
            j += 1
        n = int(expr[i+5:j])
        if expr[j] != '(':
            raise ValueError(f"Formato inválido em root_{n} — esperado '(' após índice.")
        j += 1
        parens = 1
        start = j
        while j < len(expr) and parens > 0:
            if expr[j] == '(':
                parens += 1
            elif expr[j] == ')':
                parens -= 1
            j += 1
        conteudo = expr[start:j-1]
        convertido = f"({conteudo})**(1/{n})"
        expr = expr[:i] + convertido + expr[j:]
    return expr

def calcular(expr: str, x=None):
    convertido = traduzir(expr)
    contexto = {"math": math}
    if x is not None:
        contexto["x"] = x
    return eval(convertido, contexto)
