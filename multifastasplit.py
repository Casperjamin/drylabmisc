"""
Casper Jamin 2019-10-19
this python script takes a fasta file with multiple entries
and splits them into seperate fasta files
"""

from Bio import SeqIO
from argparse import ArgumentParser

def multifastasplitter(inputfile, outputfile):
    """
    takes input multifasta, spits out multiple single fasta files
    """
    count = 0
    for i in SeqIO.parse(inputfile, "fasta"):
        with open(f"{outputfile}_{count}.fasta", 'w') as f:
            f.write(f">{i.id}\n{i.seq}")

        count += 1


def main(command_line = None):
    #add main parser object
    parser = ArgumentParser(description = "multifasta splitter")
    parser.add_argument("-i", required = True, dest = "input_file")
    parser.add_argument("-o", required = False, dest = "output_file")



    args = parser.parse_args(command_line)
    multifastasplitter(args.input_file, args.output_file)

if __name__ == "__main__":
    main()
