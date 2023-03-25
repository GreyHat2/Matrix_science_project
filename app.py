from flask import Flask, render_template, request, url_for
import matrix
import numpy as np

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/decrypt_page')
def decrypt_page():
    return render_template('decrypt.html')

@app.route('/encrypt_message', methods=['GET', 'POST'])
def encrypt_msg():
    if request.method == 'POST':
        input_string = request.form['text']
        password = request.form['password']

        a, b, c, d = map(int, (password).split(","))
        encoding_matrix = np.array([[a, b], [c, d]])
        encrypted_values = matrix.encrypt(input_string, encoding_matrix)
        return render_template('index.html', data="Your encrypted data is: "+str(encrypted_values), data2 ="Your password is: "+str(password))
    else:
        return "Failed"

@app.route('/decrypt_message', methods=['GET', 'POST'])
def decrypt_message():
    if request.method == 'POST':
        text = request.form['encrypted_text']
        encoding_matrix_password = request.form['password']

        a, b, c, d = map(int, (encoding_matrix_password).split(","))
        encoding_matrix = np.array([[a, b], [c, d]])
        encrypted_values = list(map(int, (text).split(",")))
        decrypted_string = matrix.decrypt(encrypted_values, encoding_matrix)

        return render_template('decrypt.html', data="Your decrypted data is: "+decrypted_string)
    else:
        return "Failed"


if __name__ == '__main__':
    app.run()