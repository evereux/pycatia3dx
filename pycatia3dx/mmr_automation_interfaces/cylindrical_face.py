#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.face import Face


class CylindricalFace(Face):

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
                |                                 CylindricalFace
                | 
                | 2-D boundary with a cylindrical geometry.
                | Role: This Boundary object may be, for example, the lateral face of a
                | cylinder.
                | You will create a CylindricalFace object using the Shapes.GetBoundary ,
                | HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as
                | ShapeFactory.AddNewCircPattern ).
                | The lifetime of a CylindricalFace object is limited, see
                | Boundary.
                | 
                | Example:
                |     This example asks the end user to select a shape to pattern and a
                |     cylindrical face, and creates a circular pattern of the shape. The cylindrical
                |     face specifies the rotation axis.
                | 
                |      Dim InputObjectType(0)
                |      Set Editor = CATIA.ActiveEditor
                |      Set Selection = Editor.Selection
                |      'We propose to the user that he select the shape to
                |      pattern
                |      InputObjectType(0)="SketchBasedShape"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the shape to
                |      pattern",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Shape = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the cylindrical
                |      face
                |      InputObjectType(0)="CylindricalFace"
                |      Status=Selection.SelectElement2(InputObjectType,"Select the cylindrical
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set CylindricalFace = Selection.Item(1).Value
                |      Set Part = Editor.ActiveObject
                |      Set RotationCenter = Part.CreateReferenceFromName("")
                |      Set CircPattern = ShapeFactory.AddNewCircPattern(Shape,1,4,20.0,45.0,1,4,RotationCenter,CylindricalFace,True,0.0,True)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_direction(self, o_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetDirection(CATSafeArrayVariant oDirection)
                |     Returns the direction of the cylindrical face axis
                | 
                |     Parameters:
                | 
                |         oDirection[0]
                |             The X Coordinate of the axis direction 
                |         oDirection[1]
                |             The Y Coordinate of the axis direction 
                |         oDirection[2]
                |             The Z Coordinate of the axis direction

        :param tuple o_direction:
        :return: None
        """
        return self.com_object.GetDirection(o_direction)

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GetOrigin(CATSafeArrayVariant oOrigin)
                |     Returns the origin of the cylindrical face axis.
                | 
                |     Parameters:
                | 
                |         oOrigin[0]
                |             The X Coordinate of the axis origin 
                |         oOrigin[1]
                |             The Y Coordinate of the axis origin 
                |         oOrigin[2]
                |             The Z Coordinate of the axis origin

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_origin)

    def __repr__(self):
        return f'CylindricalFace(name="{ self.name }")'
