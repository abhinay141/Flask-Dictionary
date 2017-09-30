from flask import Flask,render_template,request
from PyDictionary import PyDictionary
from flask import jsonify
dictionary = PyDictionary()
app = Flask('__name__')
@app.route('/')
def page():
    return render_template('word.html')
@app.route('/send',methods=['GET'])
def meaning():
    word = request.args.get('word')
    dicti=dictionary.meaning(word)
    return jsonify(result=dicti)
if __name__ == '__main__':
    app.run(debug=True)
