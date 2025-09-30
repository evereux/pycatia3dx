"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingMacroMotions(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingMacroMotions
                | 
                | Interface to manage the macros of an operation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def active(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Active() As long
                |     Returns or sets whether the macro is active.

        :return: int
        """

        return self.com_object.Active

    @active.setter
    def active(self, value: int):
        """
        :param int value:
        """

        self.com_object.Active = value

    def get_macro_motion(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMacroMotion(long iPosition) As AnyObject
                |     Gets the motion corresponding to the macro.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The type of the macro we want. Must be equal to 1 or
                |             2.
                | 
                |             Macro Type
                | iPosition = 1
                | iPosition = 2
                |            -----------------------------------------------------------------
                |             MfgApproachMacro
                | Approach
                | Global approach
                |             (in some axial operations only, like thread
                |             milling)
                |             MfgRetractMacro
                | Retract
                | Global retract
                |             (in some axial operations only, like thread
                |             milling)
                |             MfgLinkingMacro
                | Retract
                |
                |             Approach
                |             MfgClearanceMacro
                | Clearance
                |
                |             NOTHING
                |             MfgReturnOneLevelMacro
                | Retract
                |
                |             Approach
                |             MfgReturnTwoLevelMacro
                | Retract
                |
                |             Approach
                |             MfgReturnFinishPathMacro
                | Retract
                |
                |             Approach
                |             MfgBetweenPassesMacro
                | Between paths
                | Between paths
                |             link
                |             MfgAutomaticRoughingMacro
                | Automatic
                |
                |             NOTHING
                |             MfgPreRoughingMacro
                | Pre motions
                |
                |             NOTHING
                |             MfgPostRoughingMacro
                | Post motions
                |
                |             NOTHING
                |              
                | 
                |     Returns:
                |         The corresponding motion.

        :param int i_position:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetMacroMotion(i_position))

    def __repr__(self):
        return f'ManufacturingMacroMotions(name="{ self.name }")'
