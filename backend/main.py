from flask import Flask, jsonify, request
from flask_cors import CORS
import json

from usuarios import Usuarios
from publication import Publication

users = []

users.append(Usuarios("Abner Cardona","Masculino","admin","admin@ipc1.com","admin@ipc1"))

post = []

contador_publicaciones = 3;


app = Flask(__name__)
CORS(app)


@app.route('/')
def prueba():
    objeto = {
        "string": "Hola",
        "letras": "4"
    }
    return jsonify(objeto)


@app.route('/ingresar', methods=['GET'])
def ingresar():
    label = {
        "string": "Ingrese su nombre de usuario"
    }

    return jsonify(label)

@app.route('/users', methods=['GET'])
def mostrarusers():
    global users
    datosusers = []
    for Usuarios in users:
        json = {
            "name": Usuarios.getname(),
            "gender": Usuarios.getgender(),
            "username": Usuarios.getusername(),
            "email": Usuarios.getemail(),
            "password": Usuarios.getpassword()
        }
        datosusers.append(json)
    return(jsonify(datosusers))


@app.route('/users/<string:username>', methods=['GET'])
def mostrar_unuser(username):
    global users
    for Usuarios in users:
        if Usuarios.getusername() == username:
            json = {
                "name": Usuarios.getname(),
                "gender": Usuarios.getgender(),
                "username": Usuarios.getusername(),
                "email": Usuarios.getemail(),
                "password": Usuarios.getpassword()
            }
            return(jsonify(json))
    Error  = {"Error": "No se ha encontrado al usuario solicitado"}
    return(jsonify(Error))


@app.route('/users/<string:username>', methods=['PUT'])
def modificar_users(username):
    global users
    for Usuarios in users:
        if Usuarios.getusername() == username:
            json={
                "name": Usuarios.setname(request.json['name']),
                "gender": Usuarios.setgender(request.json['gender']),
                "username": Usuarios.setusername(request.json['username']),
                "email": Usuarios.setemail(request.json['email']),
                "password": Usuarios.setpassword(request.json['password'])
            }
            exito = {"Mensaje": "Se ha actualizado correctamente al usuario"}
            return (jsonify(exito))
    Error = {"Error": "No se ha podido actualizar al usuario, es probable que no exista"}
    return(jsonify(Error))


@app.route('/users', methods=['POST'])
def crear_usuario():
    global users
    name = request.json['name']
    gender = request.json['gender']
    username = request.json['username']
    email = request.json['email'] 
    password = request.json['password']

    usuario_nuevo = Usuarios(name,gender,username,email,password)
    users.append(usuario_nuevo)
    mensaje = {"Mensaje": "El usuario se ha creado exitosamente"}
    return(jsonify(mensaje))


@app.route('/users/<string:username>', methods=['DELETE'])
def eliminar_usuario(username):
    global users
    for i in range(len(users)):
        if username == users[i].getusername():
            del users[i]
            mensaje = {"Mensaje": "Se ha eliminado el usuario correctamente"}
            return(jsonify(mensaje))
    
    Error = {"Error": "No se ha podido eliminar el usuario, posiblemente no exista"}
    return(jsonify(Error))


@app.route('/publications', methods=['GET'])
def mostrar_posts():
    global post
    datospost = []
    for Publication in post:
        json = {
            "type": Publication.gettype(),
            "url": Publication.geturl(),
            "date": Publication.getdate(),
            "category": Publication.getcategory(),
            "author": Publication.getauthor(),
            "likes": Publication.getlikes(),
            "id": Publication.getid()
        }
        datospost.append(json)

    return(jsonify(datospost))


@app.route('/publications', methods=['POST'])
def crear_post():
    global post
    global contador_publicaciones
    type = request.json['type']
    url = request.json['url']
    date = request.json['date']
    category = request.json['category']
    author = request.json['author']
    contador_publicaciones = contador_publicaciones + 1
    id = contador_publicaciones

    post_nuevo = Publication(type,url,date,category,author,0,id)
    post.append(post_nuevo)
    mensaje = {"Mensaje": "La publicación se ha creado con exito"}
    return(jsonify(mensaje))

@app.route('/publications/<string:author>', methods=['GET'])
def ver_publicacion_author(author):
    global post
    datos = []
    for Publication in post:
        if Publication.getauthor() == author:
            json = {
                "type": Publication.gettype(),
                "url": Publication.geturl(),
                "date": Publication.getdate(),
                "category": Publication.getcategory(),
                "author": Publication.getauthor(),
                "likes": Publication.getlikes(),
                "id": Publication.getid()
            }
            datos.append(json)
    return(jsonify(datos))



@app.route('/publications/<int:id>', methods=['GET'])
def ver_publicacion(id):
    global post
    for Publication in post:
        if Publication.getid() == id:
            json = {
                "type": Publication.gettype(),
                "url": Publication.geturl(),
                "date": Publication.getdate(),
                "category": Publication.getcategory(),
                "author": Publication.getauthor(),
                "likes": Publication.getlikes(),
                "id": Publication.getid()
            }
            return(jsonify(json))
    Error  = {"Error": "No se ha encontrado al usuario solicitado"}
    return(jsonify(Error))

@app.route('/publications/<int:id>', methods=['PUT'])
def actualizar_like(id):
    global post
    for Publication in post:
        if Publication.getid() == id:
            likes = Publication.getlikes()
            likes = likes + 1
            Publication.setlikes(likes)
            
            exito = {"Mensaje": "Se ha actualizado los likes"}
            return (jsonify(exito))
    Error = {"Error": "No se ha actualizado nada"}
    return(jsonify(Error))

@app.route('/quitarlike/<int:id>', methods=['PUT'])
def quitar_like(id):
    global post
    for Publication in post:
        if Publication.getid() == id:
            likes = Publication.getlikes()
            likes = likes - 1
            Publication.setlikes(likes)
            
            exito = {"Mensaje": "Se ha actualizado los likes"}
            return (jsonify(exito))
    Error = {"Error": "No se ha actualizado nada"}
    return(jsonify(Error))


@app.route('/publications/<int:id>', methods=['DELETE'])
def eliminar_publicacion(id):
    global post
    for i in range(len(post)):
        if id == post[i].getid():
            del post[i]
            mensaje = {"Mensaje": "Se ha eliminado la publicacion correctamente"}
            return(jsonify(mensaje))




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 4000,debug = True)