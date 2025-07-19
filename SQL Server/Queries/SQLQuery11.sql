select *
from shop
where shop.shop# in

(select balance.shop#
from balance
where balance.av_no<balance.lim_no and balance.shbq in

(select book.shbq
from book
where book.title like N'اقتصاد خرد'))