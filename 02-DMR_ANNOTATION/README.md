# Scripts and files used to identify and annotate differentially methylated regions

#### dss_temp_var.R
- This script was used to identify differentially methylated regions for pairwise comparisons of DNA collected from animals acclimated to 15°C, 20°C, and 25°C.

For this script we input coverage output files (bismark.cov.gz) that were generated from methylation calling using Bismark.

##### Dependencies: 
* [DSS](https://www.bioconductor.org/packages/release/bioc/html/DSS.html)
* [bsseq](https://www.bioconductor.org/packages/release/bioc/html/bsseq.html)

#### annotation_extraction.py
- Script to characterize DMRs based on gene annotations
