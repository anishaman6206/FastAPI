from fastapi import FastAPI, HTTPException
from models import Employee
from typing import List

# variable_name: data_type = value
employees_db: List[Employee] = []

app = FastAPI() 

# 1. Read all employees
@app.get("/employees", response_model=List[Employee]) # list of Employee objects will be returned as JSON
def read_employees():
    return employees_db

# 2. Read specific employee by ID
@app.get("/employees/{employee_id}", response_model=Employee) 
def get_employee(employee_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail="Employee not found")


# 3. Add a new employee
@app.post("/add_employee", response_model=Employee)
def add_employee(new_employee: Employee):
    # Check if employee with the same ID already exists
    for emp in employees_db:
        if emp.id == new_employee.id:
            raise HTTPException(status_code=400, detail="Employee with this ID already exists")
    employees_db.append(new_employee)
    return new_employee


# 4. Update an existing employee
@app.put("/update_employee/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee not found")


# 5. Delete an employee
@app.delete("/delete_employee/{employee_id}")
def delete_employee(employee_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == employee_id:
            del employees_db[index]
            return {"message": "Employee deleted successfully"}
    raise HTTPException(status_code=404, detail="Employee not found")
