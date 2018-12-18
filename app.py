from flask import Flask
from flask import jsonify,request
import pickle
import Mapping as mp

app = Flask(__name__)
	
@app.route("/predict",methods=['GET'])
def predict():
	type = mp.transform_type(request.args.get('type'))
	amount = float(request.args.get('amount'))
	old_bal_org = float(request.args.get('old_bal_org'))
	new_bal_org = float(request.args.get('new_bal_org'))
	name_dest = mp.transform_nameDest(request.args.get('name_dest'))
	old_bal_det = float(request.args.get('old_bal_det'))
	new_bal_det = float(request.args.get('new_bal_det'))
	
	trained_model = pickle.load(open('finalModel', 'rb'))
	result = trained_model.predict([[type,amount,old_bal_org,new_bal_org,name_dest,old_bal_det,new_bal_det]])
	if  result == 1:
		return "The Result of The Prediction: <b> Take Care !! This Transaction is Fraud </b>."
	else:
		return "The Result of The Prediction: <b>Good !! This Transaction is not Fraud </b>."
	
	
if __name__ == '__main__':
    app.run(port = 9000, debug = True)	