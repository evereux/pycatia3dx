"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class Line(HybridShape):

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
                |                         Line
                | 
                | Represents the hybrid shape Line feature object.
                | Role: Declare hybrid shape Line root feature object. All interfaces for
                | different type of Line derives HybridShapeLine.
                | 
                | Use the CATIAHybridShapeFactory to create a HybridShapeLine
                | objects.
                | 
                | See also:
                |     HybridShapeFactory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def first_upto_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property FirstUptoElem() As Reference
                |     Role: Gets the First upto element of the line.
                | 
                |     Parameters:
                | 
                |         oFirstUpto
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else

        :return: Reference
        """

        return Reference(self.com_object.FirstUptoElem)

    @first_upto_elem.setter
    def first_upto_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.FirstUptoElem = value

    @property
    def second_upto_elem(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property SecondUptoElem() As Reference
                |     Role: Gets the Second upto element of the line.
                | 
                |     Parameters:
                | 
                |         oSecondUpto
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else

        :return: Reference
        """

        return Reference(self.com_object.SecondUptoElem)

    @second_upto_elem.setter
    def second_upto_elem(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.SecondUptoElem = value

    def get_direction(self, o_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetDirection(CATSafeArrayVariant oDirection)
                |     Role: Returns the unit-vector pointing in the direction of the
                |     line.
                | 
                |     Parameters:
                | 
                |         oDirection
                |         oDirection[0]
                |             The X Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         oDirection[1]
                |             The Y Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         oDirection[2]
                |             The Z Coordinate of the unit vector pointing in the direction of
                |             the line 
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_direction:
        :return: None
        """
        return self.com_object.GetDirection(o_direction)

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetOrigin(CATSafeArrayVariant oOrigin)
                |     Role: Returns the origin of the line.
                | 
                |     Parameters:
                | 
                |         oOrigin
                |         oOrigin[0]
                |             The X Coordinate of a point lying on the line 
                |         oOrigin[1]
                |             The Y Coordinate of a point lying on the line 
                |         oOrigin[2]
                |             The Z Coordinate of a point lying on the line The Origin is
                |             evaluated from the geometry of the line. 
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param tuple o_origin:
        :return: None
        """
        return self.com_object.GetOrigin(o_origin)

    def put_direction(self, i_direction: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub PutDirection(CATSafeArrayVariant iDirection)
                |     Role: Sets the unit-vector pointing in the direction of the
                |     line.
                | 
                |     Parameters:
                | 
                |         iDirection
                |         iDirection[0]
                |             The X Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         iDirection[1]
                |             The Y Coordinate of the unit vector pointing in the direction of
                |             the line 
                |         iDirection[2]
                |             The Z Coordinate of the unit vector pointing in the direction of
                |             the line 
                | 
                |     Returns:
                |         HRESULT S_OK if Ok E_FAIL else return error code for C++
                |         Implementations 
                |     See also:
                |         HybridShapeFactory

        :param tuple i_direction:
        :return: None
        """
        return self.com_object.PutDirection(i_direction)

    def __repr__(self):
        return f'Line(name="{ self.name }")'
