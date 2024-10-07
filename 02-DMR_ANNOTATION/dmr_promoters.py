#!/usr/bin/env python3

"""
Module Name: dmr_promoters.py
Description: This script annotates differentially methylated regions in promoters
Author: Alexandra M. Vargas
Date: 2024-10-07
Version: 1.0
"""

import argparse
import pandas as pd
import os

def annotate_dmrs(dmr_file, bed_file):
    # Load data
    dmr=pd.read_csv(dmr_file, sep=',')
    promoters=pd.read_table(bed_file, sep='\s+', header=None)
    promoters.columns = ['chr', 'start', 'end', 'gene', 'strand']
    # Merge dmr and promoter file on chromosomes
    merged = dmr.merge(promoters, how='inner', on='chr')
    # Identify dmrs that fall within promoters
    dmr_pro=merged.loc[(merged['start_x']>=merged['start_y']) & (merged['end_x']<=merged['end_y'])]
    #Count dmrs in transposable elements
    dmr_pro_count=len(dmr_pro)
    return (dmr_pro, dmr_pro_count)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Annotate differentially methylated regions in promoters")
    parser.add_argument('dmr_file', type=str, help='Path to the dmr file')
    parser.add_argument('bed_file', type=str, help='Path to the promoter bed file')
    # Use --csv parameter to generate a csv file of tranposable element annotations for dmrs
    parser.add_argument('--csv', action='store_true', help='create dmr promoter annotation csv file')
    parser.add_argument('--file_name', type=str, help='Specify the name of the output CSV file.')
    args = parser.parse_args()

    # Call the function with the provided arguments
    (dmr_pro, dmr_pro_count)=annotate_dmrs(args.dmr_file, args.bed_file)
    print(f"Number of differentially methylated promoters: {dmr_pro_count}")

    if args.csv:
        if args.file_name:
            dmr_pro.to_csv(args.file_name, index=False)
        else:
            print("Error: Specify the output file name using --file_name when --csv is set")
    else:
        pass

if __name__ == "__main__":
    main()
