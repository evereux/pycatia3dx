"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_math_point import SimMathPoint
from pycatia3dx.sma_mpa_base.sim_math_vector import SimMathVector


class SimAxis(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAxis
                | 
                | Represents the Axis object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Axis() As CATBaseDispatch (Read Only)
                |     Returns of set the axis.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Axis)

    @property
    def axis_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisType() As SimAxisAxisType
                |     Returns of set the axis type. The graphical user interface editor for this
                |     SimAxis only supports geometric axis types. See SimAxisAxisType for additional
                |     information.

        :return: int
        """

        return self.com_object.AxisType

    @axis_type.setter
    def axis_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.AxisType = value

    def get_axis(self, o_origin: SimMathPoint, o_vector: SimMathVector) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxis(SimMathPoint oOrigin,SimMathVector oVector)
                |     Retrieves the axis point and direction.
                | 
                |     Parameters:
                | 
                |         oOrigin[out]
                |             is the point 
                |         oVector[out]
                |             is the direction of the line

        :param SimMathPoint o_origin:
        :param SimMathVector o_vector:
        :return: None
        """
        return self.com_object.GetAxis(o_origin.com_object, o_vector.com_object)

    def set_axis(self, i_origin: SimMathPoint, i_vector: SimMathVector) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxis(SimMathPoint iOrigin,SimMathVector iVector)
                |     Sets the axis data using point and direction. If this method is used to set
                |     the Axis then GetAxis( CATMathPoint & oOrigin, CATMathVector & oVector ) must
                |     be used to retrieve the axis and not GetAxis(CATISimLinkAccess_var & ispSupport
                |     ).
                | 
                |     Parameters:
                | 
                |         iOrigin[in]
                |             is the point 
                |         iVector[in]
                |             is the direction of the line 

        :param SimMathPoint i_origin:
        :param SimMathVector i_vector:
        :return: None
        """
        return self.com_object.SetAxis(i_origin.com_object, i_vector.com_object)

    def __repr__(self):
        return f'SimAxis(name="{ self.name }")'
