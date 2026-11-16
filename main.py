from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

import sqlite3

def get_connection():
    connection=sqlite3.connect(
        "students.db"
    )
    return connection
get_connection()

def create_table():
    connection= get_connection()
    cursor = connection.cursor()
    q = """
    create table If NOT EXISTS students (
        id integer primary key autoincrement,
        name text not null,
        age integer,
        gender text,
        marks integer,
        course text,
        image text,
        status integer
        )"""
    cursor.execute(q)   
    connection.commit()
    connection.close()
create_table()


templates = Jinja2Templates(
    directory="templates"
)

app = FastAPI()

@app.get("/")
def home(req:Request):
    connection=get_connection()
    cursor = connection.cursor()
    q = """select * from students"""
    cursor.execute(q)
    students = cursor.fetchall()
    cursor.close()
    
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"stds":students}
    )
       
    
@app.get("/student/{std_id}")
def single_std(req:Request,std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q ="""
    select * from students where id = ?"""
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()
    print(student)
    cursor.close()
    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={"stds":student}
    )

@app.post("/student/delete/{std_id}") 
def delete_std(std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q = """
    delete from students where id = ?
    """
    cursor.execute(q,(std_id,))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303)
    
         
    
    
@app.get("/students/add")
def add_std(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="add-student.html",
        context={}
    )
    
class DataValidation(BaseModel):
    name:str
    age:int
    gender:str
    marks:int
    course:str
    image:str
    status:int
    
@app.post("/students/add")
def create_form(
    name = Form(),
    age = Form(),
    gender = Form(), 
    marks = Form(),
    course = Form(),
    image = Form(),
    status = Form()
 ):
    std_obj=DataValidation(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image= image,
        status=status
    )
    values=(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,bool(std_obj.status))
    connection = get_connection()
    cursor= connection.cursor()
    q = """
    insert into students(name,age,gender,marks,course,image,status)
    values (?,?,?,?,?,?,?)
    """
    cursor.execute(q,values)   
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303)


@app.get("/update/std/{std_id}")
def update(req:Request,std_id):
    connection =get_connection()
    cursor = connection.cursor()
    q = """select * from students where id = ?"""
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()
    return templates.TemplateResponse(
        request=req,
        name="update-std.html",
        context={"std":student}
    )
    
    
        
class Students(BaseModel):
    
    name:str
    age:int
    gender:str
    marks:int
    course:str
    image:str
    status:int
    
@app.post("/update/std/{std_id}")
def update_std(
    std_id:int,
    name = Form(),
    age = Form(),
    gender = Form(), 
    marks = Form(),
    course = Form(),
    image = Form(),
    status = Form()
 ):
    std_obj=Students(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image= image,
        status=status
    )
    connection = get_connection()
    cursor= connection.cursor()
    q = """
    update students SET name=?,age=?,gender=?,marks=?,course=?,image=?,status=? WHERE id=?
    """
    cursor.execute(q,(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,bool(std_obj.status),std_id)) 
    connection.commit()
    connection.close()
    return RedirectResponse(url="/",status_code=303)
    
