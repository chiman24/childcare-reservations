# mongo_config.py
from mongoengine import connect

connect(
    db="jubilee_voices",
    host="mongodb://dbUser:xPC63amFP!k%24!n5X@cluster0-shard-00-01.szb1z.mongodb.net:27017/?tls=true"
)
