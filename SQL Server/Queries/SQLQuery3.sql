SELECT sum((cast(book.price AS int))*sell.count1) as مجموع_فروش
FROM sell inner join book on sell.shbq = book.shbq
WHERE NOT (sell.fac_date > '1388-10-15' OR sell.fac_date < '1388-10-10') AND sell.shop# = '4545';