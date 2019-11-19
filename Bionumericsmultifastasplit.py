"""
Casper Jamin 2019-11-19
this python script takes a fasta file with multiple entries from BioNumerics export
and splits them into seperate fasta files

required python3.6 as I like f-strings
"""

from Bio import SeqIO
from argparse import ArgumentParser

def multifastasplitter(inputfile):
    """
    takes input multifasta, splits them into seperate genome assemblies
    """

    for i in SeqIO.parse(inputfile, "fasta"):
        outputfile = i.id.split("|")[2]
        with open(f"{outputfile}.fasta", 'a') as f:
            f.write(f">{i.id}\n{i.seq}")




def main(command_line = None):
    #add main parser object
    parser = ArgumentParser(description = "multifasta splitter")
    parser.add_argument("-i", required = True, dest = "input_file")



    args = parser.parse_args(command_line)
    multifastasplitter(args.input_file)

if __name__ == "__main__":
    main()
