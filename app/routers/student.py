from fastapi import APIRouter, HTTPException, Depends
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app import schema, crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/students", response_model=schema.StudentOut)
def create(student: schema.StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

@router.get("/students", response_model=list[schema.StudentOut])
def get_all(db: Session = Depends(get_db)):  
    return crud.get_students(db)

@router.get("/students/name/{name}", response_model=schema.StudentOut)
def get_student(name: str, db: Session = Depends(get_db)):
    return crud.get_student(db, name)

@router.put("/students/name/{name}", response_model=schema.StudentOut)
def update_student(student: schema.StudentCreate, db: Session=Depends(get_db)):
    result = crud.update_student(db, student)
    if not result:
        raise HTTPException(404, "Student not found")
    return result

@router.delete("/students/by-name/{name}")
def delete(name: str, db: Session = Depends(get_db)):
    student = crud.delete_student(db, name)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Deleted"}