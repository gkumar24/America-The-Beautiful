-- Table: public.visitor_count_analysis

-- DROP TABLE public.visitor_count_analysis;

CREATE TABLE public.visitor_count_analysis
(
    month integer NOT NULL,
    park_code character varying(10) COLLATE pg_catalog."default" NOT NULL,
    park_name character varying(255) COLLATE pg_catalog."default",
    visitor_count double precision,
    CONSTRAINT visitor_count_analysis_pkey PRIMARY KEY (month, park_code)
)

alter table public.visitor_count_analysis add snp500_index double precision
