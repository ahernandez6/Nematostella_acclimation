# Scripts and files used to identify and annotate differentially methylated regions

#### dss_temp_var.R
* Script to identify differentially methylated regions for pairwise comparisons of DNA collected from animals acclimated to 15°C, 20°C, and 25°C

* Input was coverage output files (bismark.cov.gz) generated from methylation calling using Bismark.

##### Dependencies: 
* [DSS](https://www.bioconductor.org/packages/release/bioc/html/DSS.html)
* [bsseq](https://www.bioconductor.org/packages/release/bioc/html/bsseq.html)

#### annotation_extraction.py
* Script to characterize gene body DMRs
* Counts the number of DMRs located within genes, exons, and introns
* Produces a csv file with gene annotation information for DMRs on gene bodies

#### transposon_extraction.py
* Script to characterize transposable element DMRs
* Counts the number of DMRs located in transposable elements
* Produces a csv file with transposable element annotation information for DMRs

#### Nvec200.fasta.repeat.out.edit 
* Out file from RepeatMasker used as input for transposon_extraction.py
