from flask import Flask, request
from flask import render_template
from forms import MyForm

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def hello():
    form = MyForm(request.form)
    input_text = ''
    formatted = ''
    sub_str = ''
    if request.method == 'POST':
        if form.validate():
            input_text = request.form['text']
            start = request.form['start']
            end = request.form['end']

            if int(start) < len(input_text) and int(end) < len(input_text) and int(start) > int(end):
                sub_str = input_text[int(start):int(end)]
            else:
                sub_str = 'invalid start/end index!'
    else:
        form = MyForm()

    return render_template('index.html', form = form, input_text = input_text, substr = sub_str)

if __name__ == '__main__':
    app.run(debug = True)