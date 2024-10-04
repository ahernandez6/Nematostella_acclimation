# COMMANDS TO IDENTIFY AND ANNOTATE DIFFERENTIALLY METHYLATED REGIONS (DMRS)

## IDENTIFYING DMRS IN TEMPERATURE COMPARISONS
The input files used to run this script are the coverage output files (bismark.cov.gz) generated from methylation calling using Bismark. Keep these in the path of the script.
```
Rscript dss_temp_var.R
```

## ANNOTATE GENE BODY DMRS 
We used the DMR files produced from the command above and the gff file produced from the [Zimmermann et al. (2023) gene annotations](https://simrbase.stowers.org/show/Nematostella/vectensis/analysis)
```
python annotation_extraction.py dmr_F15_v_F20_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F15_v_F20_alpha_0.05_2024.csv
python annotation_extraction.py dmr_F20_v_F25_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F20_v_F25_alpha_0.05_2024.csv
python annotation_extraction.py dmr_F15_v_F25_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F15_v_F25_alpha_0.05_2024.csv
```

## ANNOTATE TRANSPOSABLE ELEMENT DMRS
### Create _de novo_ repeat library using [Zimmermann et al. (2023) Nematostella genome assembly](https://simrbase.stowers.org/show/Nematostella/vectensis/analysis)
```
BuildDatabase -name "Nvec200" Nvec200.fasta
```
### Concated RepBase database to Nvec200 de novo repeat library
```
cat /apps/pkg/repeatmasker/4.1.2/Libraries/RepeatMasker.lib Nvec200-families.fa > RepBase.Nvec200.fa
```
### Run RepeatMasker to annotate repetitive content in the Zimmermann et al. (2023) genome assemby
```
RepeatMasker -pa 14 -lib RepBase.Nvec200.fa Nvec200.fasta -a -gff -dir RepBase_Nvec200_out
```
