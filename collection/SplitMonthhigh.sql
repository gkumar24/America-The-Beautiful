SELECT monthhigh, replace(monthhigh,'July','') high, '07' as month 
FROM public.import_weather_csv
where monthhigh like 'July%';

select * from  public.import_weather_csv order by park_code,month

/*
alter table import_weather_csv add high character varying(50);
alter table import_weather_csv add month character varying(50);
*/
/*
update  public.import_weather_csv
set high = replace(monthhigh,'July',''),
	month = '07'
where monthhigh like 'July%';
*/
/*
update  public.import_weather_csv set high = replace(monthhigh,'January',''), month = '1' where monthhigh like 'January%';
update  public.import_weather_csv set high = replace(monthhigh,'February',''), month = '2' where monthhigh like 'February%';
update  public.import_weather_csv set high = replace(monthhigh,'March',''), month = '3' where monthhigh like 'March%';
update  public.import_weather_csv set high = replace(monthhigh,'April',''), month = '4' where monthhigh like 'April%';
update  public.import_weather_csv set high = replace(monthhigh,'May',''), month = '5' where monthhigh like 'May%';
update  public.import_weather_csv set high = replace(monthhigh,'June',''), month = '6' where monthhigh like 'June%';
update  public.import_weather_csv set high = replace(monthhigh,'July',''), month = '7' where monthhigh like 'July%';
update  public.import_weather_csv set high = replace(monthhigh,'August',''), month = '8' where monthhigh like 'August%';
update  public.import_weather_csv set high = replace(monthhigh,'September',''), month = '9' where monthhigh like 'September%';
update  public.import_weather_csv set high = replace(monthhigh,'October',''), month = '10' where monthhigh like 'October%';
update  public.import_weather_csv set high = replace(monthhigh,'November',''), month = '11' where monthhigh like 'November%';
update  public.import_weather_csv set high = replace(monthhigh,'December',''), month = '12' where monthhigh like 'December%';
*/