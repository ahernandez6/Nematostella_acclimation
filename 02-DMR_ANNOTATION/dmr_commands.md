# COMMANDS TO IDENTIFY AND ANNOTATE DIFFERENTIALLY METHYLATED REGIONS (DMRS)

## IDENTIFYING DMRS IN TEMPERATURE COMPARISONS
The input files used to run this script are the coverage output files (bismark.cov.gz) generated from methylation calling using Bismark. Keep these in the path of the script.
```
Rscript dss_temp_var.R
```

## ANNOTATE GENE BODY DMRS 
We used the DMR files produced from the command above and the gff file produced from the [Zimmermann et al. (2023) gene annotations](https://simrbase.stowers.org/show/Nematostella/vectensis/analysis).
```
python annotation_extraction.py dmr_F15_v_F20_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F15_v_F20_alpha_0.05_2024.csv
python annotation_extraction.py dmr_F20_v_F25_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F20_v_F25_alpha_0.05_2024.csv
python annotation_extraction.py dmr_F15_v_F25_alpha_0.05.csv NV2g.20240221.gff --csv --file_name anno_dmr_F15_v_F25_alpha_0.05_2024.csv
```

## ANNOTATE TRANSPOSABLE ELEMENT DMRS
### Create _de novo_ repeat library using Zimmermann et al. (2023) _Nematostella_ genome assembly
```
BuildDatabase -name "Nvec200" Nvec200.fasta
```
### Concatenate RepBase database to Nvec200 _de novo_ repeat library
```
cat /apps/pkg/repeatmasker/4.1.2/Libraries/RepeatMasker.lib Nvec200-families.fa > RepBase.Nvec200.fa
```
### Run RepeatMasker to annotate repetitive content in the Zimmermann et al. (2023) genome assemby
```
RepeatMasker -pa 14 -lib RepBase.Nvec200.fa Nvec200.fasta -a -gff -dir RepBase_Nvec200_out
```
### Identify and count DMRs that are in transposable elements
We used the DMR files produced from dss_temp_var.R and the out file from RepeatMasker. We edited the out file headings (see included file .out.edit file) to better work with our custom script.
```
python transposon_extraction.py dmr_F15_v_F20_alpha_0.05.csv Nvec200.fasta.repeat.out.edit --csv --file_name dmr_te_F15_v_F20_alpha_0.05.csv
python transposon_extraction.py dmr_F20_v_F25_alpha_0.05.csv Nvec200.fasta.repeat.out.edit --csv --file_name dmr_te_F20_v_F25_alpha_0.05.csv
python transposon_extraction.py dmr_F15_v_F25_alpha_0.05.csv Nvec200.fasta.repeat.out.edit --csv --file_name dmr_te_F15_v_F25_alpha_0.05.csv
```

## ANNOTATE PROMOTER DMRS
### Annotate promoters in the the Zimmermann et al. (2023) genome assemby
The custom scripts SlicePromoters.py and json_to_bed.py were created by [Cleves at el. (2020)](https://www.pnas.org/doi/abs/10.1073/pnas.2015737117).
```
python SlicePromoters.py NV2g.20240221.gff Nvec200.fasta 1000 Nvec200.slicepromoter.out
```
### Convert output to bed file
```
python json_to_bed.py promoters_1000.txt promoters_1000.bed
```
### Identify and count DMRs that are in promoters
```
python dmr_promoters.py dmr_F15_v_F20_alpha_0.05.csv promoters_1000.bed --csv --file_name dmr_promoters_F15_v_F20_alpha_0.05.csv
python dmr_promoters.py dmr_F20_v_F25_alpha_0.05.csv promoters_1000.bed --csv --file_name dmr_promoters_F20_v_F25_alpha_0.05.csv
python dmr_promoters.py dmr_F15_v_F25_alpha_0.05.csv promoters_1000.bed --csv --file_name dmr_promoters_F15_v_F25_alpha_0.05.csv
```
