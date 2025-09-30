"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.types.general import CATVariant


class MarkerPointing(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MarkerPointing
                | 
                | Allows management of Marker Pointing information.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_object(self, i_object: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObject(AnyObject iObject)
                |     Adds a new Link to a 3D marker.
                | 
                |     Parameters:
                | 
                |         iObject
                |             The 3D object ( VPMOccurence) to be linked 
                | 
                |     Example:
                | 
                |          This example adds a new link ThisProduct to the 3D
                |          Marker.
                |          
                | 
                |          cMarker.AddObject(ThisProduct)

        :param AnyObject i_object:
        :return: None
        """
        return self.com_object.AddObject(i_object.com_object)

    def count_object(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CountObject() As long
                |     Returns the number of objects which are linked to the marker
                |     3D.
                | 
                |     Returns:
                |         The number of objects 
                |     Example:
                | 
                |          This example reads the number of objects in the
                |          marker3D
                |          
                | 
                |          Dim pMarkerPointing As MarkerPointing
                |          Dim count As Integer
                |          count = pMarkerPointing.CountObject

        :return: int
        """
        return self.com_object.CountObject()

    def get_pointing_positions(self, i_index: CATVariant) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPointingPositions(CATVariant iIndex) As
                | CATSafeArrayVariant
                |     Returns the coordinates of the anchor point of the marker on the
                |     object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             3D: The index of the object in the marker 3D. The index of the first object is 1, and the index of the last object is CountObject. : 0, if not linked Object 2D: 0 
                | 
                |     Returns:
                |         oCoordinates The coordinates of the anchor point 2D: oCoordinates (0)
                |         is the X coordinate of the anchor point oCoordinates (1) is the Y coordinate of
                |         the anchor point 3D: oCoordinates (0) is the X coordinate of the anchor point
                |         oCoordinates (1) is the Y coordinate of the anchor point oCoordinates (2) is
                |         the Z coordinate of the anchor point 
                |     Example:
                | 
                |          The following example returns the 3D Text pointing
                |          position
                |          
                | 
                |          Dim Pos (2)
                |          Dim pMarkerPointing As MarkerPointing
                |          Pos = pMarkerPointing.GetPointingPositions

        :param CATVariant i_index:
        :return: tuple
        """
        return self.com_object.GetPointingPositions(i_index)

    def item_object(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ItemObject(CATVariant iIndex) As CATBaseDispatch
                |     Returns an object which is linked to the marker 3D using its
                |     index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the object in the marker 3D. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |
                |     Returns:
                |         The retrieved object ( VPMOccurence) 
                |     Example:
                | 
                |          This example retrieves in ThisObject the first object from marker
                |          3D.
                |
                |          Dim ThisObject As Marker
                |          Set ThisObject = cMarker.ItemObject(1)

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.ItemObject(i_index)

    def remove_object(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveObject(CATVariant iIndex)
                |     Removes an object which is linked to the marker 3D using its
                |     index.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the object in the marker 3D. The index of the first
                |             object is 1, and the index of the last object is CountObject.
                |             
                | 
                |     Example:
                | 
                |          This example removes the first object from the marker
                |          3D.
                |          
                | 
                |          cMarker.RemoveObject(1)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.RemoveObject(i_index)

    def set_pointing_positions(self, i_index: CATVariant, i_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPointingPositions(CATVariant iIndex,CATSafeArrayVariant
                | iCoordinates)
                |     Sets the coordinates of the anchor point of the marker on the
                |     object.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             3D: The index of the object in the marker 3D. The index of the first object is 1, and the index of the last object is CountObject. : 0, if not linked Object 2D: 0 
                |         iCoordinates
                |             The coordinates of the anchor point 2D: iCoordinates (0) is the X
                |             coordinate of the anchor point iCoordinates (1) is the Y coordinate of the
                |             anchor point 3D: iCoordinates (0) is the X coordinate of the anchor point
                |             iCoordinates (1) is the Y coordinate of the anchor point iCoordinates (2) is
                |             the Z coordinate of the anchor point 
                | 
                |     Example:
                | 
                |          The following example set the 3D Text pointing
                |          position
                |          pre>
                |          Dim Pos (2)
                |          Pos (0) = 10, Pos (1) = 10, Pos (2) = 10
                |          Dim pMarkerPointing As MarkerPointing
                |          pMarkerPointing.SetPointingPositions 0, Pos

        :param CATVariant i_index:
        :param tuple i_coordinates:
        :return: None
        """
        return self.com_object.SetPointingPositions(i_index, i_coordinates)

    def __repr__(self):
        return f'MarkerPointing(name="{ self.name }")'
