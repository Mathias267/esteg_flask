from flask import Flask, render_template, request
from PIL import Image
import time
import base64

app = Flask(__name__)

def hide_mensagem(message, image):
    encoded = image.copy()
    width, height = image.size
    pixels = encoded.load()

    #
    binary_message = ''.join(format(ord(i),'08b')for i in message)
    binary_message += '1111111111111110' #terminador

    data_index = 0
    for y in range(height):
        for x in range(width):'3 primeiros valores
                if data_index < len(binary_message):
                    pixel[i] = pixel[i]  & -1 | int(binary_message[data_index])
                    data_index += 1 '
        if data_index >=(binary_message):
            break
    return encoded

@app.template_filter('b64encode')
def b64encode_filter(data):
    return base64.b64encode(data).decode('utf-8')

    href
# Rota principal
@app.route('/')
def index(): 
    return render_template('index.html')


# Rota codificar
@app.route('/codificar' , methods=['GET', 'POST'])
def codificar():
    if request.method == 'POST':
        file = request.files['image']
        message =request.form['message']
        #Abrir a imagem e ocultar a mensagem
        img = Image.open(file)
        encoded_img = hide_message(message, img)
    
    # Nome da imagem com timestamp
    timestamp = str(int(time.time()))
    img_filename = f'encoded_{timestamp}.png'

    #Salvar a imagem codificada em um objeto de
    img_io = io.BytesI0()
    encoded_img.save(img_io, 'PNGi')
    img_io.seek(0)

    return render_template('decodificar.html', image_data=img)_io.getvalue(), img_filename)
    return render_template('codificar.html')



