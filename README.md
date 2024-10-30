# Summary
This is used for two chain protein
# Setup
```
conda install -c conda-forge -c schrodinger pymol-bundle
```
# Parameter
```
usage: parseaf3.py [-h] [--input <file path>] [--first <first chain>] [--second <second chain>] [--label 1|0]
                   [--output <file path>] [--range <rang>]

parseaf3.py --input xxx.cif [--first a] [--second b] [--lable 1] [--output xxx.pse]

options:
  -h, --help            show this help message and exit
  --input <file path>   model file cif or pdb
  --first <first chain>
                        the first chain
  --second <second chain>
                        the second chain
  --label 1|0           1: label all residues;0: no labels for all
  --output <file path>  pse output file
  --range <rang>        rang for residue view with unit Å
```

# How to use
```
python .\parseaf3.py --input C:\Users\aa\Downloads\fold_kcnj2_tmem63a\fold_kcnj2_tmem63a_model_2.cif
```
Please replace the .cif with yours

