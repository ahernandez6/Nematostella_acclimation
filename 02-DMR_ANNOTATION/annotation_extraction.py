#!/usr/bin/env python3

"""
Module Name: annotation_extraction.py
Description: This script annotates differentially methylated regions within genes, exons, and introns.
Author: Alexandra M. Vargas
Date: 2024-08-19
Version: 1.0
"""

import argparse
import pandas as pd
import os

def annotate_dmrs(dmr_file, gff_file):
    # Load data
    dmr=pd.read_csv(dmr_file, sep=',')
    gff=pd.read_csv(gff_file, sep='\t', header=None, comment='#')
    gff.columns=['chr', 'source', 'type','start', 'end', 'score', 'strand', 'frame', 'ID']
    # Merge dmr and gff file on chromosomes
    merged = dmr.merge(gff, how='inner', on='chr')
    # Identify dmrs that fall within genes
    methylated_genes=merged.loc[(merged['start_x']>=merged['start_y']) & (merged['end_x']<=merged['end_y']) & (merged['type']=='gene')]
    methylated_genes=methylated_genes.rename(columns={'start_x':'methy_start', 'end_x':'methy_end', 'start_y':'gene_start', 'end_y':'gene_end'})
    # Identify dmrs within exons
    methylated_exons=merged.loc[(merged['start_x']>=merged['start_y']) & (merged['end_x']<=merged['end_y']) & (merged['type']=='exon')]
    # Drop isoforms
    methylated_exons=methylated_exons.drop_duplicates(subset=('start_y','end_y'))
    # Count dmrs on gene bodies
    unique_methy_genes=methylated_genes.drop_duplicates(subset='areaStat')
    dmr_gene_count=len(unique_methy_genes)
    # Count the number of dmrs that are located on exons
    unique_methy_exons = methylated_exons.drop_duplicates(subset='areaStat')
    dmr_exon_count=len(unique_methy_exons)
    # Count dmrs in introns
    methylated_introns=unique_methy_genes[~unique_methy_genes['areaStat'].isin(unique_methy_exons['areaStat'])]
    dmr_intron_count=len(methylated_introns)

    return (dmr_gene_count, dmr_exon_count, dmr_intron_count, methylated_genes)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Annotate differentially methylated regions")
    parser.add_argument('dmr_file', type=str, help='Path to the dmr file')
    parser.add_argument('gff_file', type=str, help='Path to the gff file')
    # Use --csv parameter to generate a csv file of gene annotations for dmrs (includes isoforms and possible pseudogenes)
    parser.add_argument('--csv', action='store_true', help='create dmr gene annotation csv file')
    parser.add_argument('--file_name', type=str, help='Specify the name of the output CSV file.')
    args = parser.parse_args()

    # Call the function with the provided arguments
    (dmr_gene_count, dmr_exon_count, dmr_intron_count, methylated_genes)=annotate_dmrs(args.dmr_file, args.gff_file)
    print(f"Number of differentially methylated genes: {dmr_gene_count}")
    print(f"Number of differentially methylated exons: {dmr_exon_count}")
    print(f"Number of differentially methylated introns: {dmr_intron_count}")

    if args.csv:
        if args.file_name:
            methylated_genes.to_csv(args.file_name, index=False)
        else:
            print("Error: Specify the output file name using --file_name when --csv is set")
    else:
        pass

if __name__ == "__main__":
    main()
