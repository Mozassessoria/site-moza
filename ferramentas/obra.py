# -*- coding: utf-8 -*-
"""A obra do método: uma estrutura sendo levantada em isometria.

Linguagem oposta à da roda de propósito. A roda é objeto renderizado, com
volume e luz; esta é prancha técnica, traço puro. Duas seções com a mesma
mecânica de rolagem não podem ter o mesmo desenho.

Cada etapa do método levanta uma camada, e a ordem é a ordem da obra:
  1 Diagnóstico   o terreno, medido antes de qualquer coisa
  2 Posicionamento a fundação, que decide onde a coisa fica de pé
  3 Conteúdo       os pilares, que sobem todo dia
  4 Venda          a laje, onde o peso finalmente apoia
  5 Jornada        o guarda-corpo e as cotas, o que sustenta depois de pronto

Os traços se desenham por stroke-dashoffset com pathLength="1": assim não
preciso medir comprimento de caminho nenhum, e mexer na geometria não pede
recalcular constante.
"""
import math

CX, CY = 260.0, 320.0
C30, S30 = math.cos(math.radians(30)), math.sin(math.radians(30))
LADO, ALTURA, GUARDA = 60, 110, 40      # meia-largura, pé-direito, guarda-corpo


def iso(x, y, z=0.0):
    return (CX + (x - y) * C30, CY + (x + y) * S30 - z)


def linha(a, b):
    p, q = iso(*a), iso(*b)
    return 'M%.1f,%.1f L%.1f,%.1f' % (p[0], p[1], q[0], q[1])


def quadrado(z, lado=LADO):
    c = [(-lado, -lado), (lado, -lado), (lado, lado), (-lado, lado)]
    p = [iso(x, y, z) for x, y in c]
    return ('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z'
            % (p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1], p[3][0], p[3][1]))


def camada(n, d):
    """Cada camada sai em dois traços no mesmo caminho: o de baixo assenta em
       linha muda, o de cima passa em ciano enquanto a etapa está em foco."""
    return (
'      <path class="obra__traco" style="--e:var(--e%d,0)" pathLength="1" d="%s"/>\n'
'      <path class="obra__foco"  style="--e:var(--e%d,0);--a:var(--a%d,0)" pathLength="1" d="%s"/>'
        % (n, d, n, n, d))


def montar():
    L = []; A = L.append
    A('<svg class="obra" viewBox="30 70 460 400" aria-hidden="true">')
    A('  <g class="obra__corpo">')

    # 1 · o terreno
    g = []
    for k in range(-110, 111, 44):
        g.append(linha((-110, k), (110, k)))
        g.append(linha((k, -110), (k, 110)))
    A('    <g class="obra__camada obra__camada--terreno">')
    A(camada(1, ' '.join(g)))
    A('    </g>')

    # 2 · a fundação, com as estacas nos cantos
    f = [quadrado(0)]
    for sx in (-LADO, LADO):
        for sy in (-LADO, LADO):
            f.append(linha((sx, sy, 0), (sx, sy, 14)))
    A('    <g class="obra__camada">')
    A(camada(2, ' '.join(f)))
    A('    </g>')

    # 3 · os pilares
    p = [linha((sx, sy, 0), (sx, sy, ALTURA))
         for sx in (-LADO, LADO) for sy in (-LADO, LADO)]
    A('    <g class="obra__camada">')
    A(camada(3, ' '.join(p)))
    A('    </g>')

    # 4 · a laje, com as vigas que a travam
    lj = [quadrado(ALTURA),
          linha((-LADO, 0, ALTURA), (LADO, 0, ALTURA)),
          linha((0, -LADO, ALTURA), (0, LADO, ALTURA))]
    A('    <g class="obra__camada">')
    A(camada(4, ' '.join(lj)))
    A('    </g>')

    # 5 · guarda-corpo e cotas
    gc = [quadrado(ALTURA + GUARDA)]
    for sx in (-LADO, LADO):
        for sy in (-LADO, LADO):
            gc.append(linha((sx, sy, ALTURA), (sx, sy, ALTURA + GUARDA)))
    # cota horizontal, embaixo, com as marcas de ponta
    gc.append(linha((-LADO, 128), (LADO, 128)))
    for sx in (-LADO, LADO):
        gc.append(linha((sx, 118), (sx, 138)))
    # cota vertical, à direita, do chão ao guarda-corpo
    gc.append(linha((128, LADO, 0), (128, LADO, ALTURA + GUARDA)))
    for z in (0, ALTURA + GUARDA):
        gc.append(linha((118, LADO, z), (138, LADO, z)))
    A('    <g class="obra__camada">')
    A(camada(5, ' '.join(gc)))
    A('    </g>')

    A('  </g>')
    A('</svg>')
    return '\n        '.join(L)


if __name__ == '__main__':
    print(montar())
