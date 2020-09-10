from flask import Flask
from flask import jsonify, request
import numbers
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

products = []
id = 0
errResponse = []
 
@app.route('/create/products', methods=['POST'])
def createProduct():
    if not request.json:
        return jsonify({
            "status" : "Error",
            "errors" : "No request found"
        }), 400
    
    for i in range(len(request.json)):
        if "product_name" not in request.json[i]:
            setError("product_name", "Product Name is required", i)
            
        if "quantity" not in request.json[i]:
            setError("quantity","Quantity is required", i)
        
        if "amount" not in request.json[i]:
            setError("amount", "Amount is required", i)
            
        if "rating" not in request.json[i]:
            setError("rating","Rating is required",i) 

    if len(errResponse) != 0:
        
        errRes =  jsonify({
            "status" : "Error",
            "errors" : errResponse
        })
        errResponse.clear()
        return errRes, 400
    else:
        global products
        global id
        for i in range(len(request.json)):
            task = {
                'id': products[-1]['id']+1 if len(products) != 0 else id + 1,
                'product_name': request.json[i]['product_name'],
                'quantity': request.json[i]['quantity'],
                'amount': request.json[i]['amount'],
                'rating': request.json[i]['rating']
            }
            products.append(task)
        return jsonify({'products': products}), 201

def setError(key, errMsg, index):
    global errResponse
    errResponse.append(str(errMsg) + " at index " + str(index))
    
@app.route('/list/products', methods=['GET'])
def getProducts():
    global products
    return jsonify({'products': products}), 200



app.run(debug = True)



