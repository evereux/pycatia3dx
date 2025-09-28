#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.edge import Edge


class BiDimFeatEdge(Edge):

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
                |                             CATMmrAutomationInterfaces.Edge
                |                                 BiDimFeatEdge
                | 
                | 1-D boundary belonging to a feature whose topological result is two
                | dimensional.
                | Role: This Boundary object may be, for example, the edge of a surface obtained
                | through the extrusion of a spline.
                | You will create a BiDimFeatEdge object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | HybridShapeFactory.AddNewPointOnCurveFromDistance ).
                | The lifetime of a BiDimFeatEdge object is limited, see
                | Boundary.
                | 
                | Example:
                |     This example asks the end user to select an edge, and creates a point on
                |     this edge. Here, both TriDimFeatEdge and BiDimFeatEdge objects are proposed to
                |     the user.
                | 
                |      Set Editor = CATIA.ActiveEditor
                |      Set Part = Editor.ActiveObject
                |      Set HybridBodies = Part.HybridBodies
                |      Set HybridBody = HybridBodies.Item("Geometrical Set.1")
                |      'We propose to the user that he select an edge
                |      Dim InputObjectType(1)
                |      InputObjectType(0)="TriDimFeatEdge"
                |      InputObjectType(1)="BiDimFeatEdge"
                |      Set Selection = Editor.Selection
                |      Status=Selection.SelectElement2(InputObjectType,"Select an
                |      edge",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Curve = Selection.Item(1).Value
                |      Set HybridShapePointOnCurve = HybridShapeFactory.AddNewPointOnCurveFromDistance(Curve,18.0,False)
                |      HybridBody.AppendHybridShape HybridShapePointOnCurve
                |      Part.InWorkObject = HybridShapePointOnCurve
                |      Part.Update
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'BiDimFeatEdge(name="{ self.name }")'
