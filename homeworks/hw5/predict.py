import pickle
from flask import Flask
from flask import request
from flask import jsonify

dv_file = 'dv.bin'
model_file = 'model1.bin'
with open(dv_file,'rb') as f_in:
    dv = pickle.load(f_in)
with open(model_file,'rb') as f_in:
    model = pickle.load(f_in)

app = Flask('get_credit')
@app.route('/predict',methods=['POST'])
def predict():
    client = request.get_json()
    X = dv.transform([client])
    p = model.predict_proba(X)[0,1]
    status = p >= 0.5
    result = {
        "status":bool(status),
        "probability":float(p)
    }
    return jsonify(result)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=9696)