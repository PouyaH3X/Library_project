select shop# as کد_فروشگاه
from book inner join balance on book.shbq = balance.shbq
where author1 not like N'پیشرو'