from sqlalchemy.orm import Session
import models, schemas


def get_employees(db: Session): # what is session? it is a handle to the database, we can use it to query the database
    return db.query(models.Employee).all()


def get_employee(db: Session, emp_id: int): # these are converted to sql queries by sqlalchemy
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )


def create_employee(db: Session, employee: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name=employee.name, email=employee.email
    )
    db.add(db_employee)
    db.commit()        # to save the changes to the database, we need to commit, as autocommit is set to False
    db.refresh(db_employee)  # to get the updated instance with the id assigned by the database
    return db_employee


def update_employee(db: Session, emp_id: int, employee: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email = employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee