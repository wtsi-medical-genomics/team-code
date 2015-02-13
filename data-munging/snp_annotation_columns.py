#!/usr/bin/env python
import numpy as np
import sys
import os
import pdb

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

def check_snp_in_annotation(annot_dir, snp_file_loc, result_file_loc):
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
    
    annot_files = sorted(os.listdir(annot_dir))
    print(annot_files)

    # Create 4 seperate lists to hold all of the annotation information
    annot_chrom = np.array([])
    annot_start = np.array([])
    annot_end = np.array([])
    annot_index = np.array([])

    # Build the annot vector by iterating over the annot_files
    for index, annot_filename in enumerate(annot_files):
        annot_file_loc = os.path.join(annot_dir, annot_filename)
        chroms = np.genfromtxt(annot_file_loc, usecols=(0), dtype=('S4'), skiprows=1)
        annot_chrom = np.r_[annot_chrom, chroms]
        annot_start = np.r_[annot_start, np.genfromtxt(annot_file_loc, usecols=(1), dtype=('i4'), skiprows=1)]
        annot_end = np.r_[annot_end, np.genfromtxt(annot_file_loc, usecols=(2), dtype=('i4'), skiprows=1)]
        annot_index = np.r_[annot_index, np.ones(chroms.shape) * index]

    # Need to trim 'chr' from the front of all the chromosme entries in the annotations
    trim_chr = lambda x: x[3:]
    annot_chrom = map(trim_chr, annot_chrom)

    snp_file = open(snp_file_loc)
    snp_lines = snp_file.readlines()

    result_file = open(result_file_loc, 'w')
    file_name_header = '\t'.join(annot_files)
    result_file.write('{}\t{}\n'.format(snp_lines[0].strip(), file_name_header))
   
    # Go through each line of the snp_file and check against the annotion numpy arrays
    for snp_line in snp_lines[1:]: 
        snp_chrom, snp_bp = parse_snp_line(snp_line)
        chrom_match = np.core.defchararray.equal(snp_chrom, annot_chrom)
        start_match = snp_bp >= annot_start
        end_match = snp_bp <= annot_end
        result = chrom_match * start_match * end_match
        annot_found = np.unique(annot_index[result]).astype('int')
        annot_str = np.zeros(len(annot_files))
        if len(annot_found) > 0:
            annot_str[annot_found] = 1
        annot_str = "\t".join(map(str,annot_str.astype('int')))
        result_file.write('{}\t{}\n'.format(snp_line.strip(), annot_str))
    
    result_file.close()
    snp_file.close()

if __name__ == "__main__":
    try:
        annot_dir, snp_file_loc, result_file_loc = sys.argv[1:4]
    except:
        print('Need to provide location of annotation directory, snp file, result file') 
    
    #print annot_dir, snp_file_loc, result_file_loc

    check_snp_in_annotation(annot_dir, snp_file_loc, result_file_loc)
