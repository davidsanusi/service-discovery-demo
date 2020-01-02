from flask import Flask, render_template, request
import requests
app = Flask(__name__)

base_address = "http://backend.demo.lab" 
base_url=base_address

# base_address = "http://127.0.0.1:" 
# base_port="5001"
# base_url=base_address+base_port

@app.route('/api', methods=['post', 'get'])
def get_api():
    result = ''
    if request.method == 'POST':
        username = request.form.get('endpoint')  # access the data inside 
        print(username)# access the data inside 
        resp = requests.get(f'{base_url}/{username}') # access the data inside 
		
        if resp.status_code == 200:
            result = resp.json()
        else:
            result = "no such route"
 
    return render_template('index.html', message=result)