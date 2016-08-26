import requests

BUILDS = [\
    'GRCh37',
    'NCBI36',
    'NCBI35',
    'NCBI34',
]


def map_to_build(chrom1, pos1, build1, build2):
    server = 'http://rest.ensembl.org'
    ext = '/map/human/{}/{}:{}..{}:/{}?'.format(build1, chrom1, pos1, pos1, build2)
    r = requests.get(server+ext, headers={'Content-Type':'application/json'})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    decoded = r.json()
    mappings = decoded['mappings']
    if len(mappings) != 1:
        return 0
    mapped = mappings[0]['mapped']
    start = mapped['start']
    return start


def get_location(rsid, build='GRCh38'):
    if build == 'GRCh38':
        server = 'http://rest.ensembl.org/'
    elif build == 'GRCh37':
        server = 'http://grch37.rest.ensembl.org/'
    ext = '/variation/human/{}'
    r = requests.get(server+ext.format(rsid), headers={'Content-Type':'application/json'})
    if not r.ok:
        r.raise_for_status()
        sys.exit()
    snp = r.json()
    mappings = snp['mappings']
    if len(mappings) != 1:
        return
    location = mappings[0]['location']
    chrom, _ = location.split(':')
    start, end = _.split('-')
    return {'chrom': chrom, 'start': start, 'end': end}


def determine_rsid_build(rsid, chrom, pos):
    pos = int(pos)
    location_GRCh38 = get_location(rsid)
    if not location_GRCh38:
        return
    if  pos == location_GRCh38['start']:
        return 'GRCh38'
    for build in BUILDS:
        mapped_start = map_to_build(location_GRCh38['chrom'], location_GRCh38['start'], 'GRCh38', build)
        if mapped_start == pos:
            return build


def determine_bim_build(bim):
    with open(bim) as f:
        lines = f.readlines()
    rsids = filter(lambda x: '\trs' in x, lines)
    builds = set()
    for index in range(0, len(rsids), len(rsids)/10):
        rsid = rsids[index]
        chrom, rsid, _, pos, A1, A2 = rsid.split()
        build = determine_rsid_build(rsid, chrom, pos)
        if build and (build in BUILDS):
            builds.add(build)
    return builds

