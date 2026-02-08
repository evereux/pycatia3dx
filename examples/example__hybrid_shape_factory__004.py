"""

    Example - Hybrid Shape Factory - 004

    Description:
        Loops through the items in hybrid body "ConstructionGeometry" and determine the object type using selection.
        Once determined create an object from it and find it's parent(s).

    Requirements:
        - An active part document open with a geometrical set called "ConstructionGeometry" containing points
          generated using HybridShapePtCoord and line generated using HybridShapeLinePtPt:

            Part
            |- ConstructionGeometry
                |- Points

"""

##########################################################
# insert syspath to project folder so examples can be run.
# for development purposes.
import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))
##########################################################

from pycatia3dx import catia3dx
from pycatia3dx.hybrid_shapes.hybrid_shape_line_pt_pt import HybridShapeLinePtPt
from pycatia3dx.hybrid_shapes.hybrid_shape_point_coord import (
    HybridShapePointCoord,
)
from pycatia3dx.mmr_automation_interfaces.part import Part

application = catia3dx()
editor = application.active_editor
# ActiveObject returns AnyObject, so we need to wrap it with Part class manually
part = Part(editor.active_object.com_object)

hbs = part.hybrid_bodies
hb_construction_lines = hbs.item("ConstructionGeometry")
gs_construction_geometry = hb_construction_lines.hybrid_shapes

for i in range(len(gs_construction_geometry)):
    shape_index = i + 1
    hs = gs_construction_geometry.item(shape_index)

    # clear the selection on each loop.
    editor.selection.clear()
    # add the shape to the selection.
    editor.selection.add(hs)
    # create the selected element by getting the first item in the document selection.
    selected_elem = editor.selection.item(1)

    # test part only has HybridShapeLinePtPt
    if selected_elem.type == "HybridShapeLinePtPt":
        # to create the HybridShapeLinePtPt object we need to use the hybrid_shape com_object.
        hs_line_pt_pt = HybridShapeLinePtPt(hs.com_object)

        ref_start_point = hs_line_pt_pt.pt_origin
        ref_end_point = hs_line_pt_pt.pt_extremity

        start_point = HybridShapePointCoord(gs_construction_geometry.item(ref_start_point.display_name).com_object)
        end_point = HybridShapePointCoord(gs_construction_geometry.item(ref_end_point.display_name).com_object)

        print(f'Line: {hs_line_pt_pt.name}')
        print(f'\tStart point: {start_point.name, start_point.get_coordinates()}')
        print(f'\tEnd point: end_point.name, end_point.get_coordinates()')