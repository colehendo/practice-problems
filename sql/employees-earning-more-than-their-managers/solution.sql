select worker.name as Employee
from Employee as worker
left join Employee as manager
on worker.managerId = manager.id
where worker.salary > manager.salary;