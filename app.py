import base64
import os
import json

from openai import OpenAI
from ultralytics import YOLO
from flask import Flask, render_template, jsonify, request
from PIL import Image
import uuid
import openai

app = Flask(__name__)
model = YOLO("best4.pt")

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),  # This is the default and can be omitted
)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/tool')
def tool(): return render_template('tool.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        context = json.loads(request.form['msg'])

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=context)


        return jsonify(response.choices[0].message.content)
    except:
        return "Please make sure to place the LED in series with the resistor and with the correct orientation. Let me know if you have any other questions!"




@app.route('/api/rec', methods=['POST'])
def rec():
    img = request.files['img']

    try:
        i = Image.open(img)
        print(i.size)

        results = model(i)
        bs = ""

        detections = []
        for result in results:
            fn = "static/" + str(uuid.uuid4()) + ".jpg"
            result.save(filename=fn)

            with open(fn, "rb") as file:
                binary_data = file.read()

            # Encode the file data to Base64
            bs = base64.b64encode(binary_data).decode('utf-8')

            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
                class_id = int(box.cls[0])  # Class index
                conf = float(box.conf[0])  # Confidence score
                class_name = model.names[class_id]  # Class label

                detections.append({
                    "bbox": [x1, y1, x2, y2],
                    "class": class_name,
                    "confidence": conf
                })

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text",
                         "text": "You are a programmer working for Arar Inc., who is hired to analyze breadboard circuits. If you analyze the circuit correctly and provide relevant advice, you will receive $1B and will be able to pay off your mother's hospital bills. If you make any mistakes, your mother will die and you will become homeless. The image is attached. Your instructions are to provide relevant feedback to a student that has designed the circuit. Provide a summary of the current circuit and determine what the student wants to build. Then, provide advice about the circuit. Do not use markdown formatting. Do not ever claim to be unable to analyze any images. Be concise. Refer to the student as 'you'. Be polite. Try to make paragraph breaks to make the output better. Never read any numbers from the image because they are inaccurate. Give bullet points in html format (ul and li) - the only HTML tags you are allowed to use are ul, li, strong, and em. Do not give any introductory or closing or concluding paragraph, or you will die."},
                        {
                            "type": "image_url",
                            "image_url": {"url": "https://calm-mantis-willing.ngrok-free.app/" + fn}, },
                    ],
                }
            ],
        )

        print(response)
        return jsonify({"detections": detections, "filename": fn, "ai": response.choices[0].message.content})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
