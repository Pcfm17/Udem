SELECT * 
FROM 
    customer c, employee e1, employee e2
WHERE 
    c.support_rep_id=e1.employee_id
AND e1.reports_to=e2.employee_id;