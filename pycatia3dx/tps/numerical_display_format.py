"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class NumericalDisplayFormat(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     NumericalDisplayFormat
                | 
                | Interface to manage numerical format properties of GST, DRF and Datum
                | Target.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def avilable_display_factor(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AvilableDisplayFactor() As long (Read Only)
                |     Retrieves or sets the maximun level of factor available to be
                |     displayed.
                |     It may vary according to the name of the format.

        :return: int
        """

        return self.com_object.AvilableDisplayFactor

    @property
    def display_factor(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisplayFactor() As long
                |     Retrieves or sets the level of factor to be displayed.
                |     The numerical values associated to the annotation will be displayed as per
                |     this Display Factor.

        :return: int
        """

        return self.com_object.DisplayFactor

    @display_factor.setter
    def display_factor(self, value: int):
        """
        :param int value:
        """

        self.com_object.DisplayFactor = value

    @property
    def display_leading_zero(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisplayLeadingZero() As long
                |     Retrieves or sets the annotation DisplayLeadingZero.
                |     The numerical values associated to the annotation will be displayed as per
                |     this DisplayLeadingZero.
                |     The integer value of onValue/inValue corresponding to:
                |     0 : no display of LeadingZero.
                |     1 : display the LeadingZero.

        :return: int
        """

        return self.com_object.DisplayLeadingZero

    @display_leading_zero.setter
    def display_leading_zero(self, value: int):
        """
        :param int value:
        """

        self.com_object.DisplayLeadingZero = value

    @property
    def display_trailing_zero(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DisplayTrailingZero() As long
                |     Retrieves or sets the annotation DisplayTrailingZero.
                |     The numerical values associated to the annotation will be displayed as per
                |     this DisplayTrailingZero.
                |     The integer value of onValue/inValue corresponding to:
                |     0 : no display of TrailingZero.
                |     1 : display the TrailingZero.

        :return: int
        """

        return self.com_object.DisplayTrailingZero

    @display_trailing_zero.setter
    def display_trailing_zero(self, value: int):
        """
        :param int value:
        """

        self.com_object.DisplayTrailingZero = value

    @property
    def format_name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FormatName() As CATBSTR
                |     Retrieves or sets the format name.
                |     The numerical values associated to the annotation will be displayed as per
                |     this format.

        :return: str
        """

        return self.com_object.FormatName

    @format_name.setter
    def format_name(self, value: str):
        """
        :param str value:
        """

        self.com_object.FormatName = value

    @property
    def precision(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Precision() As long
                |     Retrieves or sets the precision of annotation.
                |     The numerical values associated to the annotation will be displayed as per
                |     this precision.

        :return: int
        """

        return self.com_object.Precision

    @precision.setter
    def precision(self, value: int):
        """
        :param int value:
        """

        self.com_object.Precision = value

    @property
    def separator(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Separator() As long
                |     Retrieves or sets the annotation separator.
                |     The numerical values associated to the annotation will be displayed with
                |     this seperator.
                |     The integer value of onValue/inValue corresponding to:
                |     0 ""
                |     1 "/"
                |     2 ":"
                |     3 "("
                |     4 ")"
                |     5 "\\"
                |     6 ","
                |     7 "<
                |     8 ">
                |     9 "X"
                |     10 "*"
                |     11 "."
                |     12 ";"
                |     13 "+"
                |     14 "["
                |     15 "]"
                |     16 "-"
                |     17 "_"
                |     18 " " 

        :return: int
        """

        return self.com_object.Separator

    @separator.setter
    def separator(self, value: int):
        """
        :param int value:
        """

        self.com_object.Separator = value

    def __repr__(self):
        return f'NumericalDisplayFormat(name="{ self.name }")'
