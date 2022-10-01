import funcoes.image_classification as ic
import funcoes.ocr_google_vision as ocr
import funcoes.file_control as f
import json
import io
import re

print("Selecione uma imagem")
imagePath = f.openImageSelector()

imageClass = ic.getImageClass(imagePath)

if imageClass["confidence"] <= 50:
    print("Classificação da imagem não identificada!")
    exit()

imageText = ocr.getImageText(imagePath)
# with io.open('D:/Dev/Python/tcc-image-classification-ocr/v1/main/json_rg_verso.txt', 'rb') as json_txt:
#     imageText = json.loads(json_txt.read())

if imageClass["class"] == "CNH frente":
    print("Classificação da imagem: CNH frente")

elif imageClass["class"] == "CNH verso":
    print("Classificação da imagem: CNH verso")

elif imageClass["class"] == "RG frente":
    print("Classificação da imagem: RG frente")

elif imageClass["class"] == "RG verso":
    print("Classificação da imagem: RG verso")

elif imageClass["class"] == "CPF frente":
    print("Classificação da imagem: CPF frente")

elif imageClass["class"] == "CPF verso":
    print("Classificação da imagem: CPF verso")

print(imageText["texts"][0])

dados = {
    "rg": None,
    "nome": None,
    "naturalidade": None,
    "data_nascimento": None,
}

dados["rg"] = re.findall("\d{2}\.\d{3}\.\d{3}-[0-9X]", imageText["texts"][0])[0]

nome_inicio = re.search("NOME|nome", imageText["texts"][0]).span()[1]
nome_fim = re.search("FILIAÇÃO|filiação|FILIACAO|filiacao", imageText["texts"][0]).span()[0]
dados["nome"] = imageText["texts"][0][nome_inicio:nome_fim].strip()

naturalidade_inicio = re.search("NATURALIDADE|naturalidade", imageText["texts"][0]).span()[1]
naturalidade_fim = re.search("DOC ORIGEM|doc origem", imageText["texts"][0]).span()[0]
dados["naturalidade"] = imageText["texts"][0][naturalidade_inicio:naturalidade_fim].strip()

data_nascimento_inicio = re.search("DATA DE NASCIMENTO|data de nascimento", imageText["texts"][0]).span()[1]
dados["data_nascimento"] = re.findall("\d{2}\/\d{2}\/\d{4}", imageText["texts"][0][data_nascimento_inicio:len(imageText["texts"][0])])[0]

print(dados)