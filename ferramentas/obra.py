# -*- coding: utf-8 -*-
"""O método em camadas de registro.

A primeira versão era uma construção civil em isometria, e o Kauan reprovou:
puxava para arquitetura. Esta é a mesma ideia de processo, em linguagem de
precisão em vez de obra: cinco chapas finas que descem e assentam uma sobre a
outra, alinhadas por dois pinos de registro.

É um empilhamento de passes, como gravura ou montagem ótica. Cada chapa traz
uma marca em fio de cabelo que diz o que aquela etapa faz, e a ordem importa
porque chapa fora de registro não fecha imagem nenhuma. É exatamente o que a
copy da seção diz: cinco etapas, uma ordem.
"""
import math

CX, CY = 250.0, 300.0
KX, KY = 0.92, 0.32          # isometria achatada: chapa vista de cima e de frente
LX, LY = 124.0, 80.0         # meia-largura e meia-profundidade da chapa
PASSO = 36.0                 # distância entre uma chapa e a seguinte
ESP = 5.0                    # espessura aparente


def iso(x, y, z=0.0):
    return (CX + (x - y) * KX, CY + (x + y) * KY - z)


def face(z, lx=LX, ly=LY):
    c = [(-lx, -ly), (lx, -ly), (lx, ly), (-lx, ly)]
    p = [iso(x, y, z) for x, y in c]
    return ('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z'
            % (p[0][0],p[0][1], p[1][0],p[1][1], p[2][0],p[2][1], p[3][0],p[3][1]))


def canto(z, lx=LX, ly=LY):
    """As duas faces da frente, que dão espessura à chapa."""
    a = iso(-lx, ly, z);  b = iso(lx, ly, z);  d = iso(lx, -ly, z)
    return ('M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z '
            'M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f L%.1f,%.1f Z'
            % (a[0],a[1], b[0],b[1], b[0],b[1]+ESP, a[0],a[1]+ESP,
               b[0],b[1], d[0],d[1], d[0],d[1]+ESP, b[0],b[1]+ESP))


def seg(p, q):
    a, b = iso(*p), iso(*q)
    return 'M%.1f,%.1f L%.1f,%.1f' % (a[0], a[1], b[0], b[1])


def marca(n, z):
    """O fio de cabelo em cima da chapa. Cada etapa tem o seu, senão as cinco
       chapas viram cinco retângulos iguais e o desenho não diz nada."""
    if n == 1:                                   # Diagnóstico: medir o terreno
        d = []
        for gx in range(-3, 4):
            for gy in range(-2, 3):
                x, y = gx * 26, gy * 26
                d.append(seg((x - 4, y, z), (x + 4, y, z)))
                d.append(seg((x, y - 4, z), (x, y + 4, z)))
        return ' '.join(d)
    if n == 2:                                   # Posicionamento: um eixo só
        return (seg((-92, 0, z), (92, 0, z)) + ' ' +
                seg((-92, -8, z), (-92, 8, z)) + ' ' + seg((92, -8, z), (92, 8, z)))
    if n == 3:                                   # Conteúdo: ritmo que repete
        return ' '.join(seg((x, -52, z), (x, 52, z)) for x in range(-90, 91, 20))
    if n == 4:                                   # Venda: o que converge
        return ' '.join(seg((-92, y, z), (86, 0, z)) for y in (-56, -28, 0, 28, 56))
    # Jornada: o ciclo que se fecha
    d = []
    passos = 40
    for k in range(passos):
        a1 = 2 * math.pi * k / passos
        a2 = 2 * math.pi * (k + 1) / passos
        if k % 2:
            continue
        d.append(seg((math.cos(a1) * 78, math.sin(a1) * 46, z),
                     (math.cos(a2) * 78, math.sin(a2) * 46, z)))
    return ' '.join(d)


def camada(n, corpo):
    return (
'      <path class="obra__chapa" style="--e:var(--e%d,0)" d="%s"/>\n'
'      <path class="obra__canto" style="--e:var(--e%d,0)" d="%s"/>\n'
'      <path class="obra__borda" style="--e:var(--e%d,0);--a:var(--a%d,0)" d="%s"/>\n'
'      <path class="obra__marca" style="--e:var(--e%d,0);--a:var(--a%d,0)" d="%s"/>\n'
'      <path class="obra__foco" style="--a:var(--a%d,0)" d="%s"/>'
        % (n, corpo['face'], n, corpo['canto'], n, n, corpo['face'], n, n, corpo['marca'],
           n, corpo['face']))


def montar():
    L = []; A = L.append
    A('<svg class="obra" viewBox="40 60 420 400" aria-hidden="true">')
    A('  <g class="obra__corpo">')

    # Os pinos de registro: o que diz que as chapas só servem alinhadas.
    for sx, sy in ((-LX - 16, LY + 10), (LX + 16, -LY - 10)):
        A('    <path class="obra__pino" d="%s"/>'
          % seg((sx, sy, -16), (sx, sy, PASSO * 4 + 30)))

    for n in range(1, 6):
        z = PASSO * (n - 1)
        A('    <g class="obra__camada" style="--e:var(--e%d,0)">' % n)
        A(camada(n, {'face': face(z), 'canto': canto(z), 'marca': marca(n, z)}))
        A('    </g>')

    A('  </g>')
    A('</svg>')
    return '\n        '.join(L)


if __name__ == '__main__':
    print(montar())
