"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingInstructionSetAction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingInstructionSetAction
                | 
                | Interface for drilling riveting instruction set actions.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activation_condition(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ActivationCondition() As CATBSTR
                |     Returns or sets parameter name which drives the activation of the action.

        :return: str
        """

        return self.com_object.ActivationCondition

    @activation_condition.setter
    def activation_condition(self, value: str):
        """
        :param str value:
        """

        self.com_object.ActivationCondition = value

    def get_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetType() As CATBSTR
                |     Gets the type of action.

        :return: str
        """
        return self.com_object.GetType()

    def __repr__(self):
        return f'ManufacturingInstructionSetAction(name="{ self.name }")'
