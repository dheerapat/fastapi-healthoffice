from fastapi import FastAPI, Form
from pydantic import BaseModel
import sqlite3

connect = sqlite3.connect(':memory:')
cursor = connect.cursor()

cursor.execute('CREATE TABLE office(id, name, sub)')

class Provider(BaseModel):
    id: str
    name: str
    sub: str

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/add/")
async def add_healthcare(id: str = Form(), name: str = Form(), sub: str = Form()):
    cursor.execute("INSERT INTO office VALUES(?, ?, ?)", (id, name, sub))
    connect.commit()
    return {"message": "Insert data successfully"}

@app.get("/view/")
async def viewdata():
    data = cursor.execute("SELECT * FROM office")
    return data.fetchall()