select *  from youbike
where (updatetime,sna) IN (
select MAX(updatetime), sna
from youbike
where sarea = '士林區'
group by sna
)