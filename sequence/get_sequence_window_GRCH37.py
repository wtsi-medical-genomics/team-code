#!/usr/bin/env python

"""
Retrieve a window of bases from GRCH37 centered on provided chrom, pos locations
using ensembl's RESTful API.


Author: Daniel Rice
"""

import requests
import argparse


def base_look_up(chrom, pos, radius):
    print chrom, pos, radius
    pos = int(pos)
    server = "http://grch37.rest.ensembl.org"
    ext = "/sequence/region/human/{chrom}:{start}..{end}?"
    url = server + ext
    args = {
        'chrom': chrom,
        'start': pos - radius,
        'end': pos + radius,
    }
    r = requests.get(url.format(**args), headers={ "Content-Type" : "text/plain"}) 
    if not r.ok:
      r.raise_for_status()
    seq = r.text
    return seq


def bases_look_up(locations_file, radius):
    o_name = locations_file + '.results'
    with open(locations_file) as i, open(o_name, 'w') as o:
        header = i.readline()
        o.write(header.strip() + '\tseq\n')
        for line in i:
            tokens = line.split()
            if len(tokens) != 4:
                print 'Skipping because #tokens != 4', line
                continue
            chrom, pos, ref, alt = tokens
            seq = base_look_up(chrom, pos, radius)
            assert seq[radius] == ref
            o.write(line.strip() + '\t' + seq + '\n')

    print 'Output written to ', o_name


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Retrieve a window of bases from GRCH37 centered on provided chrom, pos locations.')
    parser.add_argument('locations_file',
        type=str, help='Tab-seperated input file with header: chrom pos ref alt')
    parser.add_argument('radius', nargs='?', type=int, default=100,
        help='The radius of the sequence window around provided locations (default: 100)')
    args = parser.parse_args()
    bases_look_up(args.locations_file, args.radius)


