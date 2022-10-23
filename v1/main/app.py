from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/getImageClass")
def getImageClass():
    import funcoes.decode_base64_image as di
    import funcoes.image_classification as ic
    if request.is_json:
        body = request.get_json()

        if not "img_base64" in body:
            return {"error": "Image string missing"}, 422
        
        decoded = di.decodeBase64Image(body["img_base64"])

        image = open('image.jpeg', 'wb')
        image.write(decoded)
        image.close()

        return ic.getImageClass(), 201

    return {"error": "Request must be JSON"}, 415

@app.get("/getImageText")
def getImageText():
    import funcoes.decode_base64_image as di
    import funcoes.ocr_google_vision as ocr
    import funcoes.extract_key_data as ed

    if request.is_json:
        body = request.get_json()

        if not "img_base64" in body:
            return {"error": "Image string missing"}, 422
        if not "img_class" in body:
            return {"error": "Image class missing"}, 422

        decoded = di.decodeBase64Image(body["img_base64"])

        image = open('image.jpeg', 'wb')
        image.write(decoded)
        image.close()

        imageText = ocr.getImageText()

        if body["img_class"] == "CNH frente":
            dados = ed.extractDadosCNHFrente(imageText)

        elif body["img_class"] == "RG verso":
            dados = ed.extractDadosRGVerso(imageText)

        elif body["img_class"] == "CPF frente":
            dados = ed.extractDadosCPFFrente(imageText)

        return dados, 201
    
    return {"error": "Request must be JSON"}, 415