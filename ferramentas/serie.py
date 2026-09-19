# -*- coding: utf-8 -*-
"""Recorta a série do Panamera da folha de contato para o acervo do site.

A folha (`serie-panamera-aprovada.jpg`, 1984x2200) tem dez vistas em grade de
três colunas, a última linha com uma só. As coordenadas abaixo são medidas na
folha; se a folha mudar, medir de novo em vez de adivinhar.

Uso:  python3 ferramentas/serie.py <folha.jpg> <pasta-de-saida>
"""
import subprocess, sys, os

COLS = [(18, 632), (674, 633), (1334, 634)]
LINHAS = [(40, 449), (569, 471), (1124, 474), (1680, 476)]


def recortar(folha, destino):
    os.makedirs(destino, exist_ok=True)
    n = 0
    for li, (ly, lh) in enumerate(LINHAS):
        for ci, (cx, cw) in enumerate(COLS):
            if li == 3 and ci > 0:
                continue
            n += 1
            bruto = os.path.join(destino, 'v%02d.png' % n)
            subprocess.run(['magick', folha, '-crop',
                            '%dx%d+%d+%d' % (cw - 8, lh - 8, cx + 4, ly + 4),
                            '+repage', bruto], check=True)
            for larg in (640, 400):
                base = os.path.join(destino, 'g665-%02d-%d' % (n, larg))
                subprocess.run(['magick', bruto, '-resize', '%dx' % larg,
                                '-quality', '84', base + '.jpg'], check=True)
                subprocess.run(['magick', bruto, '-resize', '%dx' % larg,
                                '-quality', '80', '-define', 'webp:method=6',
                                base + '.webp'], check=True)
            os.remove(bruto)
    return n


if __name__ == '__main__':
    print('vistas:', recortar(sys.argv[1], sys.argv[2]))
