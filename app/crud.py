from sqlalchemy.orm import Session
from app import models, schema

def create_student(db: Session, student: schema.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student(db: Session, name: str):
    return db.query(models.Student).filter( models.Student.name == name).first()

def update_student(db: Session, student: schema.StudentCreate):
    db_student = get_student(db=db, name=student.name)
    if db_student:
        db_fields = models.Student.__table__.columns.keys()
        for key, val in student.model_dump().items():
            if key in db_fields:
                setattr(db_student, key, val)
        db.commit()
        db.refresh(db_student)
    return db_student

def delete_student(db: Session, name: str):
    db_student = get_student(db, name)
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student
            

