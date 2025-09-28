"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapeOffset(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapeOffset
                | 
                | Represents the hybrid shape offset feature object.
                | Role: To access the data of the hybrid shape offset feature object. This data
                | includes:
                | 
                |     The element to offset
                |     The offset direction
                |     The offset value
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeOffset
                | object.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def offset_direction(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OffsetDirection() As boolean
                |     Returns or sets whether the offset direction is to be
                |     inverted.
                |     True to invert the offset direction.

        :return: bool
        """

        return self.com_object.OffsetDirection

    @offset_direction.setter
    def offset_direction(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.OffsetDirection = value

    @property
    def offset_value(self) -> Length:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OffsetValue() As Length
                |     Returns or sets the offset value.

        :return: Length
        """

        return Length(self.com_object.OffsetValue)

    @offset_value.setter
    def offset_value(self, value: Length):
        """
        :param Length value:
        """

        self.com_object.OffsetValue = value

    @property
    def offseted_object(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property OffsetedObject() As Reference
                |     Returns or sets the face to offset.
                |     Sub-element(s) supported (see Boundary object): Face.

        :return: Reference
        """

        return Reference(self.com_object.OffsetedObject)

    @offseted_object.setter
    def offseted_object(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.OffsetedObject = value

    @property
    def suppress_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SuppressMode() As boolean
                |     Returns or sets suppress mode.
                |     True to activate suppress mode

        :return: bool
        """

        return self.com_object.SuppressMode

    @suppress_mode.setter
    def suppress_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SuppressMode = value

    def add_tricky_face(self, i_tricky_face: Reference) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub AddTrickyFace(Reference iTrickyFace)
                |     Adds a tricky face object on the object.

        :param Reference i_tricky_face:
        :return: None
        """
        return self.com_object.AddTrickyFace(i_tricky_face.com_object)

    def get_tricky_face(self, i_rank: int) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Func GetTrickyFace(long iRank) As Reference
                |     Returns the invalid face object on the object.
                |     param : iRank =position of faces ionvalid for offset

        :param int i_rank:
        :return: Reference
        """
        return Reference(self.com_object.GetTrickyFace(i_rank))

    def remove_tricky_face(self, i_rank: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveTrickyFace(long iRank)
                |     Remove the tricky face object on the object.
                |     param : iRank =position of the face in the list of TrickyFaces

        :param int i_rank:
        :return: None
        """
        return self.com_object.RemoveTrickyFace(i_rank)

    def set_offset_value(self, i_offset: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetOffsetValue(double iOffset)
                |     Set Offset value with input as double.
                |     To be replaced in further release by integration in the pragma put_xxx

        :param float i_offset:
        :return: None
        """
        return self.com_object.SetOffsetValue(i_offset)

    def __repr__(self):
        return f'HybridShapeOffset(name="{ self.name }")'
