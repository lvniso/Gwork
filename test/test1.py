import dxfgrabber
import dxfwrite

dxf = dxfgrabber.readfile("Drawing1.dxf")
print("DXF version: {}".format(dxf.dxfversion))
header_var_count = len(dxf.header)  # dict of dxf header vars
layer_count = len(dxf.layers)  # collection of layer definitions
block_definition_count = len(dxf.blocks)  # dict like collection of block definitions
entity_count = len(dxf.entities)  # list like collection of entities