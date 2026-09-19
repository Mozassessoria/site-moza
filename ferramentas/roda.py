# -*- coding: utf-8 -*-
"""A roda da Moza, no padrão da referência que o Kauan mandou (18/09/2026).

O que mudou em relação à versão anterior, e por quê:

- **O aro é preto brilhante, não prata.** Era o erro que mais fazia o desenho
  parecer genérico: aro cromado é de carro de rua, aro de corrida é preto com
  brilho especular duro nas quinas.
- **Dez raios em Y.** Cada raio sai do cubo, abre em dois braços perto do aro e
  fecha vinte vãos. Raio reto é desenho de ícone; o Y é o que existe em roda de
  competição de verdade.
- **O pneu é muito mais gordo.** Na referência o aro tem 54% do diâmetro total.
  A versão anterior tinha 69%, e era isso que dava a leitura de roda de
  bicicleta.
- **Xadrez que se dissolve** no flanco, em vez de arco cheio. Sai de um
  stroke-dasharray que encurta, não de doze caminhos.

A luz continua vindo de uma direção só, em userSpaceOnUse, para todas as peças.
"""
import math

C = 230.0
LUZ = 225.0

# Raios de referência, em unidades do viewBox de 460
R_PNEU_FORA = 210.0
R_PNEU_DENTRO = 148.0
R_FLANCO_DENTRO = 113.0
R_ARO = 109.0
R_RAIO_FORA = 110.0
R_CUBO = 45.0
R_FURO = 24.0
N_RAIOS = 10


def pt(ang, r):
    a = math.radians(ang)
    return C + math.cos(a) * r, C + math.sin(a) * r


def barra(p1, p2, w1, w2):
    """Quadrilátero entre dois pontos quaisquer, com largura em cada ponta."""
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    L = math.hypot(dx, dy) or 1
    px, py = -dy / L, dx / L
    return ('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z' % (
        p1[0] + px * w1, p1[1] + py * w1,
        p2[0] + px * w2, p2[1] + py * w2,
        p2[0] - px * w2, p2[1] - py * w2,
        p1[0] - px * w1, p1[1] - py * w1))


def raio_y(ang):
    """O raio em Y: haste do cubo até a bifurcação, e dois braços até o aro."""
    haste = barra(pt(ang, 38), pt(ang, 72), 8.4, 9.6)
    bracos = [barra(pt(ang, 68), pt(ang + lado, R_RAIO_FORA), 8.0, 6.2)
              for lado in (-10.5, 10.5)]
    return haste + ' ' + ' '.join(bracos)


def aresta_raio(ang):
    """Fio de luz na quina virada para a fonte. Em peça preta brilhante é a
       única coisa que diz onde a superfície dobra."""
    n = (ang + 90) % 360
    sinal = 1 if math.cos(math.radians(n - LUZ)) > 0 else -1
    saidas = []
    for a, r1, r2, w in ((ang, 38, 72, 9.0), (ang - 10.5, 68, R_RAIO_FORA, 7.0),
                         (ang + 10.5, 68, R_RAIO_FORA, 7.0)):
        p1, p2 = pt(ang if r1 == 68 else a, r1), pt(a, r2)
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        L = math.hypot(dx, dy) or 1
        px, py = -dy / L * sinal * w, dx / L * sinal * w
        saidas.append('M%.1f,%.1f L%.1f,%.1f'
                      % (p1[0] + px, p1[1] + py, p2[0] + px, p2[1] + py))
    return ' '.join(saidas)


def arco(r, ini, fim):
    x1, y1 = pt(ini, r); x2, y2 = pt(fim, r)
    grande = 1 if (fim - ini) % 360 > 180 else 0
    return 'M%.1f,%.1f A%.1f,%.1f 0 %d 1 %.1f,%.1f' % (x1, y1, r, r, grande, x2, y2)


def montar(variante):
    L = []; A = L.append
    A('<svg class="roda roda--%s" viewBox="0 0 460 460" aria-hidden="true">' % variante)
    A('  <g class="roda__vista">')
    A('    <ellipse class="roda__chao" cx="230" cy="432" rx="150" ry="16"/>')
    A('    <g class="roda__profundidade">')
    A('      <circle class="roda__banda" cx="252" cy="212" r="179"/>')
    A('    </g>')
    A('  <g class="roda__corpo">')

    # ---- PNEU ------------------------------------------------------------
    A('    <circle class="roda__pneu" cx="230" cy="230" r="179"/>')
    A('    <circle class="roda__grao" cx="230" cy="230" r="179"/>')
    # Ombro: a quina externa da borracha pegando luz.
    A('    <path class="roda__ombro" d="%s"/>' % arco(206, 186, 268))
    A('    <path class="roda__recorte" d="%s"/>' % arco(206, 12, 70))
    # Flanco interno: o anel mais claro entre a borracha e o aro. É a peça que
    # faltava para a roda ter camadas em vez de ser um disco com um furo.
    A('    <circle class="roda__flanco" cx="230" cy="230" r="130.5"/>')
    A('    <circle class="roda__talao" cx="230" cy="230" r="113"/>')

    # ---- XADREZ ----------------------------------------------------------
    A('    <path class="roda__xadrez" d="%s"/>' % arco(176, 156, 232))
    A('    <path class="roda__xadrez" d="%s"/>' % arco(176, 308, 24))

    # ---- ARO -------------------------------------------------------------
    A('    <circle class="roda__poco" cx="230" cy="230" r="%.0f"/>' % R_RAIO_FORA)
    A('    <circle class="roda__lip" cx="230" cy="230" r="%.0f"/>' % R_ARO)
    A('    <path class="roda__lipLuz" d="%s"/>' % arco(R_ARO, 188, 262))

    # ---- RAIOS -----------------------------------------------------------
    passo = 360.0 / N_RAIOS
    for g in range(5):
        angs = (g * passo, g * passo + 180)
        A('    <g class="roda__par" style="--r:var(--r%d,0)">' % (g + 1))
        for ang in angs:
            A('      <path class="roda__raio" d="%s"/>' % raio_y(ang))
        for ang in angs:
            A('      <path class="roda__raioLuz" d="%s"/>' % aresta_raio(ang))
        A('    </g>')

    # ---- CUBO ------------------------------------------------------------
    if variante == 'monta':
        A('    <circle class="roda__cubo" cx="230" cy="230" r="%.0f"/>' % R_CUBO)
        A('    <circle class="roda__cuboAro" cx="230" cy="230" r="%.0f"/>' % (R_CUBO - 7))
        A('    <circle class="roda__furo" cx="230" cy="230" r="%.0f"/>' % R_FURO)
    else:
        A('    <circle class="roda__oco" cx="230" cy="230" r="%.0f"/>' % R_CUBO)

    A('  </g>')
    A('  </g>')
    A('</svg>')
    return '\n        '.join(L)


if __name__ == '__main__':
    import sys
    print(montar(sys.argv[1] if len(sys.argv) > 1 else 'oca'))
