"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingInstructionSetParam(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingInstructionSetParam
                | 
                | Interface for drilling riveting instruction set parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def default_value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DefaultValue() As CATBSTR
                |     Returns or sets the default value.

        :return: str
        """

        return self.com_object.DefaultValue

    @default_value.setter
    def default_value(self, value: str):
        """
        :param str value:
        """

        self.com_object.DefaultValue = value

    @property
    def mapping_rule(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MappingRule() As CATBSTR
                |     Returns or sets the mapping rule to evaluate it. It fails when parameter is
                |     public or when iMappingRule syntax is not valid.

        :return: str
        """

        return self.com_object.MappingRule

    @mapping_rule.setter
    def mapping_rule(self, value: str):
        """
        :param str value:
        """

        self.com_object.MappingRule = value

    @property
    def public(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Public() As boolean
                |     Returns or sets whether the parameter is public. (i.e. evaluated in
                |     drilling riveting operation)

        :return: bool
        """

        return self.com_object.Public

    @public.setter
    def public(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Public = value

    def get_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetType() As long
                |     Gets parameter type.
                | 
                |     Returns:
                | 
                |             0:Boolean
                |             1:Integer
                |             2:Real
                |             3:String
                |             4:Length
                |             5:Angle
                |             6:Time
                |             7:LinearFeedRate
                |             8:AngularFeedRate

        :return: int
        """
        return self.com_object.GetType()

    def __repr__(self):
        return f'ManufacturingInstructionSetParam(name="{ self.name }")'
