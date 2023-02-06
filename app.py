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


    print("\n"
    "Welcome to the Song Archive.\n"
    "\n"
    "Enter ADD to add a new song\n"
    "\n"
    "Enter GET and then the song's title if you'd like to see song details\n"
    "\n"
    "Enter DELETE + title if you'd like to delete a song\n"
    "\n"
    "Enter UPDATE + song title if you need to change some details of an entry\n"
    )
    user_input = input("------->  ")

    # print(user_input.lower())
    # song = Songs.get(Songs.title == user_input)
    # print(song.title)

    if user_input.lower() == 'add':
        add()
    elif user_input.lower() == "delete":
        search = input("Which song would you like to delete?")
        Songs.delete().where(Songs.title == search).execute()
        
        print(f"{search} was deleted.")

    elif user_input.lower() == f"update {Songs.title}":
        print('UPDATE WORKS')

    elif user_input.lower() == 'get':
        search = input("Enter the title of the song you want to see. ")
        song = Songs.get(Songs.title == search)
        print(
            f"TITLE: {song.title}\n"
            f"ARTIST: {song.artist}\n"
            f"KEY: {song.key}\n"
            f"TEMPO: {song.tempo}\n")

    else:
        print("Please only enter one of the options above")


session()