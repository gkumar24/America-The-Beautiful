select *, cast(rain as double precision) from  public.import_weather_csv

select V.*, W.* from visitor_count_analysis as V
inner join import_weather_csv as W
on V.park_code = W.park_code and V.month = cast(W.month as integer)
order by V.park_code, V.month;

update visitor_count_analysis
set high = cast(import_weather_csv.high as double precision),
	low = cast(import_weather_csv.low as double precision),
	rain = cast(import_weather_csv.rain as double precision)
from import_weather_csv
where visitor_count_analysis.park_code = import_weather_csv.park_code 
	and visitor_count_analysis.month = cast(import_weather_csv.month as integer);



