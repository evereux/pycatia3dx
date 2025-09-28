"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.real_param import RealParam
from pycatia3dx.knowledge_interfaces.unit import Unit


class Dimension(RealParam):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.Parameter
                |                         KnowledgeIDLItf.RealParam
                |                             Dimension
                | 
                | Represents the dimension parameter.
                | It is an abstract object which is not intended to be created as such, but from
                | which the length and angle parameters derive.
                | 
                | See also:
                |     Length, Angle
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def unit(self) -> Unit:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Unit() As Unit (Read Only)
                |     Returns the unit used for this dimension object.

        :return: Unit
        """

        return Unit(self.com_object.Unit)

    def value_as_string2(self, i_nb_decimals: int, i_show_trailing_zeros: bool) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func ValueAsString2(long iNbDecimals,boolean iShowTrailingZeros) As
                | CATBSTR
                |     Gets the value of the parameter as a string, with a given
                |     precision.
                | 
                |     Parameters:
                | 
                |         iNbDecimals
                |             the maximum number of decimal places to use to generate the string
                |             (minimum 0, maximum 9) 
                |         iShowTrailingZeros
                |             this argument says if trailing zeros have to be shown
                |             
                | 
                |     Returns:
                |         oValue the value of the parameter 
                | 
                | Example:
                |     This example gets the value of the existing dimension parameter and shows
                |     it in a message box
                | 
                |      Dim str
                |      str = dimension.ValueAsString2
                |      MsgBox str

        :param int i_nb_decimals:
        :param bool i_show_trailing_zeros:
        :return: str
        """
        return self.com_object.ValueAsString2(i_nb_decimals, i_show_trailing_zeros)

    def __repr__(self):
        return f'Dimension(name="{ self.name }")'
