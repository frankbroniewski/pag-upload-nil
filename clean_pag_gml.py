#
#
# Fix the GML created by QGIS for the PAG Upload
#
# QGIS versions after 2.18.10 introduce an empty node in the GML element tree
# with an attribute xsi:nil="true". This leads to validation errors.
# Users can use this script to remove all nodes which have an xsi:nil="true"
# attribute.
#
# author: Frank Broniewski
# email: hallo@frankbroniewski.com
#

def clean_me(args):
    """brute force detection and removal"""
    with open(args.input, 'rb') as infile:
        with open(args.output, 'wb') as outfile:
            
            for line in infile:
                if not 'xsi:nil="true"' in line:
                    outfile.write(line)
                else:
                    print "Removing %s" % line


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input GML file')
    parser.add_argument('output', help='Output GML file')
    
    args = parser.parse_args()
    clean_me(args)
