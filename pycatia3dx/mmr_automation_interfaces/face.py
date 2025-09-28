#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.boundary import Boundary


class Face(Boundary):

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
                |                             Face
                | 
                | 2-D boundary.
                | Role: This Boundary object may be, for example, the lateral face of
                | cylinder.
                | You will create a Face object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | ShapeFactory.AddNewFaceFillet ).
                | The lifetime of a Face object is limited, see Boundary.
                | See also:
                | PlanarFace , CylindricalFace .
                | 
                | Example:
                |     This example asks the end user to select two faces, and creates a face-face
                |     fillet on these faces:
                | 
                |      Dim InputObjectType(0)
                |      Set Editor = CATIA.ActiveEditor
                |      Set Selection = Editor.Selection
                |      'We propose to the user that he select the first face
                |      InputObjectType(0)="Face"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the first
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set FirstFace = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the second face
                |      InputObjectType(0)="Face"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the second
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set SecondFace = Selection.Item(1).Value
                |      Set FaceFillet = ShapeFactory.AddNewFaceFillet(FirstFace,SecondFace,5.0)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'Face(name="{ self.name }")'
