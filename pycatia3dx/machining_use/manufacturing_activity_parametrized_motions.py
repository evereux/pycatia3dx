"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingActivityParametrizedMotions(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivityParametrizedMotions
                | 
                | Interface to get the macros of an operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_value(self, i_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetValue(CATBSTR iName) As AnyObject
                |     Gets the macro corresponding to the given type.
                | 
                |     Parameters:
                | 
                |         iName
                |             The type of the macro wanted. Authorized values
                |             are:
                | 
                |                 MfgApproachMacro
                |                 MfgRetractMacro
                |                 MfgReturnOneLevelMacro
                |                 MfgReturnTwoLevelMacro
                |                 MfgLinkingMacro
                |                 MfgReturnFinishPathMacro
                |                 MfgClearanceMacro
                |                 MfgBetweenPassesMacro
                |                 MfgAutomaticRoughingMacro (for roughing
                |                 operation)
                |                 MfgPreRoughingMacro (for roughing operation)
                |                 MfgPostRoughingMacro (for roughing operation)
                | 
                |     Returns:
                |         The corresponding macro found.

        :param str i_name:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetValue(i_name))

    def __repr__(self):
        return f'ManufacturingActivityParametrizedMotions(name="{ self.name }")'
