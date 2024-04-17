import sys
from PIL import Image

def juntar_imagens_verticamente(lista_de_imagens):
    imagens = [Image.open(imagem) for imagem in lista_de_imagens]
    
    largura_maxima = max(imagem.width for imagem in imagens)
    altura_total = sum(imagem.height for imagem in imagens)

    imagem_final = Image.new('RGB', (largura_maxima, altura_total))
    
    y_offset = 0
    for imagem in imagens:
        imagem_final.paste(imagem, (0, y_offset))
        y_offset += imagem.height
    
    caminho_imagem_final = 'imagem_final.png'
    imagem_final.save(caminho_imagem_final)
    return caminho_imagem_final

if __name__ == "__main__":
    if len(sys.argv) > 1:
        caminhos_de_imagem = sys.argv[1:]
        caminho_imagem_final = juntar_imagens_verticamente(caminhos_de_imagem)
        print(f"A imagem final foi salva como: {caminho_imagem_final}")
    else:
        print("Por favor, forneça os caminhos das imagens como argumentos ao executar o script.")
