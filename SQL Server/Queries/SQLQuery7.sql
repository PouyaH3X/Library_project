select sum(customer.dept) مجموع_بدهی_به_انتشارات_آیلار
from customer
where customer.customer# in (select sell.customer#
from sell
where sell.shbq in (select book.shbq
from book
where book.publisher like N'آیلار'))