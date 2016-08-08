SELECT DISTINCT(adm2_code) FROM sparc_population_month_drought WHERE iso3 = 'NGA';

SELECT SUM(pop) FROM sparc_population_month_drought WHERE iso3 = 'PNG' and month='feb';

SELECT * FROM sparc_gaul_wfp_iso ORDER BY iso3;

SELECT * FROM sparc_gaul_wfp_iso WHERE LENGTH(iso2)>2;

SELECT DISTINCT(iso2),name,iso3 FROM sparc_gaul_wfp_iso ORDER BY iso3;

UPDATE public.sparc_gaul_wfp_iso
   SET iso3='NG'
 WHERE iso3='NGA';

ALTER TABLE sparc_gaul_wfp_iso RENAME COLUMN iso2_old TO iso3;

SELECT * FROM sparc_gaul_wfp_iso WHERE iso3 = 'NGA' ORDER BY adm2_code;

SELECT * FROM sparc_gaul_wfp_iso WHERE adm2_name LIKE '%''%' ORDER BY adm2_code;

UPDATE sparc_gaul_wfp_iso SET adm2_name = 'Quaan Pan' WHERE adm2_name = 'Qua''an Pan';

 