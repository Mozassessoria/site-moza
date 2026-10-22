# -*- coding: utf-8 -*-
"""O método em chapas de registro, versão 3D.

A primeira versão era construção civil em isometria e puxava para arquitetura.
A segunda era isometria falsa em SVG: parelelogramo chapado, sem material e sem
câmera. O Kauan reprovou por simples, e estava certo.

Esta é a mesma ideia, executada noutro nível: as chapas são elementos reais em
perspectiva 3D do navegador, com vidro, aresta que pega luz, profundidade de
campo e uma câmera que se move com a rolagem. A isometria desenhada à mão
morreu: quem faz o ângulo agora é o `perspective` do palco.

O que cada chapa carrega continua sendo a marca técnica da etapa, porque cinco
retângulos iguais não contam história nenhuma.
"""

ETAPAS = [
    ('malha',      'Diagnóstico'),
    ('eixo',       'Posicionamento'),
    ('ritmo',      'Conteúdo'),
    ('convergir',  'Venda'),
    ('ciclo',      'Jornada'),
]


def marca(tipo):
    """O fio de cabelo sobre a chapa, em SVG de 400x260."""
    if tipo == 'malha':
        d = []
        for gx in range(-5, 6):
            for gy in range(-3, 4):
                x, y = 200 + gx * 32, 130 + gy * 32
                d.append('M%d,%d h9 M%d,%d v9' % (x - 4.5, y, x, y - 4.5))
        return ' '.join(d)
    if tipo == 'eixo':
        return 'M40,130 H360 M40,118 V142 M360,118 V142'
    if tipo == 'ritmo':
        return ' '.join('M%d,56 V204' % x for x in range(48, 361, 26))
    if tipo == 'convergir':
        return ' '.join('M40,%d L352,130' % y for y in (44, 87, 130, 173, 216))
    return ('M200,42 C288,42 352,81 352,130 C352,179 288,218 200,218 '
            'C112,218 48,179 48,130 C48,81 112,42 200,42')


def montar():
    L = []; A = L.append
    A('<div class="obra" aria-hidden="true">')
    A('  <div class="obra__camara">')
    A('    <div class="obra__pilha">')
    for i, (tipo, nome) in enumerate(ETAPAS, start=1):
        A('      <div class="chapa" style="--i:%d;--e:var(--e%d,0);--a:var(--a%d,0)">' % (i - 1, i, i))
        A('        <div class="chapa__corpo">')
        A('          <svg class="chapa__marca" viewBox="0 0 400 260" aria-hidden="true">')
        A('            <path d="%s"/>' % marca(tipo))
        A('          </svg>')
        A('          <span class="chapa__brilho"></span>')
        A('        </div>')
        # A régua na aresta: detalhe de instrumento, não enfeite.
        A('        <div class="chapa__regua">%s</div>' % ('<i></i>' * 14))
        A('      </div>')
    A('    </div>')
    # O eixo de registro: o que diz que as chapas só servem alinhadas.
    A('    <div class="obra__eixo"></div>')
    A('  </div>')
    A('</div>')
    return '\n        '.join(L)


if __name__ == '__main__':
    print(montar())
