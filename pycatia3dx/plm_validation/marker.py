"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.plm_validation.marker_pointing import MarkerPointing


class Marker(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Marker
                | 
                | Represents a marker.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Angle() As double
                |     Returns or sets the Angle of the marker.
                | 
                |     Example:
                | 
                |          This example sets the Angle
                |          
                | 
                |          Dim cMarker As Marker
                |          cMarker.Angle = 45

        :return: float
        """

        return self.com_object.Angle

    @angle.setter
    def angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.Angle = value

    @property
    def document_ref(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DocumentRef(CATBSTR iReference) (Write Only)
                |     Sets a path of the document for Picture, Hyperlink and
                |     Audio.
                | 
                |     Example:
                | 
                |          The following set the path to the document
                |          
                | 
                |          Dim cMarker As Marker
                |          Dim path As String
                |          cMarker.DocumentRef path

        :return: None
        """

        return None

    @document_ref.setter
    def document_ref(self, value: str):
        """
        :param str value:
        """

        self.com_object.DocumentRef = value

    @property
    def fill(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Fill() As boolean
                |     Returns or sets the Fill of the Marker.
                | 
                |     Example:
                | 
                |          This example sets the Fill
                |          
                | 
                |          Dim cMarker As Marker
                |          cMarker.Fill = True

        :return: bool
        """

        return self.com_object.Fill

    @fill.setter
    def fill(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Fill = value

    @property
    def frame(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Frame() As boolean
                |     Returns or sets the Frame of the Marker.
                | 
                |     Example:
                | 
                |          This example sets the Frame
                |
                |          Dim cMarker As Marker
                |          cMarker.Frame = True

        :return: bool
        """

        return self.com_object.Frame

    @frame.setter
    def frame(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Frame = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR (Read Only)
                |     Returns the type of the Marker. 2DLine 2DPen 2DCircle 2DRectangle 2DArrow
                |     2DText, 3DText 2DPicture, 3DPicture 2DHyperlink, 3DHyperlink 2DAudio,
                |     3DAudio
                | 
                |     Example:
                | 
                |          This example get the marker type
                |
                |          Dim cMarker As Marker
                |          Dim myType As String 
                |          myType = cMarker.Type

        :return: str
        """

        return self.com_object.Type

    def get_pointing(self) -> MarkerPointing:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPointing() As MarkerPointing
                |     Returns the pointing info related to a marker.
                | 
                |     Parameters:
                | 
                |         oPointing
                |             The Pointing 
                | 
                |     Example:
                |
                |          Dim cMarker As Marker
                |          Dim bIsPointing As boolean
                |          bIsPointing = cMarker.IsPointing 
                |          if(bIsPointing) then
                |         Dim markerPointing As MarkerPointing
                |         Set markerPointing = cMarker.GetPointing 
                |          end if

        :return: MarkerPointing
        """
        return MarkerPointing(self.com_object.GetPointing())

    def get_positions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPositions() As CATSafeArrayVariant
                |     Returns the coordinates of the positions of the Marker.
                | 
                |     These positions depend on the type of the Marker. 2D Line: 2 positions (two
                |     end points). 2D Arrow: 2 positions (head and tail points). 2D Rectangle: 2
                |     positions (bottom left and top right corner). 2D Circle: 2 positions (center
                |     and point through which it passes). 2D Freehand: 2 positions (series of
                |     points). 2D & 3D Text, Picture, Hyperlink, Audio: 1 anchor position (top left
                |     point).
                | 
                |     Parameters:
                | 
                |         oCoordinates
                |             2D: oCoordinates (0) is the X coordinate of the first point
                |             oCoordinates (1) is the Y coordinate of the first point oCoordinates (2) is the
                |             X coordinate of the second point oCoordinates (3) is the Y coordinate of the
                |             second point oCoordinates (n*2-2) is the X coordinate of the n-th point
                |             oCoordinates (n*2-1) is the X coordinate of the n-th point 3D: oCoordinates (0)
                |             is the X coordinate of the anchor point oCoordinates (1) is the Y coordinate of
                |             the anchor point oCoordinates (2) is the Z coordinate of the anchor point
                |
                |     Example:
                | 
                |          This example returns the 3D Text anchor position
                |
                |          Dim cMarker As Marker
                |          Dim Pos (2)
                |          Pos = cMarker.GetPositions

        :return: tuple
        """
        return self.com_object.GetPositions()

    def is_pointing(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsPointing() As boolean
                |     Returns the check if pointing info exists.
                | 
                |     Example:
                |
                |          Dim cMarker As Marker
                |          Dim bIsPointing As boolean
                |          bIsPointing = cMarker.IsPointing

        :return: bool
        """
        return self.com_object.IsPointing()

    def set_positions(self, i_coordinates: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPositions(CATSafeArrayVariant iCoordinates)
                |     Sets the coordinates of the positions of the Marker.
                | 
                |     These positions depend on the type of the Marker. 2D Line: 2 positions (two
                |     end points). 2D Arrow: 2 positions (head and tail points). 2D Rectangle: 2
                |     positions (bottom left and top right corner). 2D Circle: 2 positions (center
                |     and point through which it passes). 2D Freehand: 2 positions (series of
                |     points). 2D & 3D Text, Picture, Hyperlink, Audio: 1 anchor position (top left
                |     point).
                | 
                |     Parameters:
                | 
                |         iCoordinates
                |             2D: iCoordinates (0) is the X coordinate of the first point
                |             iCoordinates (1) is the Y coordinate of the first point iCoordinates (2) is the
                |             X coordinate of the second point iCoordinates (3) is the Y coordinate of the
                |             second point iCoordinates (n*2-2) is the X coordinate of the n-th point
                |             iCoordinates (n*2-1) is the X coordinate of the n-th point 3D: iCoordinates (0)
                |             is the X coordinate of the anchor point iCoordinates (1) is the Y coordinate of
                |             the anchor point iCoordinates (2) is the Z coordinate of the anchor point
                |
                |     Example:
                | 
                |          The following example set the 3D Text anchor position
                |
                |          Dim Pos (2)
                |          Dim cMarker As Marker
                |          Pos (0) = 10, Pos (1) = 10, Pos (2) = 10
                |          cMarker.SetPositions Pos

        :param tuple i_coordinates:
        :return: None
        """
        return self.com_object.SetPositions(i_coordinates)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Update()
                |     Updates the marker for account of modification if any.
                | 
                |     Example:
                | 
                |          This example will update the marker
                |
                |          Dim cMarker As Marker
                |          cMarker.Update

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'Marker(name="{ self.name }")'
