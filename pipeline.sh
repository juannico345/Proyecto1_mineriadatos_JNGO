QUERY="SELECT+TOP+1000000+ga.source_id,ga.phot_g_mean_mag,ga.phot_bp_mean_mag,ga.phot_rp_mean_mag,ga.phot_rp_mean_flux_error,ga.bp_rp,param.teff_gspphot,param.mg_gspphot,param.radius_gspphot+FROM+gaiadr3.gaia_source+AS+ga+JOIN+gaiadr3.astrophysical_parameters+AS+param+USING+(source_id)+WHERE+param.radius_gspphot+>+0+AND+param.teff_gspphot+>+0"
URL="https://gea.esac.esa.int/tap-server/tap/sync?REQUEST=doQuery&LANG=ADQL&FORMAT=csv&QUERY=${QUERY}"
echo "Descargando archivos"
wget -q -O gaia.csv "$URL"

echo "Archivo descargado: gaia.csv"

python constructor_db.py
python analisis_visual.py

cat README.md


