from flask import Flask, jsonify, request
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model

db = PostgresqlDatabase('songs', user='postgres', password='12345', host='localhost', port=5432)

class BaseModel(Model):
    class Meta:
        database = db

class Song(BaseModel):
    title = CharField(max_length=255)
    artist = CharField(max_length=255)
    key = CharField(max_length=3)
    tempo = IntegerField(max_length=3)
