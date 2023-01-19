select Department.name as Department, Employee.name as Employee, Employee.salary as Salary
from Employee
left join Department
on Employee.departmentId = Department.id
where (Employee.departmentId, Employee.salary) in (
    select Employee.departmentId, max(Employee.salary)
    from Employee
    group by Employee.departmentId
)