import funcoes.image_classification as ic
import funcoes.ocr_google_vision as ocr
import funcoes.file_control as f
import funcoes.extract_key_data as ed
import json
import io

print("Selecione uma imagem")
imagePath = f.openImageSelector()

imageClass = ic.getImageClass(imagePath)

if imageClass["confidence"] <= 50:
    print("Classificação da imagem não identificada!")
    exit()

imageText = ocr.getImageText(imagePath) #normal
# imageText = json.dumps(ocr.getImageText(imagePath)) #quando for salvar ocr em txt
# with io.open('D:/Dev/Python/tcc-image-classification-ocr/v1/main/json_cpf_frente.txt', 'rb') as json_txt:
#     imageText = json.loads(json_txt.read())

if imageClass["class"] == "CNH frente":
    print("Classificação da imagem: CNH frente")
    dados = ed.extractDadosCNHFrente(imageText)

elif imageClass["class"] == "CNH verso":
    print("Classificação da imagem: CNH verso")

elif imageClass["class"] == "RG frente":
    print("Classificação da imagem: RG frente")

elif imageClass["class"] == "RG verso":
    print("Classificação da imagem: RG verso")
    dados = ed.extractDadosRGVerso(imageText)

elif imageClass["class"] == "CPF frente":
    print("Classificação da imagem: CPF frente")
    dados = ed.extractDadosCPFFrente(imageText)

elif imageClass["class"] == "CPF verso":
    print("Classificação da imagem: CPF verso")

print(dados)