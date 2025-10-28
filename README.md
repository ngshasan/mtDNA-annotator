# 🧬 mtDNA-annotator

**mtDNA-annotator** is a command-line tool for batch annotation of mitochondrial DNA (mtDNA) variants using public databases like:

- [HmtVar](http://www.hmtvar.uniba.it/)
- [MITOMAP](https://www.mitomap.org/)
- [gnomAD-mtDNA](https://gnomad.broadinstitute.org/downloads)
- [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/)

It supports multiple VCF files and outputs both annotated tables and a circular genome visualization of variant positions.

## ✨ Features
✅ Batch annotate multiple mtDNA VCF files  
✅ Lookup variants in HmtVar API  
✅ Optional MITOMAP web scraping  
✅ Optional gnomAD frequency merging  
✅ Optional ClinVar clinical significance lookup  
✅ Outputs `.csv`, `.tsv`, and a circular plot of variants

## 📦 Installation
### 🔹 Conda (recommended)
```bash
conda create -n mtdna-env python=3.9 -y
conda activate mtdna-env
conda install -c conda-forge pandas requests tqdm beautifulsoup4 matplotlib
```

### Pip Install (Local)
```bash
git clone https://github.com/ngshasan/mtDNA-annotator.git
cd mtDNA-annotator
pip install .
```

### 📁 Structure of Folder:
```java
mtDNA-annotator/
├── annotate_mtDNA.py              ✅ Main script
├── README.md                      ✅ From earlier (you already have this)
├── Dockerfile                     ✅ Included
├── environment.yml                ✅ For conda
├── LICENSE                        ✅ MIT License (default)
├── .gitignore                     ✅ Python/Docker ignores
├── setup.py                       ✅ For pip installation
└── mtDNA_annotator/               ✅ Python package folder
    └── __init__.py
    └── core.py                    ✅ Move script logic here
```

### 1) Downloading ClinVar mtDNA VCF File (GRCh37 / rCRS-based)

#### Option A: Download full ClinVar VCF (GRCh37 build)
```bash
mkdir clinvar
cd clivar

wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz
wget https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar.vcf.gz.tbi

#### Option B: Extract only mitochondrial variants
bcftools view -r MT clinvar.vcf.gz -o clinvar_mtDNA.vcf -Ov
```

### 2) Downloading gnomAD-mtDNA Frequency File
```bash
cd ..
mkdir gnomad
cd gnomad

# gnomAD v3.1 genomes — chrM (mtDNA)
wget https://storage.googleapis.com/gcp-public-data--gnomad/release/3.1/vcf/genomes/gnomad.genomes.v3.1.sites.chrM.vcf.bgz
wget https://storage.googleapis.com/gcp-public-data--gnomad/release/3.1/vcf/genomes/gnomad.genomes.v3.1.sites.chrM.vcf.bgz.tbi
wget https://storage.googleapis.com/gcp-public-data--gnomad/release/3.1/vcf/genomes/gnomad.genomes.v3.1.sites.chrM.reduced_annotations.tsv


#### Convert to TSV (simplified format):
bcftools query -f '%POS\t%REF\t%ALT\t%INFO/AF\n' gnomad.mtDNA.vcf.bgz > gnomad_mtDNA.tsv
```

### 🧪U Usage: Basic CLI example
```bash
mtdna-annotate \
  --vcf_folder vcfs \
  --gnomad gnomad \
  --clinvar clinvar \
  --output_prefix my_results \
  --use_gnomad --use_mitomap --use_clinvar
```

### Required Inputs:
- vcfs/ — folder with one or more .vcf files
- gnomad_mtDNA.tsv — gnomAD mtDNA variant frequencies (optional)
- clinvar_mtDNA.vcf — ClinVar variants limited to chrM/MT (optional)

### Output
- my_results.csv — annotated variant data (comma-separated)
- my_results.tsv — same as above, tab-separated
- my_results_circular_plot.png — circular genome view of variants

### 📚 Data Sources
- HmtVar (via API)
- MITOMAP SNPsByPosition (web scraped)
- gnomAD mtDNA VCF (filtered)
- ClinVar VCF (filtered to chrM)

### 🛠 Developer Info
- Language: Python 3.7+
- Packages: pandas, requests, tqdm, beautifulsoup4, matplotlib
- Entry point: mtDNA_annotator/core.py

