"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter


class EnumParam(Parameter):

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
                |                         EnumParam
                | 
                | Represents the enum parameter.
                | 
                | See also:
                |     BoolParam
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def value_enum(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ValueEnum() As CATBSTR
                |     Returns or sets the value of the EnumParameter object. Units are expressed
                |     in the IS unit system, except for lengths expressed in millimeters, and angles
                |     expressed in decimal degrees.
                | 
                |     Example:
                |         This example sets the param1 value to 1 if its value is greater than
                |         2.5:
                | 
                |          If (density.Value > 2.5)  Then
                |              density.Value = 1
                |          End If

        :return: str
        """

        return self.com_object.ValueEnum

    @value_enum.setter
    def value_enum(self, value: str):
        """
        :param str value:
        """

        self.com_object.ValueEnum = value

    def __repr__(self):
        return f'EnumParam(name="{ self.name }")'
