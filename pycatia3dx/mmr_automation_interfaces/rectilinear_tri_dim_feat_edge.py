#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.tri_dim_feat_edge import TriDimFeatEdge


class RectilinearTriDimFeatEdge(TriDimFeatEdge):

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
                |                                CATMmrAutomationInterfaces.TriDimFeatEdge
                |                                     RectilinearTriDimFeatEdge
                | 
                | 1-D boundary belonging to a feature whose topological result is three
                | dimensional, the boundary having a rectilinear geometry.
                | Role: This Boundary object may be, for example, the edge of a Pad resulting
                | from the extrusion of a square.
                | You will create a RectilinearTriDimFeatEdge object using the Shapes.GetBoundary
                | , HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as Hole.SetDirection
                | ).
                | The lifetime of a RectilinearTriDimFeatEdge object is limited, see
                | Boundary.
                | 
                | Example:
                |     This example asks the end user to select a face, a rectilinear edge, and
                |     creates a hole. The rectilinear edge specifies the hole direction. It may be a
                |     RectilinearTriDimFeatEdge, a RectilinearBiDimFeatEdge or a
                |     RectilinearMonoDimFeatEdge.
                | 
                |      Dim EnabledObjectSelection1(0)
                |      Dim EnabledObjectSelection2(2)
                |      Set Editor = CATIA.ActiveEditor
                |      Set Selection = Editor.Selection
                |      'We propose to the user that he select a face
                |      EnabledObjectSelection1(0)="Face"
                |      Status=Selection.SelectElement2(EnabledObjectSelection1,"Select a
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Face = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the hole direction
                |      EnabledObjectSelection2(0)="RectilinearTriDimFeatEdge"
                |      EnabledObjectSelection2(1)="RectilinearBiDimFeatEdge"
                |      EnabledObjectSelection2(2)="RectilinearMonoDimFeatEdge"
                |      Status=Selection.SelectElement2(EnabledObjectSelection2,"Select the hole
                |      direction",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Hole = ShapeFactory.AddNewHoleFromPoint(20.0,-5.5, 1.07,Face,10.0)
                |      Hole.ThreadingMode = 1
                |      Hole.ThreadSide = 0
                |      Hole.SetDirection Selection.Item(1).Value
    
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
                |     Returns the direction of the rectilinear edge
                | 
                |     Parameters:
                | 
                |         oDirection[0]
                |             The X Coordinate of the direction 
                |         oDirection[1]
                |             The Y Coordinate of the direction 
                |         oDirection[2]
                |             The Z Coordinate of the direction

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
                |     Returns the origin of the the rectilinear edge.
                | 
                |     Parameters:
                | 
                |         oOrigin[0]
                |             The X Coordinate of the rectilinear edge origin 
                |         oOrigin[1]
                |             The Y Coordinate of the rectilinear edge origin 
                |         oOrigin[2]
                |             The Z Coordinate of the rectilinear edge origin

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_origin)

    def __repr__(self):
        return f'RectilinearTriDimFeatEdge(name="{ self.name }")'
