CREATE TABLE public.sparc_population_month
(
  id integer NOT NULL DEFAULT nextval('sparc_population_month_id_seq'::regclass),
  iso3 character(3),
  adm0_name character(120),
  adm0_code character(8),
  adm1_name character(120),
  adm1_code character(8),
  adm2_code character(8),
  adm2_name character(120),
  rp integer,
  jan integer,
  feb integer,
  mar integer,
  apr integer,
  may integer,
  jun integer,
  jul integer,
  aug integer,
  sep integer,
  oct integer,
  nov integer,
  "dec" integer,
  n_cases double precision
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.sparc_population_month
  OWNER TO geonode;