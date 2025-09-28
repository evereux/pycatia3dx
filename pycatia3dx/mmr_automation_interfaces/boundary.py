#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.mode.reference import Reference


class Boundary(Reference):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfModelInterfaces.Reference
                |                         Boundary
                | 
                | Topological cell, such as a face, an edge or a vertex.
                | Role: The Boundary objects are basic topological objects, such as the edge of a
                | Pad. Some of them posess a geometrical feature (planar face, rectilinear
                | edge).
                | You will create a Boundary object (such as the TriDimFeatEdge object, which is
                | derived, indirectly, from the Boundary object) using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | ShapeFactory.AddNewEdgeFilletWithConstantRadius ). Note that, regarding V4
                | sub-elements, once the data of a CATIA Version 4 Model has been copied to a
                | .CATPart, the sub-elements of the resulting .CATPart are supported by the
                | Boundary object.
                | The lifetime of a Boundary object is limited. In particular, after having call
                | Part.Update , the Boundary objects are usually no more valid.
                | See also:
                | 
                |     Face , PlanarFace , CylindricalFace
                |     Edge , TriDimFeatEdge , RectilinearTriDimFeatEdge , BiDimFeatEdge ,
                |     RectilinearBiDimFeatEdge , MonoDimFeatEdge ,
                |     RectilinearMonoDimFeatEdge
                |     Vertex , TriDimFeatVertexOrBiDimFeatVertex ,
                |     NotWireBoundaryMonoDimFeatVertex,
                |     ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex
                | 
                | Note: Boundary objects cannot be selected into the specification
                | tree.
                | 
                | Note:For a Boundary object, the object returned by the AnyObject.Parent
                | property is the master shape. For example, if we have:
                | 
                |                          Pad.2
                |                           !
                |                           !
                |  +                        V
                |  !                      +---+ 
                |  !                    /   / !
                |  +-- Pad.1          /   /   !
                |  !                /   / one +------+
                |  !               +---+    /       /! <--- Pad.1
                |  !               !   !  /       /  +
                |  +-- Pad.2       !   !/       /   /
                |                  !   +------+   /
                |                  !          ! /
                |                  +----------+
                |  
                | 
                | then, for the PlanarFace number "one", the AnyObject.Parent property returns
                | the Pad.2 automation object (see Pad ).
                | 
                | Example:
                |     This example asks the end user to select an edge (using the TriDimFeatEdge
                |     object), and creates an edge fillet on this edge:
                | 
                |      Dim InputObjectType(0)
                |      Set Selection = CATIA.ActiveEditor.Selection
                |      'We propose to the user that he select an edge
                |      InputObjectType(0)="TriDimFeatEdge"
                |      Status=Selection.SelectElement2(InputObjectType,"Select an
                |      edge",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set EdgeFillet = ShapeFactory.AddNewEdgeFilletWithConstantRadius(Selection.Item(1).Value,1,5.0)
                |      EdgeFillet.EdgePropagation = 1
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Boundary(name="{ self.name }")'
