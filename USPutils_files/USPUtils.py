#essa biblioetca é dependente do arquivo "usp_mathparser" ep recisa estar no mesmo diretório que ele
#AVISO, DIGITE "pip install sympy" NO TERMINAL ANTES DE USAR
#MESMO AVISO PARA "math", já que "usp_mathparser" usa da mesma
import sympy
import usp_mathparser

def help():
    print("========== AJUDA USPUtils ==========\n\n[ MATRIZES ]\n- mat_criar(linhas, colunas)\n    linhas: número de linhas da matriz\n    colunas: número de colunas da matriz\n\n- mat_preencher(matriz)\n    matriz: uma matriz criada (lista de listas); preenche via input\n\n- mat_soma(a, b)\na, b: duas matrizes do mesmo tamanho\n\n- mat_mult(a, b)\n    a: matriz\n    b: número ou outra matriz (com colunas compatíveis)\n\n- mat_det(m)\n    m: matriz quadrada (n x n)\n\n[ VETORES / ALGEBRA LINEAR ]\n- esc_dot(a, b)\n    a, b: vetores (listas do mesmo tamanho)\n\n- vet_cross(a, b)\n    a, b: vetores 3D\n\n- vet_proj(u, v)\n    u: vetor a ser projetado\n    v: vetor base\n\n- reta_vet(p1, p2)\n    p1, p2: pontos (listas do tipo [x, y, z])\n\n- plano_area(u, v)\n    u, v: vetores 3D que formam o plano\n\n[ CÁLCULO ]\n- calc_limite(expr, var='x', valor=0)\n    expr: expressão em string (ex: \"x^2 + 3*x\")\n    var: variável usada (ex: \"x\")\nvalor: número para onde x tende\n\n- calc_deriv(expr, var='x')\n   expr: expressão matemática\n    var: variável\n\n- calc_continua(expr, var='x')\n    expr: expressão\n    var: variável\n\n- calc_integral(expr, var='x', a=None, b=None)\n    expr: expressão\n    a, b: limites de integração (opcional)\n\n[ GEOMÁTICA ]\n- calc_rumo(delta_e, delta_n)\n    delta_e: diferença Leste\n    delta_n: diferença Norte\n\n- calc_azimute(n1, e1, n2, e2)\n    (n1, e1): coordenadas do ponto de origem\n    (n2, e2): coordenadas do ponto de destino\n\n- calc_distancia(n1, e1, n2, e2)\n    coordenadas de dois pontos\n\n- angulo_re(az_re, az_vante)\n    az_re: azimute do ré\n    az_vante: azimute do ponto a locar\n\n- dec2dms(angle)\n    angle: ângulo em graus decimais\n\n- dms2dec(g, m, s)\n    g: graus, m: minutos, s: segundos\n\n- calc_elementos_locacao(est_n, est_e, ponto_n, ponto_e, ref_n, ref_e)\n    est_(n,e): coordenadas da estação\n    ponto_(n,e): coordenadas do ponto a locar\n    ref_(n,e): coordenadas do ponto de ré\n\n[ QUÍMICA DOS MATERIAIS ]\n- nernst(E0, n, Q, T=298.15)\n    E0: potencial padrão (V)\n    n: número de elétrons transferidos\n    Q: quociente da reação (produtos/reagentes)\n    T: temperatura em Kelvin (padrão 298.15K)\n\n- gibbs(E, n)\n    E: potencial da célula (V)\n    n: número de elétrons\n\n- gibbs_to_k(E, n, T=298.15)\n    E: potencial padrão\n    n: elétrons\n    T: temperatura (K)\n\n====================================\n\nUse esta função sempre que esquecer o que cada coisa representa!")


# MAC
def eh_palin(t):
    """detecta se uma palavra é palindromo ou não"""
    t = t.lower()
    t_limpo = ''
    for letra in t:
        if letra.isalnum():
            t_limpo += letra
    return t_limpo == t_limpo[::-1]

def conta_vogais(t):
    """detecta vogais dentro de uma palavra"""
    vogal = 'aeiouAEIOU'
    return sum(1 for letra in t if letra in vogal)

def inverter(t):
    """inverte uma palavra"""
    return t[::-1]

def numero_par(n):
    """detecta se o numero é par"""
    return n % 2 == 0

# Matrizes
def mat_criar(linhas, colunas):
    """cria uma matriz NxM cheia de 0"""
    return [[0 for _ in range(colunas)] for _ in range(linhas)]

def mat_soma(a, b):
    """faz soma de matrizes"""
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("As matrizes devem ter as mesmas dimensões.")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def mat_mult(a, b):
    """faz multiplicação de matrizes"""
    if isinstance(b, (int, float)):
        return [[b * a[i][j] for j in range(len(a[0]))] for i in range(len(a))]
    if len(a[0]) != len(b):
        raise ValueError("Nº de colunas da primeira matriz deve ser igual ao nº de linhas da segunda.")
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]

def mat_det(m):
    """calcula determinante de uma matriz"""
    if len(m) != len(m[0]):
        return "Determinante só pode ser calculado para matrizes quadradas."
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    det = 0
    for c in range(len(m)):
        submatriz = [linha[:c] + linha[c+1:] for linha in m[1:]]
        det += ((-1)**c) * m[0][c] * mat_det(submatriz)
    return det
def mat_preencher(matriz):
    """permite o usuario preencher uma mtriz criada usando mat_criar() com os valores que desejar"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            valor = input(f"Valor para posição ({i}, {j}): ")
            try:
                matriz[i][j] = float(valor) if '.' in valor else int(valor)
            except:
                matriz[i][j] = valor  # aceita strings também se necessário
    return matriz


# Vetores
def esc_dot(a, b):
    """calcula o produto escalar"""
    return sum(x*y for x, y in zip(a, b))

def vet_cross(a, b):
    """calcula o produto vetorial de duas matrizes"""
    if len(a) != 3 or len(b) != 3:
        raise ValueError("Produto vetorial só é definido para vetores 3D.")
    return [
        a[1]*b[2] - a[2]*b[1],
        a[2]*b[0] - a[0]*b[2],
        a[0]*b[1] - a[1]*b[0]
    ]

def vet_proj(u, v):
    """calcula a projeção escalar a partir de dois vetores"""
    escalar = esc_dot(u, v)
    norma_v2 = esc_dot(v, v)
    fator = escalar / norma_v2
    return [fator * x for x in v]

def reta_vet(p1, p2):
    """calcula uma reta a partir de dois pontos"""
    d = [p2[i] - p1[i] for i in range(len(p1))]
    return f"r(t) = {[f'{p1[i]} + {d[i]}*t' for i in range(len(p1))]}"

def plano_area(u, v):
    """calcula um plano a partir de dois vetores"""
    if len(u) != 3 or len(v) != 3:
        raise ValueError("Somente vetores 3D são suportados.")
    prod = vet_cross(u, v)
    area = (sum(x**2 for x in prod))**0.5
    return area

# Cálculo simbólico
def calc_limite(expr_str, var='x', valor=0):
    """calcula limite"""
    try:
        expr = sympy.parsing.sympy_parser.parse_expr(usp_mathparser.traduzir(expr_str), evaluate=False)
        x = sympy.Symbol(var)
        return sympy.limit(expr, x, valor)
    except:
        return "Erro ao calcular o limite."

def calc_deriv(expr_str, var='x'):
    """calcula derivada"""
    try:
        expr = sympy.parsing.sympy_parser.parse_expr(usp_mathparser.traduzir(expr_str), evaluate=False)
        x = sympy.Symbol(var)
        deriv = sympy.diff(expr, x)
        if deriv == sympy.nan or deriv.has(sympy.zoo):
            return "não existe"
        return deriv
    except:
        return "não existe"

def calc_continua(expr_str, var='x'):
    """define se uma função é contínua ou não"""
    try:
        expr = sympy.parsing.sympy_parser.parse_expr(usp_mathparser.traduzir(expr_str), evaluate=False)
        x = sympy.Symbol(var)
        return sympy.simplify(sympy.limit(expr, x, 0) == expr.subs(x, 0))
    except:
        return False

def calc_integral(expr_str, var='x', a=None, b=None):
    """calcula a integral definida ou indefinida"""
    try:
        expr = sympy.parsing.sympy_parser.parse_expr(usp_mathparser.traduzir(expr_str), evaluate=False)
        x = sympy.Symbol(var)
        if a is not None and b is not None:
            res = sympy.integrate(expr, (x, a, b))
        else:
            res = sympy.integrate(expr, x)
        return str(res).replace("log", "ln")
    except:
        return "Erro ao calcular a integral."

# geomatica

def calc_rumo(delta_e,delta_n):
    """calcula o rumo"""
    ang_rad=sympy.atan2(delta_e,delta_n)
    ang_deg=sympy.deg(ang_rad)
    return ang_deg%3604

def calc_distancia_geomat(n1, e1, n2, e2):
    """Calcula a distância entre dois pontos em coordenadas N/E."""
    return ((n2 - n1)**2 + (e2 - e1)**2)**0.5

def calc_azimute(n1, e1, n2, e2):
    """Calcula o azimute entre dois pontos (em graus de 0 a 360)."""
    import sympy
    delta_n = n2 - n1
    delta_e = e2 - e1
    ang_rad = sympy.atan2(delta_e, delta_n)
    ang_deg = float(ang_rad * 180 / sympy.pi)
    return ang_deg % 360

def angulo_re(az_re, az_vante):
    """Calcula o ângulo com ré (em graus, de 0 a 360)."""
    return (az_vante - az_re) % 360

def DEC_pra_AMS(angle):
    """Converte ângulo decimal em tupla (graus, minutos, segundos)."""
    graus = int(angle)
    minutos = int((angle - graus) * 60)
    segundos = (angle - graus - minutos/60) * 3600
    return graus, minutos, round(segundos, 2)

def AMS_pra_DEC(graus, minutos, segundos):
    """Converte tupla (graus, minutos, segundos) em decimal."""
    return graus + minutos / 60 + segundos / 3600

def calc_elementos_locacao(est_n, est_e, ponto_n, ponto_e, ref_n, ref_e):
    """
    Calcula:
    - azimute de lançamento
    - ângulo com ré
    - distância
    """
    az_lanc = calc_azimute(est_n, est_e, ponto_n, ponto_e)
    az_re = calc_azimute(est_n, est_e, ref_n, ref_e)
    ang_re = angulo_re(az_re, az_lanc)
    dist = calc_distancia_geomat(est_n, est_e, ponto_n, ponto_e)
    return DEC_pra_AMS(round(az_lanc, 6)),  DEC_pra_AMS(round(ang_re, 6)), round(dist, 4)

#Quimica dos materiais