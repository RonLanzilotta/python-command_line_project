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

#seeds info into SQL db
Songs(title='Crazy In Love', artist='Beyoncé', key='D-', tempo=100).save()
Songs(title='Watermelon Sugar', artist='Harry Styles', key='C', tempo=95).save()
Songs(title='How Deep Is Your Love', artist='Bee Gees', key='Eb', tempo=105).save()

# starts a new user session and loads instructions
def session():

    # defines ADD functionality
    def add():
        
        # sets each user input to a variable that corresponds with song entry info
        title = input("Please enter title of song  ")
        artist = input("Please enter artist  ")
        key = input("Please enter key of song  ")
        tempo = input("Please enter tempo of song  ")

        #
        song_entry = Songs(title = title, artist = artist, key = key, tempo = tempo)
        song_entry.save()
        print(f"'{title}' was added to the database!  ")


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
    user_input = input("------->  ")

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