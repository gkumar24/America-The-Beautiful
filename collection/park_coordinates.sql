-- Table: public.park_coordinates

-- DROP TABLE public.park_coordinates;

CREATE TABLE public.park_coordinates
(
    park_code text COLLATE pg_catalog."default",
    park_name text COLLATE pg_catalog."default",
    longitude double precision,
    latitude double precision
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.park_coordinates
    OWNER to postgres;