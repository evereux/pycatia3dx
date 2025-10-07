"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.know_how.expert_check_runtime import ExpertCheckRuntime


class ExpertCheck(ExpertCheckRuntime):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    KnowHowIDLItf.ExpertRuleBaseComponentRuntime
                |                         KnowHowIDLItf.ExpertCheckRuntime
                |                             ExpertCheck
                | 
                | Represents the edition part of a check.
                | 
                | See also:
                |     ExpertCheckRuntime.CheckEdition, ExpertRuleSet.CreateCheck
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def body(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Body() As CATBSTR
                |     Returns or sets the body of a Check.
                | 
                |     Example:
                | 
                |          Check1.Body = "H.Diameter > 20mm AND GetSubString(P.Name, 1, 6) == \"\"myPad.\"\""

        :return: str
        """

        return self.com_object.Body

    @body.setter
    def body(self, value: str):
        """
        :param str value:
        """

        self.com_object.Body = value

    @property
    def language(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Language() As long
                |     Returns or sets the language of a check.
                | 
                |     1
                |         KWE language 
                |     2
                |         VB Script

        :return: int
        """

        return self.com_object.Language

    @language.setter
    def language(self, value: int):
        """
        :param int value:
        """

        self.com_object.Language = value

    @property
    def variables(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Variables() As CATBSTR
                |     Returns or sets the variable scope of an Expert Check.
                | 
                |     Example:
                | 
                |          Check1.Variables = "H:Hole; P: Pad"

        :return: str
        """

        return self.com_object.Variables

    @variables.setter
    def variables(self, value: str):
        """
        :param str value:
        """

        self.com_object.Variables = value

    def __repr__(self):
        return f'ExpertCheck(name="{ self.name }")'
