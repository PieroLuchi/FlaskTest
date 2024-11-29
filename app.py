from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
    # This function will be called when the button is pressed
    data = request.form['data']  # Retrieve data from the form
    
    print(f"Received data: {data}")  # Process the data as needed
    return "Data received!"

if __name__ == '__main__':
    app.run(debug=True)