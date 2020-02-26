update visitor_count_analysis
set park_name = n.park_name
from public.park_coordinates as n
where visitor_count_analysis.park_code = n.park_code