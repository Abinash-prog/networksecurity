
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://mishraabinash118:Abinash9348@cluster0.5pea3vp.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri,server_api=ServerApi('1') )

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)