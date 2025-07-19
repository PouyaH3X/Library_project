select *
from sell inner join employe on sell.shop# = employe.shop#
where employe.name like N'ناصری' and sell.emp# = employe.n_id 