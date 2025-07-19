select *
from book
where book.shbq not in (SELECT sell.shbq
FROM sell 
WHERE NOT (sell.fac_date > format(DATEADD(month, 0, GETDATE()) , 'yyyy-MM-dd', 'fa-ir' )OR sell.fac_date <format(DATEADD(month, -3, GETDATE()) , 'yyyy-MM-dd', 'fa-ir')))