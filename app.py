from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = ''
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi <= 24.9:
            category = 'Normal weight'
        elif 25 <= bmi <= 29.9:
            category = 'Overweight'
        elif 30 <= bmi <= 34.9:
            category = 'Obesity Class 1'
        elif 35 <= bmi <= 39.9:
            category = 'Obesity Class 2'
        else:
            category = 'Obesity Class 3 (Extreme or Severe)'

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
