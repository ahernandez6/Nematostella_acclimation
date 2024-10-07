#!/usr/bin/env python3

"""
Module Name: transposon_extraction.py
Description: This script annotates differentially methylated regions in transposable elements.
Author: Alexandra M. Vargas
Date: 2024-10-04
Version: 1.0
"""

import argparse
import pandas as pd
import os

def annotate_dmrs(dmr_file, repeat_file):
    # Load data
    dmr=pd.read_csv(dmr_file, sep=',')
    repeats=pd.read_table(repeat_file, sep='\s+')
    repeats=repeats.rename(columns={'query_seq': 'chr', 'qbegin': 'start', 'qend':'end'})
    # Merge dmr and repeat file on chromosomes
    merged = dmr.merge(repeats, how='inner', on='chr')
    # Identify dmrs that fall within repeats
    methylated_repeats=merged.loc[(merged['start_x']>=merged['start_y']) & (merged['end_x']<=merged['end_y'])]
    # Keep only DMR and repeat class information
    methylated_repeats=methylated_repeats.drop(columns=['SW_score', 'perc_div', 'perc_del', 'perc_ins', 'left', '?', 'rbegin', 'rend', 'left.1', 'ID']) 
    #Remove non-transposable element repeat classifications
    non_te = ['Unknown','Simple_repeat', 'Satellite', 'tRNA']
    te_df = methylated_repeats[~methylated_repeats['repeat_class'].isin(non_te)]
    te_df=te_df.drop_duplicates(subset=['areaStat'])
    #Count dmrs in transposable elements
    dmr_te_count=len(te_df)
    return (te_df, dmr_te_count)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Annotate differentially methylated regions in transposable elements")
    parser.add_argument('dmr_file', type=str, help='Path to the dmr file')
    parser.add_argument('repeat_file', type=str, help='Path to the RepeatMasker out file')
    # Use --csv parameter to generate a csv file of tranposable element annotations for dmrs
    parser.add_argument('--csv', action='store_true', help='create dmr transposable element annotation csv file')
    parser.add_argument('--file_name', type=str, help='Specify the name of the output CSV file.')
    args = parser.parse_args()

    # Call the function with the provided arguments
    (te_df, dmr_te_count)=annotate_dmrs(args.dmr_file, args.repeat_file)
    print(f"Number of differentially methylated transposable elements: {dmr_te_count}")

    if args.csv:
        if args.file_name:
            te_df.to_csv(args.file_name, index=False)
        else:
            print("Error: Specify the output file name using --file_name when --csv is set")
    else:
        pass

if __name__ == "__main__":
    main()
