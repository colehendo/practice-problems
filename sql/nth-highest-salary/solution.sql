create function getNthHighestSalary(n int) returns int
begin
set n = n - 1;
  return (
    select salary
    from Employee
    order by salary desc
    limit 1 offset n
  );
end