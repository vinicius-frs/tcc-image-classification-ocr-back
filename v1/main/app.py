from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/getImageClass', methods=['POST'])
@cross_origin()
def getImageClass():
    import funcoes.decode_base64_image as di
    import funcoes.image_classification as ic
    import uuid
    import os
    if request.is_json:
        body = request.get_json()

        if not "img_base64" in body:
            return {"error": "Image string missing"}, 422
        
        decoded = di.decodeBase64Image(body["img_base64"])

        id = str(uuid.uuid4())
        image = open('image'+id+'.jpeg', 'wb')
        image.write(decoded)
        image.close()

        objClass = ic.getImageClass('image'+id+'.jpeg')
        os.remove('image'+id+'.jpeg')
        return objClass, 201

    return {"error": "Request must be JSON"}, 415

@app.route('/getImageText', methods=['POST'])
@cross_origin()
def getImageText():
    import funcoes.decode_base64_image as di
    import funcoes.ocr_google_vision as ocr
    import funcoes.extract_key_data as ed
    import uuid
    import os

    if request.is_json:
        body = request.get_json()

        if not "img_base64" in body:
            return {"error": "Image string missing"}, 422
        if not "img_class" in body:
            return {"error": "Image class missing"}, 422

        decoded = di.decodeBase64Image(body["img_base64"])

        id = str(uuid.uuid4())
        image = open('image'+id+'.jpeg', 'wb')
        image.write(decoded)
        image.close()

        imageText = ocr.getImageText('image'+id+'.jpeg')
        os.remove('image'+id+'.jpeg')
        
        if body["img_class"] == "CNH frente":
            dados = ed.extractDadosCNHFrente(imageText)

        elif body["img_class"] == "RG verso":
            dados = ed.extractDadosRGVerso(imageText)

        elif body["img_class"] == "CPF frente":
            dados = ed.extractDadosCPFFrente(imageText)

        return dados, 201
    
    return {"error": "Request must be JSON"}, 415