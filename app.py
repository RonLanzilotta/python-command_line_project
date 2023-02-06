from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('songs', user='postgres', password='12345', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Songs(BaseModel):
    title = CharField()
    artist = CharField()
    key = CharField()
    tempo = IntegerField()

db.connect()
db.drop_tables([Songs])
db.create_tables([Songs])

Songs(title='Crazy In Love', artist='Beyoncé', key='D-', tempo=100).save()
Songs(title='Watermelon Sugar', artist='Harry Styles', key='C', tempo=95).save()
Songs(title='How Deep Is Your Love', artist='Bee Gees', key='Eb', tempo=105).save()

# app = Flask(__name__)

# app.run(debug=True, port=3333)

def session():

    def add():

        title = input("Please enter title of song")
        artist = input("Please enter artist")
        key = input("Please enter key of song")
        tempo = input("Please enter tempo of song")

        new_song = dict_to_model(Songs, request.get_json())
        new_song.save()
        return jsonify({"success": True})

    print("Welcome to the Song Archive.\n"
    "\n"
    "Enter ADD to add a new song\n"
    "\n"
    "Enter the song's title if you'd like to see song details\n"
    "\n"
    "Enter DELETE + title if you'd like to delete a song\n"
    "\n"
    "Enter UPDATE + song title if you need to change some details of an entry\n"
    )
    print()
    user_input = input("------->")

    if user_input.lower() == 'add':
        add()
    elif user_input.lower() == Songs.title:
        print(Songs)
    elif user_input.lower() == f"delete {Songs.title}":
        print('DELETE WORKS')
    elif user_input.lower() == f"update {Songs.title}":
        print('UPDATE WORKS')
    else:
        print("Please only enter one of the options above")


session()

# @app.route('/songs/', methods=['GET', 'POST'])
# @app.route('/songs/<id>', methods=['GET', 'PUT', 'DELETE'])
# def endpoint(id=None):
#     if request.method == 'GET':
#         if id:
#             return jsonify(model_to_dict(Songs.get(Songs.id == id)))
#         else:
#             songs_list = []
#             for song in Songs.select():
#                 songs_list.append(model_to_dict(song))
#             return jsonify(songs_list)

#     if request.method == 'PUT':
#         body = request.get_json()
#         Songs.update(body).where(Songs.id == id).execute()
#         return "Song " + str(song.title) + " has been updated."

#     if request.method == 'POST':
#         new_song = dict_to_model(Songs, request.get_json())
#         new_song.save()
#         return jsonify({"success": True})

#     if request.method == 'DELETE':
#         Songs.delete().where(Songs.id == id).execute()
#         return "Song " + str(song.title) + " deleted."









