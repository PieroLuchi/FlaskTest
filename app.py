from flask import Flask, render_template, request
import requests
app = Flask(__name__)

# Sample list of names
# names = ["Hermada", "Checchi", "Maestri del Lavoro", "Comasina"]
# codes = ["HE","CE12","MDL4","CO87"]

names_with_codes = {
    "Hermada": "HE",
    "Checchi": "CE12",
    "Maestri del Lavoro": "MDL4",
    "Comasina": "CO87"
}
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        selected_name = request.form.get('name')
        action = request.form.get('action')
        code = names_with_codes.get(selected_name, "Unknown Code")

        if action == 'Activate':
            print(f"{selected_name} with code {code} activated ")
            requests.post(url=f'https://abitarefunctionapp.azurewebsites.net/api/AiEcoStateSelector?nome_edificio={code}&stato_attivazione=True')
        elif action == 'Deactivate':
            print(f"{selected_name} with code {code} deactivated")
            requests.post(url=f'https://abitarefunctionapp.azurewebsites.net/api/AiEcoStateSelector?nome_edificio={code}&stato_attivazione=False')
    
    return render_template('index.html', names=names_with_codes.keys())

if __name__ == '__main__':
    app.run(debug=True)