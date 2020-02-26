SELECT *
	FROM public.import_weather_csv_will where month_num is null

update visitor_count_analysis
set high = cast(W.high as double precision),
low = cast(W.low as double precision),
rain = cast(W.rain as double precision)
from import_weather_csv_will as W
where visitor_count_analysis.park_code = W.park_code 
and visitor_count_analysis.month = cast(W.month_num as integer)
	
select V.*, W.* from visitor_count_analysis as V
inner join import_weather_csv_will as W
on V.park_code = W.park_code and V.month = cast(W.month_num as integer)
order by V.park_code, V.month;