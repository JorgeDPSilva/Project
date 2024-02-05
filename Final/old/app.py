from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def acordaos():
    with open('datasets/atco1_acordaos.json', 'r',encoding='utf-8') as f:
        dados = json.load(f)
    return render_template('acordaos.html', dados=dados)

if __name__=="__main__":
    app.run(debug=True)





