-- View: public.visitor_average

-- DROP VIEW public.visitor_average;

CREATE OR REPLACE VIEW public.visitor_average
 AS
 SELECT v.park_code,
    v.avg_jan,
    v.avg_feb,
    v.avg_mar,
    v.avg_apr,
    v.avg_may,
    v.avg_jun,
    v.avg_jul,
    v.avg_aug,
    v.avg_sep,
    v.avg_oct,
    v.avg_nov,
    v.avg_dec,
    (v.avg_jan + v.avg_feb + v.avg_mar + v.avg_apr + v.avg_may + v.avg_jun + v.avg_jul + v.avg_aug + v.avg_sep + v.avg_oct + v.avg_nov + v.avg_dec) / 12 AS avg_monthly,
    GREATEST(v.avg_jan, v.avg_feb, v.avg_mar, v.avg_apr, v.avg_may, v.avg_jun, v.avg_jul, v.avg_aug, v.avg_sep, v.avg_oct, v.avg_nov, v.avg_dec) AS great_month
   FROM ( SELECT visitor_count.park_code,
            (sum(visitor_count.jan) / count(NULLIF(visitor_count.jan, 0))::numeric)::integer AS avg_jan,
            (sum(visitor_count.feb) / count(NULLIF(visitor_count.feb, 0::double precision))::double precision)::integer AS avg_feb,
            (sum(visitor_count.mar) / count(NULLIF(visitor_count.mar, 0::double precision))::double precision)::integer AS avg_mar,
            (sum(visitor_count.apr) / count(NULLIF(visitor_count.apr, 0::double precision))::double precision)::integer AS avg_apr,
            (sum(visitor_count.may) / count(NULLIF(visitor_count.may, 0::double precision))::double precision)::integer AS avg_may,
            (sum(visitor_count.june) / count(NULLIF(visitor_count.june, 0::double precision))::double precision)::integer AS avg_jun,
            (sum(visitor_count.july) / count(NULLIF(visitor_count.july, 0::double precision))::double precision)::integer AS avg_jul,
            (sum(visitor_count.aug) / count(NULLIF(visitor_count.aug, 0::double precision))::double precision)::integer AS avg_aug,
            (sum(visitor_count.sept) / count(NULLIF(visitor_count.sept, 0::double precision))::double precision)::integer AS avg_sep,
            (sum(visitor_count.oct) / count(NULLIF(visitor_count.oct, 0::double precision))::double precision)::integer AS avg_oct,
            (sum(visitor_count.nov) / count(NULLIF(visitor_count.nov, 0::double precision))::double precision)::integer AS avg_nov,
            (sum(visitor_count."dec") / count(NULLIF(visitor_count."dec", 0::double precision))::double precision)::integer AS avg_dec
           FROM visitor_count
          WHERE visitor_count.year::double precision >= (date_part('year'::text, CURRENT_DATE) - 10::double precision)
          GROUP BY visitor_count.park_code) v;

ALTER TABLE public.visitor_average
    OWNER TO postgres;

