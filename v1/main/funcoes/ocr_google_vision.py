import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:/Dev/Python/tcc-image-classification-ocr/credential/tcc-ocr-363917-ecdc5c2a609d.json"

def getImageText(image_path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations


    text_content = {
        "texts": [],
        "bounds": []
    }

    for text in texts:
        text_content["texts"].append('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        text_content["bounds"].append('{}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    return text_content