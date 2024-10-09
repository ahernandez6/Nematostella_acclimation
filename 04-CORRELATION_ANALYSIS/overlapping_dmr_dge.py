#!/usr/bin/env python3

"""
Module Name: overlapping_dmr_dge.py
Description: This script extracts the mean difference in methylation and log2 fold change for genes that are differentially methylated and expressed.
Author: Alexandra M. Vargas
Date: 2024-08-22
Version: 1.0
"""

import argparse
import pandas as pd
import os

def prep_dmr_dge_measure_table(dmr_annotation_file, dge_results_file):
    # Load data
    dmr=pd.read_csv(dmr_annotation_file, sep=',')
    dge=pd.read_csv(dge_results_file, sep='\t', header=0, names=['Genes', 'sampleA', 'sampleB', 'baseMeanA', 'baseMeanB', 'baseMean','logFC', 'lfcSE', 'stat', 'PValue', 'padj'])
    #Extract the gene IDs for DMRs and their mean difference in methylation
    pattern = r'(NV2t\d+\.\d)'
    dmr['extracted'] = dmr['ID'].str.extract(pattern)
    for_new_df = ['extracted', 'diff.Methy']
    DMR_sub = dmr[for_new_df].copy()
    DMR_sub.rename(columns={'extracted':'Genes', 'diff.Methy':'Mean difference in methylation'}, inplace=True)
    mean_DMR=DMR_sub.groupby('Genes').mean().reset_index()
    # Extract DGEs with an adjusted p-value of less than 0.05
    dge_sig=dge.loc[dge['padj'] < 0.05]
    # Merge differentially methylated and expressed genes
    matches=mean_DMR.merge(dge_sig, how='inner', on='Genes')
    subset_matches=matches[['Genes','Mean difference in methylation','logFC']]
    return (subset_matches)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Prepare maxtrix with difference measures for differentially methylated and expressed genes")
    parser.add_argument('dmr_annotation_file', type=str, help='Path to the dmr annotation file')
    parser.add_argument('dge_results_file', type=str, help='Path to the DGE results file')
    parser.add_argument('--out', type=str, help='Specify the name of the output CSV file.')
    args = parser.parse_args()

    # Call the function with the provided arguments
    dmr_dge=prep_dmr_dge_measure_table(args.dmr_annotation_file, args.dge_results_file)

    if args.out:
        dmr_dge.to_csv(args.out, sep=',', index=False)
    else:
        print("Error: Specify the output file name with --out")

if __name__ == "__main__":
    main()
