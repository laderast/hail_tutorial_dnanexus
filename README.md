# Working with Hail on DNAnexus

This repository is an adaptation of notebooks from DNAnexus' OpenBio Repository. It abbreviates the process of working with Hail on the DNAnexus platform. It is divided into two sections:

- `01-Hail-Skills.ipynb` - Basic skills working with Hail Tables and MatrixTables
- `02-gwas-ipynb` - The full GWAS process that starts with a stored MatrixTable in a DNAnexus database.

## DNAnexus Project

There is an example project that has the relevant MatrixTable and Hail Tables stored in a DNAX database. This is not currently available. 

All output is calculated on a Synthetic Patient Dataset (100K-UKB-synth-pheno-geno).

## As-Is Software Disclaimer

This content in this repository is delivered "As-Is". Notwithstanding anything to the contrary, DNAnexus will have no warranty, support, liability or other obligations with respect to Materials provided hereunder.

## Downloading to a JupyterLab Instance

To download this repository to your JupyterLab instance, copy the cloning link and use `git clone <cloning link>` from your terminal or Bash notebook/console.
```bash
git clone https://github.com/laderast/hail_tutorial/
```
The cloning link may be found by clicking on the "Code" drop down menu in Github and following instructrutions.

## Uploading Content from a JupyterLab Instance to a Project on the Platform

To upload a file to your project, use CLI dx-toolbox command, `dx upload <file_name>`.
```bash
dx upload BGEN_import.ipynb
````

To upload a folder to your project, use CLI dx-toolbox command, `dx upload -r <folder_name>`.
```bash
dx upload -r OpenBio
```
d
