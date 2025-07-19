select employe.n_id as کد_ملی,employe.name as نام, employe.phone تلفن, employe.adress آدرس, employe.sex جنسیت 
from employe inner join shop on employe.shop#=shop.shop#
where shop.shop#=2545