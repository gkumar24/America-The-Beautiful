delete from import_weather_csv_will;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\acad.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'ACAD' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\arch.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'ARCH' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\badl.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'BADL' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\bisc.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'BISC' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\brca.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'BRCA' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\cany.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'CANY' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\care.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'CARE' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\cave.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'CAVE' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\cong.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'CONG' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\crla.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'CRLA' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\cuva.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'CUVA' where park_code is null;
COPY import_weather_csv_will(month,high,low,rain) FROM 'C:\DataVizUMN\Projects\Project2\America-The-Beautiful\collection\CleanWill\deva.csv' DELIMITER ',' CSV HEADER;
update public.import_weather_csv_will set park_code = 'DEVA' where park_code is null;
