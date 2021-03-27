from flask import Flask, request, Response
from db_manager import DB_Manager


app = Flask(__name__)
db = DB_Manager()

def verify_token(token):
    pass

@app.route('/')
def default():
    return 'this is the backend for the screening app'

@app.route('/register', methods=['POST'])
def submit_reg():
    token = request.form['token']
    if not verify_token(token):
        return Response(status=401)
    reg = request.form
    reg_info = {}

    if 'first_name' not in reg:
        return Response(status=400)
    reg_info['first-name'] = reg['first-name']

    if 'last-name' not in reg:
        return Response(status=400)
    reg_info['last-name'] = reg['last-name']

    if 'birth-date' in reg:
        reg_info['birth-date'] = reg['birth-date']
    else:
        reg_info['birth-date'] = None
    
    if 'age' in reg:
        reg_info['age'] = reg['age']
    else:
        reg_info['age'] = None
    
    if 'school-name' in reg:
        reg_info['school-name'] = reg['school-name']
    else:
        reg_info['school-name'] = None
    
    if 'standard' in reg:
        reg_info['standard'] = reg['standard']
    else:
        reg_info['standard'] = None
    
    if 'village' in reg:
        reg_info['village'] = reg['village']
    else:
        reg_info['village'] = None
    
    if 'sub-county' in reg:
        reg_info['sub-county'] = reg['sub-county']
    else:
        reg_info['sub-county'] = None
    
    if 'church' in reg:
        reg_info['church'] = reg['church']
    else:
        reg_info['church'] = None
    
    if 'childrens-Home' in reg:
        reg_info['childrens-Home'] = reg['childrens-Home']
    else:
        reg_info['childrens-Home'] = None
    
    if 'care-taker' in reg:
        reg_info['care-taker'] = reg['care-taker']
    else:
        reg_info['care-taker'] = None
    
    if 'father' in reg:
        reg_info['father'] = reg['father']
    else:
        reg_info['father'] = None
    
    if 'mother' in reg:
        reg_info['mother'] = reg['mother']
    else:
        reg_info['mother'] = None
    
    if 'care-taker-phone' in reg:
        reg_info['care-taker-phone'] = reg['care-taker-phone']
    else:
        reg_info['care-taker-phone'] = None
    
    if 'alternate-phone' in reg:
        reg_info['alternate-phone'] = reg['alternate-phone']
    else:
        reg_info['alternate-phone'] = None

    
    



def login():
    return Response(status=501)

def screening1():
    return Response(status=501)

def screening2():
    return Response(status=501)

def find_patient():
    return Response(status=501)



