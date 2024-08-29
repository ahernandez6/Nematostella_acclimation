# COMMANDS USED TO PERFORM READ MAPPING & METHYLATION CALLING

### Perform genome indexing
```
bismark_genome_preparation --bowtie2 --verbose --parallel 4 01-GENOME_PREP
```

### Align reads to reference genome
```
bismark --genome 01-GENOME_PREP -1 [FASTQ_PE1] -2 [FASTQ2_PE2] --parallel 4 --non_directional --score_min L,0,-0.6
```

### Deduplicate alignment file
```
deduplicate_bismark -p --output_dir 02-DEDUPLICATED [BAM FILES]
``` 

### Call methylation
```
bismark_methylation_extractor [BAM FILES] -p --parallel 4 --bedGraph --cytosine_report --genome_folder 01-GENOME_PREP
```
