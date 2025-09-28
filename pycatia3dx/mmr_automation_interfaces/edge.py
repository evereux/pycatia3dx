#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.boundary import Boundary


class Edge(Boundary):

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
                |                         CATMmrAutomationInterfaces.Boundary
                |                             Edge
                | 
                | 1-D boundary.
                | Role: This Boundary object may be, for example, the edge of a
                | cylinder.
                | You will create an Edge object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | HybridShapeFactory.AddNewPointTangent ).
                | The lifetime of an Edge object is limited, see Boundary.
                | See also:
                | TriDimFeatEdge , RectilinearTriDimFeatEdge , BiDimFeatEdge ,
                | RectilinearBiDimFeatEdge , MonoDimFeatEdge , RectilinearMonoDimFeatEdge
                | .
                | 
                | Example:
                |     This example asks the end user to select a planar curve, whose plane is
                |     parallel to the XY plane. Then, it creates a point on the tangent to the curve
                |     in the X direction:
                | 
                |      Dim InputObjectType(0)
                |      Set Editor = CATIA.ActiveEditor
                |      Set Selection = Editor.Selection
                |      Set Part = Editor.ActiveObject
                |      Set HybridBodies = Part.HybridBodies
                |      Set HybridBody = HybridBodies.Item("Geometrical Set.1")
                |      'We propose to the user that he select a planar curve whose plane is
                |      parallel to the XY plane
                |      InputObjectType(0)="Edge"
                |      Status=Selection.SelectElement2(InputObjectType,"Select a planar curve
                |      whose plane is parallel to the XY plane",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set PlanarCurve = Selection.Item(1).Value
                |      Set HybridShapeDirection = HybridShapeFactory.AddNewDirectionByCoord(1.0,0.0,0.0)
                |      Set HybridShapePointTangent = HybridShapeFactory.AddNewPointTangent(PlanarCurve,HybridShapeDirection)
                |      HybridBody.AppendHybridShape HybridShapePointTangent
                |      Part.InWorkObject = HybridShapePointTangent
                |      Part.Update
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Edge(name="{ self.name }")'
