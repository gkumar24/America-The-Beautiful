-- Table: public.visitor_count

-- DROP TABLE public.visitor_count;

CREATE TABLE public.visitor_count
(
    year bigint,
    jan bigint,
    feb double precision,
    mar double precision,
    apr double precision,
    may double precision,
    june double precision,
    july double precision,
    aug double precision,
    sept double precision,
    oct double precision,
    nov double precision,
    "dec" double precision,
    total bigint,
    park_code text COLLATE pg_catalog."default"
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.visitor_count
    OWNER to postgres;