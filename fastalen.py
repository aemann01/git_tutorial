import sys
from Bio import SeqIO

'''python3 fastalen.py input.fa > output.txt'''

for rec in SeqIO.parse(open(sys.argv[1], 'r'), 'fasta'):
    name = rec.id
    seqLen = len(rec)
    print(name, seqLen)
