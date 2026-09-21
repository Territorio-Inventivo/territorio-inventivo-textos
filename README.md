# Território Inventivo — Pequena África · Páginas de leitura

Páginas de leitura acessíveis do projeto **Território Inventivo — Pequena África**,
ligado ao **MUHCAB** (Museu da História e da Cultura Afro-Brasileira).

Cada página é um HTML autocontido, em texto corrido, pensado para funcionar bem
com **leitores de tela** e com o plugin de tradução para Libras **VLibras**
(`vlibras-plugin.js`). Marcação com `lang="pt-BR"`, imagens com texto alternativo
e suporte a tema claro/escuro.

A mesma URL atende aos dois cenários de uso:

- **No site** — incorporada no Experience Builder através do widget *Embed*;
- **Na exposição** — acessada pelo público via **QR Code** impresso.

## Páginas

| # | Título | Arquivo |
|---|--------|---------|
| 01 | Linha do Tempo do MUHCAB | `texto-01-linha-do-tempo.html` |
| 02 | Mapa Digital da Diáspora | `texto-02-mapa-da-diaspora.html` |
| 03 | Sala Encruzilhada | `texto-03-encruzilhada.html` |
| 04 | Verbetes das Maquetes | `texto-04-verbetes-maquetes.html` |

O `index.html` reúne e linka as quatro páginas.

## Publicação

O site é publicado pelo **GitHub Pages** (branch `main`, raiz `/`):

<https://joaopauloponte.github.io/territorio-inventivo-textos/>

## QR Codes

Os QR Codes de cada texto ficam em `qrcodes/`, gerados em alta resolução para
impressão pelo script `scripts/gerar_qrcodes.py`:

```powershell
python -m pip install "qrcode[pil]"
python scripts\gerar_qrcodes.py
```

O script é idempotente — rodar de novo apenas regrava os PNGs.

## Identidade visual

- Laranja `#E55000`
- Teal `#229B8A`
