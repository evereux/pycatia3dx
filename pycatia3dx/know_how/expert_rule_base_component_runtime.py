"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ExpertRuleBaseComponentRuntime(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ExpertRuleBaseComponentRuntime
                | 
                | Represents a rule base component in a ruleset.
                | 
                | See also:
                |     ExpertRuleBaseComponentRuntimes.Item, ExpertRuleRuntime,
                |     ExpertCheckRuntime, ExpertRuleSetRuntime
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Comment() As CATBSTR
                |     Returns or sets the comment of a rulebase component.

        :return: str
        """

        return self.com_object.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.com_object.Comment = value

    def accurate_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AccurateType() As CATBSTR
                |     Returns as a string the type of component. Returns a string among
                |     ("ExpertCheck", "ExpertCheckRuntime", "ExpertRule", "ExpertRuleRuntime",
                |     "ExpertRuleSet", "ExpertRuleSetRuntime").
                | 
                |     Returns:
                |         Type name of the rule base component

        :return: str
        """
        return self.com_object.AccurateType()

    def activate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Activate()
                |     Activates the RuleBaseComponent.

        :return: None
        """
        return self.com_object.Activate()

    def deactivate(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Deactivate()
                |     Desactivates the RuleBaseComponent.

        :return: None
        """
        return self.com_object.Deactivate()

    def is_use_only(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsUseOnly() As boolean
                |     Retrieves the use-only status of the component.
                | 
                |     Returns:
                |         Use only status of the component

        :return: bool
        """
        return self.com_object.IsUseOnly()

    def isactivate(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Isactivate() As boolean
                |     Tells if the RuleBaseComponent is active.
                | 
                |     Returns:
                |         Activity of the rule base component

        :return: bool
        """
        return self.com_object.Isactivate()

    def parse(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Parse() As CATBSTR
                |     Syntactically analyses (ie parses) the component.
                | 
                |     Returns:
                |         Empty string if the parse is correct, otherwise comments on the errors

        :return: str
        """
        return self.com_object.Parse()

    def set_use_only(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUseOnly()
                |     Prevents any access to the component for reading or deleting. Be careful : this operation is not reversible.

        :return: None
        """
        return self.com_object.SetUseOnly()

    def __repr__(self):
        return f'ExpertRuleBaseComponentRuntime(name="{ self.name }")'
