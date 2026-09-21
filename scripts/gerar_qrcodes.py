# -*- coding: utf-8 -*-
"""
Gera os QR Codes das paginas de leitura do Territorio Inventivo - Pequena Africa.

QR limpo (sem logo), alta resolucao para impressao.
Idempotente: rodar de novo apenas regrava os PNGs em qrcodes/.

Uso:
    python -m pip install "qrcode[pil]"
    python scripts\\gerar_qrcodes.py
"""

from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_Q

BASE_URL = "https://joaopauloponte.github.io/territorio-inventivo-textos"

# (arquivo html, nome do PNG de saida, titulo legivel)
PAGINAS = [
    ("texto-01-linha-do-tempo.html",   "qr-texto-01-linha-do-tempo.png",   "Linha do Tempo do MUHCAB"),
    ("texto-02-mapa-da-diaspora.html", "qr-texto-02-mapa-da-diaspora.png", "Mapa Digital da Diaspora"),
    ("texto-03-encruzilhada.html",     "qr-texto-03-encruzilhada.png",     "Sala Encruzilhada"),
    ("texto-04-verbetes-maquetes.html", "qr-texto-04-verbetes-maquetes.png", "Verbetes das Maquetes"),
]

BOX_SIZE = 20   # ~20 px por modulo -> arquivo grande, bom para impressao
BORDER = 4      # quiet zone minima recomendada pela especificacao


def main() -> None:
    raiz = Path(__file__).resolve().parent.parent
    destino = raiz / "qrcodes"
    destino.mkdir(exist_ok=True)

    for arquivo_html, nome_png, titulo in PAGINAS:
        url = f"{BASE_URL}/{arquivo_html}"

        qr = qrcode.QRCode(
            version=None,                     # ajusta o tamanho automaticamente
            error_correction=ERROR_CORRECT_Q,  # ~25% de tolerancia a dano
            box_size=BOX_SIZE,
            border=BORDER,
        )
        qr.add_data(url)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        caminho = destino / nome_png
        img.save(caminho)

        largura, altura = img.size
        print(f"[ok] {titulo}")
        print(f"     {url}")
        print(f"     -> {caminho}  ({largura}x{altura} px)")

    print(f"\n{len(PAGINAS)} QR Codes gerados em: {destino}")


if __name__ == "__main__":
    main()
