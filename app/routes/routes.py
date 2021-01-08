from app import app, db
from flask import jsonify, request, Response, abort
from app.tools import Tools
from app.send_mail import send_email
from bson import ObjectId
import jwt
import datetime


tools = Tools()

## banco de dados, criando coleções/trabelas ##
dbAdministradores = db['administradores']
dbEdicoes = db['edicoes']
dbPaginas = db['paginas']

@app.route('/administradores', methods=['GET'])
def admin_get():
    '''
    Retornar lista de administradores cadastrados no banco de dados
    '''
    admins = dbAdministradores.find({}, {'password':0})
    listar_admins = []
    for admin in admins:
        admin['_id'] = str(admin['_id'])
        listar_admins.append(admin)
    return jsonify(listar_admins)

@app.route('/administradores',methods=['post'])
def admin_post():
    '''
    Atualizar dados de um usuario especifico no banco de dados
    '''
    dados = request.form 
    try:
        name, email = dados['name'], dados['email']
    except KeyError:
        return jsonify({"error": "Dados inválidos"}), 400

    if tools.check_exist_db(email):
        newdict = {"$set":{
            'name': name
        }}

        dicio = {
            'email': email
        }

        updated = dbAdministradores.update_one(dicio, newdict)
        return jsonify({'sucess': 'Usuario atualizado'})
    else:
        return jsonify({'error': 'email não encontrado'}), 404

@app.route('/administradores',methods=['put'])
def admin_put():
    '''
        Criando usuario no banco de dados administradores
    '''
    dados = request.form
    try:# Válidação dos dados
        name, email, password = dados['name'], dados['email'], dados['password']
    except KeyError:
        return jsonify({'error': 'Dados Inválidos'}), 400
    if not tools.check_exist_db('a',email):
        dicio = {
            'name': dados['name'],
            'email': dados['email'],
            'password': tools.generate_password_hash(dados['password'])
        }
        
        inserted = dbAdministradores.insert_one(dicio)
        return jsonify({"sucess": "Usuario cadastrado"}), 201
    else:
        return jsonify({'error': 'Email já cadastrado'}), 400

@app.route('/administradores',methods=['delete'])
def admin_delete():

    '''
    Apagando um usuario do banco de dados administradores
    '''
    dados = request.form    
    try:
        id = dados['id']
    except KeyError:
        return jsonify({'error': 'Dados Inváidos'}), 400

    if tools.check_exist_db(id):
        deleted = dbAdministradores.delete_one({'_id': ObjectId(id)})
        return jsonify({"sucess": "Usuario deletado!"})
    else:
        return jsonify({'error': 'id informado não encontrado'}), 404

@app.route('/login', methods=['post'])
def login():
    '''
    Verificando usuario e senha
    '''
    dados = request.form
    try:
        email, password = dados['email'], dados['password']
    except KeyError:
        return jsonify({'error': 'Dados Inválidos'}), 400

    user = dbAdministradores.find_one({'email': email})
    if user and tools.check_password_hash(user['password'], password ):
        return jsonify({'name': user['name'], 'email': user['email']}), 200
    else:
        return abort(401)

@app.route('/edicoes', methods=['get'] )
def edicoes_get():
    '''
    Retornar lista de edições cadastrados no banco de dados
    '''
    edicoes = dbEdicoes.find({})
    listar_edicoes = []
    for edicao in edicoes:
        edicao['_id'] = str(edicao['_id'])
        listar_edicoes.append(edicao)

    return jsonify(listar_edicoes)

@app.route('/edicoes', methods=['post'] )
def edicoes_post():
    '''
    Editar edições no banco de dados
    '''
    dados = request.form
    try:
        id, name, assets, about, music, start_date, end_date, status = daods['id'], dados['name'], dados['assets'], dados['about'], dados['music'], dados['start_date'], dados['end_date'], dados['status']
    except:
        return jsonify({'error': 'dados inválidos'}), 400
    
    newdict = {
        "$set": {
            'name': name,
            'assets': assets,
            'about': about,
            'music': music,
            'start_date': start_date,
            'end_date': end_date,
            'status':status
        }
    }

    dicio = {
        '_id': ObjectId(id)
    }

    updated = dbEdicoes.update_one(dicio, newdict)

    if updated.modified_count > 0:
        return jsonify({'success': 'edição atualizado'})
    else: 
        return jsonify({'error': 'id não encontrado'})

@app.route('/edicoes', methods=['put'] )
def edicoes_put():
    '''
    Criando edição no banco de dados
    '''
    dados = request.form
    try:
        name, assets, about, music, start_date, end_date, status = dados['name'], dados['assets'], dados['about'], dados['music'], dados['start_date'], dados['end_date'], dados['status']
    except KeyError:
        return jsonify({'error': 'dados inválidos'}), 400
    
    dicio = {
        'name': name,
        'assets': assets,
        'about': about,
        'music': music,
        'start_date': start_date,
        'end_date': end_date,
        'status': status
    }

    inserted = dbEdicoes.insert_one(dicio)
    return jsonify({"success" : "edição criada"}), 201

@app.route('/edicoes', methods=['delete'] )
def edicoes_delete():
    '''
    Removendo edições no banco de daods
    '''
    dados = request.form

    try:
        id = dados['id']
    except KeyError:
        return jsonify({"error": "dados inválidos"}), 400

    deleted = dbEdicoes.delete_one({"_id": ObjectId(id)})
    if deleted.deleted_count > 0:
        return jsonify({'success': 'edição deleta com sucesso'})
    else:
        return jsonify({'error': 'id não encontrado'}), 404

@app.route('/pg/sobre')
def sobre_info():
    p = dbPaginas.find_one({'_id': 'sobre'})

    return jsonify({
        'sobre': p['sobre'],
        'ciclo': p['ciclo'],
        'acoes': p['acoes']
    })

@app.route('/admin/esqueci-senha')
def esqueci_senha():
    email = request.args.get('email')
    token = request.args.get('token')
    if email:

        payload_token = {
            "email": email,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        }
        g_token = jwt.encode(payload_token, app.config['SECRET_KEY'], algorithm="HS256")
        send = send_email([email], g_token)
        return jsonify({'info': send})
    elif token:
        pass
    return 'oi'


