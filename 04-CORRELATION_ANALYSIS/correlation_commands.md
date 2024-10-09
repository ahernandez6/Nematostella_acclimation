# COMMANDS FOR CORRELATION ANALYSIS OF DIFFERENTIAL GENE METHYLATION AND EXPRESSION

## Perform differential gene expression analysis
We used the data collected from [Baldassarre et al. (2022)](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE168938)
### Transcript quantification
```
align_and_estimate_abundance.pl --transcripts NV2g.20240221.transcripts.fa --prep_reference --samples_file sample_file.txt --est_method salmon --seqType fq --output_dir aea_outdir --aln_method bowtie2 --thread_count 20 > aea.out 2> aea.err
```
### Build transcript matrix
```
abundance_estimates_to_matrix.pl --gene_trans_map none --est_method salmon  --out_prefix Nvec200 --name_sample_by_basedir F15_1/quant.sf F15_2/quant.sf F15_3/quant.sf F15_4/quant.sf F15_5/quant.sf F20_1/quant.sf F20_2/quant.sf F20_3/quant.sf F20_4/quant.sf F20_5/quant.sf F25_1/quant.sf F25_2/quant.sf F25_3/quant.sf F25_4/quant.sf F25_5/quant.sf
```
### Quality check samples and replicates
```
/apps/pkg/trinity/2.14.0/Analysis/DifferentialExpression/PtR --matrix Nvec200.isoform.counts.matrix --samples sample_file2.txt --log2 --CPM --min_rowSums 10 --compare_replicates --prin_comp 3
```
### Differential gene expression analysis
```
/apps/pkg/trinity/2.14.0/Analysis/DifferentialExpression/run_DE_analysis.pl --matrix Nvec200.isoform.counts.matrix --method DESeq2 --samples_file sample_file2.txt
```
## Perform correlation analysis for differentially methylated and expressed genes
### Prepare matrix of difference measures for differentially methylated and expressed genes
We used the gene annotation csv file we generated from the commands run in 02-DMR_ANNOTATION of this GitHub repo and the result files produced from the differential gene expression analysis as input to prepare the matrix.
```
python overlapping_dmr_dge.py anno_dmr_F15_v_F20_alpha_0.05_2024.csv Nvec200.isoform.counts.matrix.F15_vs_F20.DESeq2.DE_results --out dmr_dge_F15_v_F20_alpha_0.05.csv
python overlapping_dmr_dge.py anno_dmr_F20_v_F25_alpha_0.05_2024.csv Nvec200.isoform.counts.matrix.F20_vs_F25.DESeq2.DE_results --out dmr_dge_F20_v_F25_alpha_0.05.csv
python overlapping_dmr_dge.py anno_dmr_F15_v_F25_alpha_0.05_2024.csv Nvec200.isoform.counts.matrix.F15_vs_F25.DESeq2.DE_results --out dmr_dge_F15_v_F25_alpha_0.05.csv
```
### Run correlation_dmr_dge.R
* correlation_dmr_dge.R - This script must be run in RStudio. The script performs a Shapiro-Wilk test to determine if the data follow a normal distribution. The script generates a scatter plot and performs a Spearman correlation analysis to determine the association between change in mean methylation and log2 fold change in gene expression after long-term temperature acclimation.
