# COMMANDS TO PERFORM GENE ONTOLOGY ENRICHMENT ANALYSIS ON DMRS
We performed this analysis using the script for [GO_MWU.R](https://github.com/z0on/GO_MWU).

### Prepare a measures table for input into GO_MWU
We used the GO terms produced from the Zimmermann et al. (2023) _Nematostella vectensis_ genome assembly: [https://simrbase.stowers.org/starletseaanemone](https://simrbase.stowers.org/starletseaanemone) (NV20240221.GO.csv)
```
python prep_GO_input.py anno_dmr_F15_v_F20_alpha_0.05_2024.csv NV20240221.GO.csv --out go_dmr_F15_v_F20_alpha_0.05_2024.csv
python prep_GO_input.py anno_dmr_F20_v_F25_alpha_0.05_2024.csv NV20240221.GO.csv --out go_dmr_F20_v_F25_alpha_0.05_2024.csv
python prep_GO_input.py anno_dmr_F15_v_F25_alpha_0.05_2024.csv NV20240221.GO.csv --out go_dmr_F15_v_F25_alpha_0.05_2024.csv
```

### Run GO_MWU
GO_MWU_temp.R - This script must be run in RStudio. All dependencies indicated on [https://github.com/z0on/GO_MWU](https://github.com/z0on/GO_MWU) must be downloaded prior to running the script. The input should be changed to each of the output files produced from the commands above.
