select *
from shop,book
where shop.shop# in (select sell.shop#
from sell
where sell.customer# in (select customer.customer#
from customer
where customer.name like N'محبی')) and book.shbq in (select sell.shbq
from sell
where sell.customer# in (select customer.customer#
from customer
where customer.name like N'محبی'))