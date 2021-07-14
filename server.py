from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def check_server():
    return render_template('index.html')

@app.route('/4')
def rows():
    return render_template('index2.html')

@app.route('/<x>/<y>')
def tens(x,y):
    input1=int(x)
    input2= int(y)
    return render_template('index3.html',input1=input1,input2=input2)

if __name__ == '__main__':
    app.run(debug=True)




