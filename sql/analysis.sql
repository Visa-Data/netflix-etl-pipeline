--count shows by country
select country,count(*) as show_count
from netflix_shows
group by country
order by show_count desc;


--count shows by rating
select rating,count(*) as count
from netflix_shows
group by rating;
