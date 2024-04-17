# Merge-Images

## Visão Geral
O repositório Merge-Images contém um script Python (`merge_images.py`) projetado para combinar múltiplas imagens em uma única imagem, alinhando-as verticalmente.

### Uso
Para usar este script, você deve fornecer os caminhos das imagens que deseja combinar como argumentos na linha de comando. O script não possui uma interface gráfica, portanto, tudo é manipulado via linha de comando.

```bash
python merge_images.py caminho/imagem1.png caminho/imagem2.png caminho/imagem3.png
```

**Saída:**
- Produz um arquivo chamado `imagem_final.png`, que contém todas as imagens fornecidas combinadas verticalmente.

## Requisitos de Instalação
Este script requer Python 3 e a biblioteca PIL (Pillow).

Para instalar a Pillow, execute:
```bash
pip install Pillow
```
