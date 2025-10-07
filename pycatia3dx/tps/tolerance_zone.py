"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ToleranceZone(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ToleranceZone
                | 
                | Interface for accessing tolerance zone informations of a TPS.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def form(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Form() As CATBSTR
                |     Retrieves tolerance zone form.

        :return: str
        """

        return self.com_object.Form

    @form.setter
    def form(self, value: str):
        """
        :param str value:
        """

        self.com_object.Form = value

    @property
    def validated_tolerance_value(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ValidatedToleranceValue() As boolean
                |     Returns or sets whether the value for the dimension limit is
                |     validated.
                |     TRUE if it is validated.

        :return: bool
        """

        return self.com_object.ValidatedToleranceValue

    @validated_tolerance_value.setter
    def validated_tolerance_value(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ValidatedToleranceValue = value

    @property
    def value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Value() As double
                |     Retrieves tolerance zone value (in millimeters). 

        :return: float
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: float):
        """
        :param float value:
        """

        self.com_object.Value = value

    def __repr__(self):
        return f'ToleranceZone(name="{ self.name }")'
