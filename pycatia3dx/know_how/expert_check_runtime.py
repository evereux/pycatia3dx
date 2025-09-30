"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.todo_know_how.expert_check import ExpertCheck
from pycatia3dx.todo_know_how.expert_report_objects import ExpertReportObjects
from pycatia3dx.todo_know_how.expert_rule_base_component_runtime import ExpertRuleBaseComponentRuntime


class ExpertCheckRuntime(ExpertRuleBaseComponentRuntime):

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
                |                         ExpertCheckRuntime
                | 
                | Runtime part of a check.
                | The following example shows how to access the Check check1 from an existing
                | RuleSet RS1 of the RuleBase RB1.
                | 
                |  Dim rulebasesset As ExpertRuleBasesSet
                |  Set rulebasesset = ...
                |  Dim Rulebase As ExpertRuleBaseRuntime
                |  Set RuleBase = rulebasesset.Collection.Item("RB1")
                |  Dim Ruleset As ExpertRuleSetRuntime
                |  Set RuleSet = RuleBase.RuleSet.ExpertRuleBaseComponentRuntimes.Item("RS1")
                |  Dim CheckRO As ExpertCheckRuntime
                |  Set CheckRO = RuleSet.ExpertRuleBaseComponentRuntimes.Item("Check1")
                |  
                | 
                | See also:
                |     ExpertRuleBasesSet, ExpertRuleBaseRuntime,
                |     ExpertRuleSetRuntime
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def automatic_correct(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AutomaticCorrect() As boolean
                |     Returns or sets the status of the automatic correction facility. When set
                |     to TRUE, the check automatically calls the user function defined by
                |     put_CorrectFunction when it fails.

        :return: bool
        """

        return self.com_object.AutomaticCorrect

    @automatic_correct.setter
    def automatic_correct(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AutomaticCorrect = value

    @property
    def check_edition(self) -> ExpertCheck:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CheckEdition() As ExpertCheck (Read Only)
                |     Returns the editable object corresponding to this check. Be careful that,
                |     according to your licence, or the type of check you're handling, you may not
                |     have the right to edit the check.
                | 
                |     Example:
                | 
                |          Dim aCheckEdition As ExpertCheck
                |          Set aCheckEdition = aCheckRuntime.CheckEdition
                | 
                |          If not(aCheckEdition is Nothing) Then
                |            CATIA.SystemService.Print aCheckEdition.Body
                |          End if

        :return: ExpertCheck
        """

        return ExpertCheck(self.com_object.CheckEdition)

    @property
    def correct_function(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CorrectFunction() As CATBSTR
                |     Returns or sets the body to be called in order to correct the check.

        :return: str
        """

        return self.com_object.CorrectFunction

    @correct_function.setter
    def correct_function(self, value: str):
        """
        :param str value:
        """

        self.com_object.CorrectFunction = value

    @property
    def correct_function_comment(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CorrectFunctionComment() As CATBSTR
                |     Returns or sets the comment of the correct function of the check.

        :return: str
        """

        return self.com_object.CorrectFunctionComment

    @correct_function_comment.setter
    def correct_function_comment(self, value: str):
        """
        :param str value:
        """

        self.com_object.CorrectFunctionComment = value

    @property
    def correct_function_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CorrectFunctionType() As long
                |     Returns or sets the type of the body to be called in order to correct the
                |     check.
                | 
                |     1
                |         Visual Basic 
                |     2
                |         Comment 
                |     3
                |         Http 
                |     4
                |         User Function

        :return: int
        """

        return self.com_object.CorrectFunctionType

    @correct_function_type.setter
    def correct_function_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.CorrectFunctionType = value

    @property
    def failures(self) -> ExpertReportObjects:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Failures() As ExpertReportObjects (Read Only)
                |     Returns the list of the tuples that don't satisfy this check. You must have
                |     the Knowledge Expert runtime license to navigate in results.

        :return: ExpertReportObjects
        """

        return ExpertReportObjects(self.com_object.Failures)

    @property
    def help(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Help() As CATBSTR
                |     Returns or sets the contextual help of the check object.

        :return: str
        """

        return self.com_object.Help

    @help.setter
    def help(self, value: str):
        """
        :param str value:
        """

        self.com_object.Help = value

    @property
    def justification(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Justification() As CATBSTR
                |     Returns or sets the reason why the check was overridden.

        :return: str
        """

        return self.com_object.Justification

    @justification.setter
    def justification(self, value: str):
        """
        :param str value:
        """

        self.com_object.Justification = value

    @property
    def priority(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Priority() As double
                |     Returns or sets the priority of the check. The priority of expert checks
                |     indicates the order in which the checks are evaluated. Checks with the same
                |     priority are evaluated in the order of their creation.

        :return: float
        """

        return self.com_object.Priority

    @priority.setter
    def priority(self, value: float):
        """
        :param float value:
        """

        self.com_object.Priority = value

    @property
    def succeeds(self) -> ExpertReportObjects:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Succeeds() As ExpertReportObjects (Read Only)
                |     Returns the list of the tuples that satisfy this check. You must have the
                |     Knowledge Expert runtime license to navigate in results.

        :return: ExpertReportObjects
        """

        return ExpertReportObjects(self.com_object.Succeeds)

    def correct(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Correct()
                |     Applies the "correction" function on failed elements.

        :return: None
        """
        return self.com_object.Correct()

    def highlight(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Highlight()
                |     Highlights the Failures on the check.

        :return: None
        """
        return self.com_object.Highlight()

    def status(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Status() As long
                |     Returns the Status of the check.
                | 
                |     Example:
                | 
                |          Dim Check1 As ExpertCheck 
                |          Set Check1 = RuleSet.ExpertRuleBaseComponentRuntimes.Item("Check1")
                |          status = Check1.Status ()
                |
                |     Returns:
                |         1=OK, 0=KO.

        :return: int
        """
        return self.com_object.Status()

    def __repr__(self):
        return f'ExpertCheckRuntime(name="{ self.name }")'
