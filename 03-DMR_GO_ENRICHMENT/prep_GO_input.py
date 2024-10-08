#!/usr/bin/env python3

"""
Module Name: prep_GO_input.py
Description: This script prepares DMR data for a GO enrichment analysis using GO_MWU.
Author: Alexandra M. Vargas
Date: 2024-08-22
Version: 1.0
"""

import argparse
import pandas as pd
import os

def prep_GO_measure_table(dmr_file, GO_file):
    # Load data
    dmr=pd.read_csv(dmr_file, sep=',')
    go=pd.read_table(GO_file, sep='\t', header=None)
    go.rename(columns={0:'Genes', 1: 'GO ID'}, inplace = True)
    # Extract gene IDs for DMRs and set values to 1 for presence/absence matrix
    pattern=r'(NV2t\d+\.\d)'
    dmr['extracted'] = dmr['ID'].str.extract(pattern)
    for_new_df = ['extracted', 'diff.Methy'] 
    dmr_sub = dmr[for_new_df].copy()
    dmr_sub.rename(columns={'extracted':'Genes', 'diff.Methy':'Methylated'}, inplace=True)
    dmr_sub=dmr_sub.drop_duplicates(subset='Genes')
    dmr_sub['Methylated']=1
    # Add missing genes from the GO annotation and set methylation values to 0 for presence/absence matrix
    all_go=go.merge(dmr_sub, how='left', on='Genes')
    all_go['Methylated'].fillna(0, inplace=True)
    all_go.drop(columns=['GO ID'], inplace=True)
    return (all_go)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Prep GO enrichment analysis input")
    parser.add_argument('dmr_file', type=str, help='Path to the dmr file')
    parser.add_argument('GO_file', type=str, help='Path to two column tab-delimited GO annotation file (gene id - GO terms)')
    parser.add_argument('--out', type=str, help='Specify the name of the output CSV file.')
    args = parser.parse_args()

    # Call the function with the provided arguments
    all_go=prep_GO_measure_table(args.dmr_file, args.GO_file)

    if args.out:
        all_go.to_csv(args.out, sep=',', index=False, header=None)
    else:
        print("Error: Specify the output file name with --out")

if __name__ == "__main__":
    main()
