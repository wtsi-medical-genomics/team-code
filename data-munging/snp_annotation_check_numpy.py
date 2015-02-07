import numpy as np
import sys

def parse_snp_line(line):
    """
    Parses a single line of the SNP file

    Parameters
    ----------
    line : str
        The line from a SNP file

    Returns
    -------
    chrom : str
        The chromosome location of the SNP
    bp : int
        The bp location of the SNP
    
    """

    data = line.split()
    chrom = data[1].strip()
    bp = int(data[2])
    return chrom, bp

def check_snp_in_annotation(annot_file_loc, snp_file_loc, result_file_loc):
    """
    Checks to see if a set of SNPs occur with an annotation set.

    Parameters
    ----------
    annot_file_loc : str
        The file location of the annotation file.

        Expected format:
        Chrom    Start    End    Summit    Fold    Norm_Fold

    snp_file_loc : str
        The file location of a set of SNPs to query against the annotation file.

        Expected format:
        SNP     Chrom   BP

    result_file_loc : str
        The file location to store the results.

        Format is:
        SNP     Chrom   BP   InAnnotation_Yes/No
   
    Returns
    -------
    None. All work saved in result_file_loc

    """
    annot_chroms = np.genfromtxt(annot_file_loc, usecols=(0), dtype=('S4'), skiprows=1)
    annot_ranges = np.genfromtxt(annot_file_loc, usecols=(1,2), dtype=('i4', 'i4'), skiprows=1)

    snp_file = open(snp_file_loc)
    snp_lines = snp_file.readlines()

    result_file = open(result_file_loc, 'w')
    result_file.write('{}\tInAnnotation_Yes/No\n'.format(snp_lines[0].strip()))
    
     #snp_chroms = np.genfromtxt('data/SNPs.txt', usecols=(1), dtype=('S4'), skiprows=1)
     #snp_locs = np.genfromtxt('data/SNPs.txt', usecols=(2), dtype=('i4'), skiprows=1)
       
    for snp_line in snp_lines[1:]: 
        snp_chrom, snp_bp = parse_snp_line(snp_line)
        chrom_match = snp_chrom == annot_chroms
        start_match = snp_bp >= annot_ranges[:,0]
        end_match = snp_bp <= annot_ranges[:,1]
        result = int(np.any(chrom_match * start_match * end_match))
        result_file.write('{}\t{}\n'.format(snp_line.strip(), result))

    result_file.close()
    snp_file.close()

if __name__ == "__main__":
    try:
        annot_file_loc, snp_file_loc, result_file_loc = sys.argv[1:4]
    except:
        print('Need to provide location of annotation file, snp file, result file') 
    
    check_snp_in_annotation(annot_file_loc, snp_file_loc, result_file_loc)
