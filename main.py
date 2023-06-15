from PIL import Image

def converter_para_preto_e_branco(caminho_imagem, limiar=128):
    # Abrir a imagem
    imagem = Image.open(caminho_imagem)

    # Converter a imagem para tons de cinza, se necessário
    if imagem.mode != "L":
        imagem = imagem.convert("L")

    # Criar uma nova imagem preto e branco
    imagem_pb = Image.new("1", imagem.size)  # Criar uma nova imagem binária (preto e branco)
    largura, altura = imagem.size

    for x in range(largura):
        for y in range(altura):
            # Obter o valor de escala de cinza do pixel
            valor_cinza = imagem.getpixel((x, y))

            # Definir o pixel na imagem preto e branco
            if valor_cinza >= limiar:
                imagem_pb.putpixel((x, y), 255)  # Pixel branco
            else:
                imagem_pb.putpixel((x, y), 0)  # Pixel preto

    # Salvar a imagem preto e branco
    imagem_pb.save("imagem_preto_e_branco.png")


def converter_para_tons_de_cinza(caminho_imagem):
    # Abrir a imagem
    imagem = Image.open(caminho_imagem)

    # Converter a imagem para tons de cinza
    imagem_tons_de_cinza = Image.new("L", imagem.size)  # Criar uma nova imagem tons de cinza
    largura, altura = imagem.size

    for x in range(largura):
        for y in range(altura):
            # Obter os valores RGB do pixel
            r, g, b = imagem.getpixel((x, y))

            # Calcular o valor de tons de cinza
            valor_tons_de_cinza = int(0.2989 * r + 0.5870 * g + 0.1140 * b)

            # Definir o pixel na imagem tons de cinza
            imagem_tons_de_cinza.putpixel((x, y), valor_tons_de_cinza)

    # Salvar a imagem tons de cinza
    imagem_tons_de_cinza.save("imagem_tons_de_cinza.png")


variavel = input("Deseja transformar a imagem em preto e branco ou em níveis de cinza?")

imagem = input("Digite o nome da imagem")


if variavel == "imagem em preto e branco":
    converter_para_preto_e_branco(imagem)

elif variavel == "níveis de cinza" or variavel == "niveis de cinza":
    converter_para_tons_de_cinza(imagem)
