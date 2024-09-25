# COMMANDS TO IDENTIFY AND ANNOTATE DIFFERENTIALLY METHYLATED REGIONS (DMRS)

## IDENTIFYING DMRS IN TEMPERATURE COMPARISONS
The input files used to run this script are the coverage output files (bismark.cov.gz) generated from methylation calling using Bismark. Keep these in the path of the script.
```
Rscript dss_temp_var.R
```

## ANNOTATE GENE BODY DMRS 
We used the gff file produced from the Zimmermann et al. (2023) gene annotations
```
python annotation_extraction.py dmr_F15_v_F20_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F15_v_F20_alpha_0.05_2024.csv
python annotation_extraction.py dmr_F20_v_F25_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F20_v_F25_alpha_0.05_2024.csv
python annotation_extraction.py dmr_F15_v_F25_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F15_v_F25_alpha_0.05_2024.csv
```
