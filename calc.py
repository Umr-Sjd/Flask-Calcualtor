from flask import Flask, render_template, request

app = Flask(__name__)  # Start the app

@app.route('/')  # When someone visits the main page
def home():
    return render_template('calculator.html')  # Show the web page

@app.route('/calculate', methods=['POST'])  # When the user clicks "="
def calculate():
    try:
        expression = request.form['expression']  # Get what the user typed
        result = str(eval(expression))           # Solve it
    except:
        result = 'Error'                         # If something goes wrong
    return render_template('calculator.html', result=result)  # Show the page with the result

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")  # Start the website
