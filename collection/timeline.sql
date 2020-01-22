-- Table: public.timeline

-- DROP TABLE public.timeline;

CREATE TABLE public.timeline
(
    name text COLLATE pg_catalog."default",
    date_established text COLLATE pg_catalog."default",
    area text COLLATE pg_catalog."default",
    recreation_visitors bigint,
    description text COLLATE pg_catalog."default",
    year_established text COLLATE pg_catalog."default",
    park_name text COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.timeline
    OWNER to postgres;