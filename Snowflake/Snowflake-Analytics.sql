use database PROJECT1;

-- 1. Updating the store table so that the opening data is on or after 2014

select * from dimstore limit 10;

select datediff(day,current_date(),'2014-01-01'); --4384

select dateadd(day,uniform(0,4384,random()),'2014-01-01');

update dimstore
set storeopeningdate =dateadd(day,uniform(0,4384,random()),'2014-01-01');

--2 update storedate for ids bwn 90-100 only shows date in last yr

select dateadd(day, uniform(0,365,random()),'2024-01-01');

update dimstore
set storeopeningdate = dateadd(day,uniform(0,365,random()),'2024-01-01')
where storeid between 90 and 100;

select * from dimstore limit 10 offset 89;


--3 List customers who did not place orders in 30days
select * from factorders limit 10;
select * from dimcustomer limit 10;
select * from dimdate limit 10;

select customerid from dimcustomer where customerid not in(  select d.customerid from dimcustomer d
join factorders d1
on d.customerid =d1.customerid
join dimdate d2
on d1.dateid = d2.dateid
where d2.date >= dateadd(month,-1,'2024-02-01'));


--4 list the store which is opened most recently along with its sale

with lateststoredate as(select storeid,storename,storeopeningdate, row_number() over (order by storeopeningdate desc) rn from dimstore),

final as(select * from lateststoredate where rn=1)

select f.storeid,sum(totalamount) from factorders f join
final d on f.STOREID = d.storeid
group by f.STOREID;

--5 monthly sales for current year
select * from factorders limit 10;

select month,sum(totalamount) as sum from factorders d1
join dimdate d2
on d1.dateid= d2.dateid
where d2.year = '2024'
group by month
order by month asc;










