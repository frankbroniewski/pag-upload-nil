Fix the GML created by QGIS for the PAG Upload

QGIS versions after 2.18.10 introduce an empty node in the GML element tree
with an attribute xsi:nil="true". This leads to validation errors.
Users can use this script to remove all nodes which have an xsi:nil="true"
attribute.

usage (in an OSGeo4W-Shell for example)
> python clean_pag_gml pag_C006.gml pag_C006_clean.gml