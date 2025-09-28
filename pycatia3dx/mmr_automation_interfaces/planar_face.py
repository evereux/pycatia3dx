#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.face import Face


class PlanarFace(Face):

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
                |                             CATMmrAutomationInterfaces.Face
                |                                 PlanarFace
                | 
                | 2-D boundary with a planar geometry.
                | Role: This Boundary object may be, for example, the face of a
                | cube.
                | You will create a PlanarFace object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as ShapeFactory.AddNewDraft
                | ).
                | The lifetime of a PlanarFace object is limited, see Boundary.
                | 
                | Example:
                |     This example asks the end user to select a face and two planar faces, and
                |     creates a draft on these faces:
                | 
                |      Dim InputObjectType(0)
                |      Set Editor = CATIA.ActiveEditor
                |      Set Selection = Editor.Selection
                |      'We propose to the user that he select the face to draft
                |      InputObjectType(0)="Face"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the face to
                |      draft",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set FaceToDraft = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the neutral face
                |      InputObjectType(0)="PlanarFace"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the neutral
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set NeutralFace = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the parting
                |      element
                |      InputObjectType(0)="PlanarFace"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the parting
                |      element",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set PartingElement = Selection.Item(1).Value
                |      Set Draft = ShapeFactory.AddNewDraft(FaceToDraft,NeutralFace,0,PartingElement,0.0,0.0,1.0,0,5.0,0)
                |      Set DraftDomains = Draft.DraftDomains
                |      Set DraftDomain = DraftDomains.Item(1)
                |      DraftDomain.SetPullingDirection 0.0, 0.0,1.0
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_first_axis(self, o_first_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetFirstAxis(CATSafeArrayVariant oFirstAxis)
                |     Returns the planar face first axis
                | 
                |     Parameters:
                | 
                |         oFirstAxis[0]
                |             The X Coordinate of the planar face first axis 
                |         oFirstAxis[1]
                |             The Y Coordinate of the planar face first axis 
                |         oFirstAxis[2]
                |             The Z Coordinate of the planar face first axis

        :param tuple o_first_axis:
        :return: None
        """
        return self.com_object.GetFirstAxis(o_first_axis)

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetOrigin(CATSafeArrayVariant oOrigin)
                |     Returns the origin of the planar face.
                | 
                |     Parameters:
                | 
                |         oOrigin[0]
                |             The X Coordinate of the planar face origin 
                |         oOrigin[1]
                |             The Y Coordinate of the planar face origin 
                |         oOrigin[2]
                |             The Z Coordinate of the planar face origin

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_origin)

    def get_second_axis(self, o_second_axis: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetSecondAxis(CATSafeArrayVariant oSecondAxis)
                |     Returns the planar face second axis.
                | 
                |     Parameters:
                | 
                |         oSecondAxis[0]
                |             The X Coordinate of the planar face second axis 
                |         oSecondAxis[1]
                |             The Y Coordinate of the planar face second axis 
                |         oSecondAxis[2]
                |             The Z Coordinate of the planar face second axis

        :param tuple o_second_axis:
        :return: None
        """
        return self.com_object.GetSecondAxis(o_second_axis)

    def __repr__(self):
        return f'PlanarFace(name="{ self.name }")'
