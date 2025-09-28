#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.boundary import Boundary


class Vertex(Boundary):

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
                |                             Vertex
                | 
                | 0-D boundary.
                | Role: This Boundary object may be, for example, the corner of a Pad resulting
                | from the extrusion of a square.
                | You will create an Vertex object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | HybridShapeFactory.AddNewLinePtPt ).
                | The lifetime of a Vertex object is limited, see Boundary.
                | See also:
                | TriDimFeatVertexOrBiDimFeatVertex , NotWireBoundaryMonoDimFeatVertex ,
                | ZeroDimFeatVertexOrWireBoundaryMonoDimFeatVertex .
                | 
                | Example:
                |     This example asks the end user to select successively two vertices. Then,
                |     it creates a line between these two vertices.
                | 
                |      Dim InputObjectType(0)
                |      Set Editor = CATIA.ActiveEditor
                |      Set Selection = Editor.Selection
                |      Set Part = Editor.ActiveObject
                |      Set HybridBodies = Part.HybridBodies
                |      Set HybridBody = HybridBodies.Item("Geometrical Set.1")
                |      'We propose to the user that he select the first vertex
                |      InputObjectType(0)="Vertex"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the first
                |      vertex",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set FirstVertex = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the second vertex
                |      InputObjectType(0)="Vertex"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the second
                |      vertex",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set SecondVertex = Selection.Item(1).Value
                |      Set hybridShapeLinePtPt = HybridShapeFactory.AddNewLinePtPt(FirstVertex,SecondVertex)
                |      HybridBody.AppendHybridShape hybridShapeLinePtPt
                |      Part.InWorkObject = hybridShapeLinePtPt
                |      Part.Update
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Vertex(name="{ self.name }")'
