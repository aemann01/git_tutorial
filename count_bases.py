import sys
def count_bases (fasta_file_name):
    sequece=''
    def count():
        if len(sequece):
            print("Number of A's: %d" % sequece.count("A"))
            print("Number of C's: %d" % sequece.count("C"))
            print("Number of G's: %d" % sequece.count("G"))
            print("Number of T's: %d" % sequece.count("T"))
            print()
    with open(fasta_file_name) as file_content:
        i=0
        for seqs in file_content:
            if seqs.startswith('>'):
                count()
                print("Sequence %d:" % i)
                i=i+1
                sequece=''
            else:
                sequece=sequece+seqs.strip()
        count()

result = count_bases(sys.argv[1])
