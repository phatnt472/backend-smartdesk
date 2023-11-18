from flask import Flask, request, render_template
import json
app = Flask(__name__)
# state = {
#     "data": ''
# }
data = '6789'

@app.route('/data', methods=['GET', 'POST'])
def get_data(): 
    raw = request.get_data()
    data = str(raw.decode())
    return data

# @app.route('/send_data', methods=['GET','POST'])
# def give_data():
#     print(">>>> /send_data: ",f'<h1>{state["data"]}</h1>')
#     return "hello 1"


@app.route('/')
def home():
    # return render_template('index.html', name=state["data"])
    return f'<h1>{data}</h1>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='6789')
