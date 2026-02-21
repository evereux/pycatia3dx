"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import TYPE_CHECKING

from pycatia3dx.know_how.expert_rule_set import ExpertRuleSet
from pycatia3dx.knowledge_interfaces.relation import Relation
from pycatia3dx.system.any_object import AnyObject

if TYPE_CHECKING:
    from pycatia3dx.know_how.expert_rule_base import ExpertRuleBase


class ExpertRuleBaseRuntime(Relation):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                        
                |                        KnowledgeIDLItf.KnowledgeActivateObject
                |                             KnowledgeIDLItf.Relation
                |                                 ExpertRuleBaseRuntime
                | 
                | Represents the Runtime part of the RuleBase.
                | Example of how to retrieve such an object.
                | 
                |  Dim RBSet as ExpertRuleBasesSet
                |  Set RBSet = ...
                |  Dim RB as ExpertRuleBaseRuntime
                |  Set RB = RBSet.Collection.Item(1)
                |  
                | 
                | See also:
                |     ExpertRuleBasesSet
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def report_description_length(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReportDescriptionLength() As CatDescriptionLengthType
                |     Returns or sets the Report Description Length (For Text option
                |     only).
                | 
                |     0
                |         ShortText 
                |     1
                |         LongText

        :return: int
        """

        return self.com_object.ReportDescriptionLength

    @report_description_length.setter
    def report_description_length(self, value: int):
        """
        :param int value:
        """

        self.com_object.ReportDescriptionLength = value

    @property
    def report_out_put_format(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReportOutPutFormat() As CatOutPutFormatType
                |     Returns or sets the Report OutPut Format.
                | 
                |     0
                |         Html 
                |     1
                |         Text 
                |     2
                |         Print 
                |     3
                |         Email

        :return: int
        """

        return self.com_object.ReportOutPutFormat

    @report_out_put_format.setter
    def report_out_put_format(self, value: int):
        """
        :param int value:
        """

        self.com_object.ReportOutPutFormat = value

    @property
    def report_path(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReportPath() As CATBSTR
                |     Returns or sets the Report output path.

        :return: str
        """

        return self.com_object.ReportPath

    @report_path.setter
    def report_path(self, value: str):
        """
        :param str value:
        """

        self.com_object.ReportPath = value

    @property
    def report_show_result(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReportShowResult() As CatShowResultType
                |     Returns or sets the option for sorting the report.
                | 
                |     0
                |         ByRule 
                |     1
                |         ByObject 
                |     2
                |         ByState

        :return: int
        """

        return self.com_object.ReportShowResult

    @report_show_result.setter
    def report_show_result(self, value: int):
        """
        :param int value:
        """

        self.com_object.ReportShowResult = value

    @property
    def rule_base_edition(self) -> 'ExpertRuleBase':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RuleBaseEdition() As ExpertRuleBase (Read Only)
                |     Returns the editable object corresponding to this rulebase. Be careful
                |     that, according to your licence, or the type of rulebase you're handling, you
                |     may not have the right to edit the rulebase.
                | 
                |     Parameters:
                | 
                |         oRuleBaseEdition
                |             the editable object corresponding to this rulebase
                |             
                | 
                |     Returns:
                |         the editable object corresponding to this rulebase. 
                |     Example:
                | 
                |          Dim aRBEdition As CATIAExpertRuleBase
                |          Set aRBEdition = aRBRuntime.RuleBaseEdition
                | 
                |          If not(aRBEdition is Nothing) Then
                |            ' .. action on the editable rulebase
                |          End if

        :return: ExpertRuleBase
        """
        from pycatia3dx.know_how.expert_rule_base import ExpertRuleBase
        return ExpertRuleBase(self.com_object.RuleBaseEdition)

    @property
    def rule_set(self) -> ExpertRuleSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RuleSet() As ExpertRuleSet (Read Only)
                |     Returns the Set linked to the RuleBase. This is the main RuleSet that
                |     contains all the RuleBase components.

        :return: ExpertRuleSet
        """

        return ExpertRuleSet(self.com_object.RuleSet)

    @property
    def solve_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SolveType() As CatSolveType
                |     Returns or sets the solve option.

        :return: int
        """

        return self.com_object.SolveType

    @solve_type.setter
    def solve_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SolveType = value

    @property
    def text_visualization(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TextVisualization() As CatVisualizationType
                |     Returns or sets the Report option for visualization.
                | 
                |     0
                |         Passed 
                |     1
                |         Failed 
                |     2
                |         Both

        :return: int
        """

        return self.com_object.TextVisualization

    @text_visualization.setter
    def text_visualization(self, value: int):
        """
        :param int value:
        """

        self.com_object.TextVisualization = value

    @property
    def working_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property WorkingMode() As CatWorkingMode
                |     Returns or sets the WorkingMode option.
                | 
                |     0
                |         WholeObjects 
                |     1
                |         OccurenceObjects 
                |     2
                |         PLMObjects 
                |     3
                |         AllOccurenceObjects

        :return: int
        """

        return self.com_object.WorkingMode

    @working_mode.setter
    def working_mode(self, value: int):
        """
        :param int value:
        """

        self.com_object.WorkingMode = value

    def accurate_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AccurateType() As CATBSTR
                |     Returns as a string the type of component.
                | 
                |     Returns:
                |         A string among ("ExpertRuleBase", "ExpertRuleBaseRuntime")

        :return: str
        """
        return self.com_object.AccurateType()

    def add_fact(self, i_fact: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddFact(AnyObject iFact)
                |     Adds new fact to the rule base resolution.
                | 
                |     Parameters:
                | 
                |         iFact
                |             Fact to be added 
                | 
                |     Example:
                | 
                |          Dim aRuleBaseSet as ExpertRuleBasesSet
                |          Set aRuleBaseSet  = ...
                |          Dim rulebase as ExpertRuleBaseRuntime
                |          Set rulebase = aRuleBaseSet.Collection.Item("RuleBase")
                | 
                |          Dim part1 as Part
                |          Set part1 = ...
                |          Dim pad3 as Shape
                |          Set pad3 = part1.MainBody.Shapes.Item("Pad3")
                |          rulebase.AddFact (pad3)

        :param AnyObject i_fact:
        :return: None
        """
        return self.com_object.AddFact(i_fact.com_object)

    def add_root_of_facts(self, i_root_facts: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddRootOfFacts(AnyObject iRootFacts)
                |     Adds a new root of facts to the rule base.
                | 
                |     Parameters:
                | 
                |         iRootFacts
                |             root of facts to be added.

        :param AnyObject i_root_facts:
        :return: None
        """
        return self.com_object.AddRootOfFacts(i_root_facts.com_object)

    def deduce(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Deduce()
                |     Launch a Forward chaining Solve on the current RuleBase. 
                | Example:
                | 
                |      Dim aRuleBaseSet as ExpertRuleBasesSet
                |      Set aRuleBaseSet  = ...
                |      Dim rulebase as ExpertRuleBaseRuntime
                |      Set rulebase = aRuleBaseSet.Collection.Item("RuleBase")
                |      rulebase.Deduce ()
                |      
                | 
                |     To operate this solve, you must have the Knowledge Expert Runtime license.

        :return: None
        """
        return self.com_object.Deduce()

    def fingerprint(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Fingerprint() As boolean
                |     Returns the Fingerprint information. The fingerprint indicates
                |     if the last result of the rulebase is relevant regarding to
                |     the objects the rule base has checked. In other words, if the
                |     part has evolved since last Deduce, the fingerprint is false.
                |     Be careful : on volatile rulebases ( ExpertRuleBase.VolatileCopy ),
                |     it raises an error.
                | 
                |     Returns:
                |         Fingerprint information

        :return: bool
        """
        return self.com_object.Fingerprint()

    def get_number_of_roots_of_facts(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfRootsOfFacts() As long
                |     Retrieves the number of roots of facts of the rule base.
                | 
                |     Returns:
                |         Number of roots of facts.

        :return: int
        """
        return self.com_object.GetNumberOfRootsOfFacts()

    def get_roots_of_facts(self, o_roots_of_facts: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetRootsOfFacts(CATSafeArrayVariant oRootsOfFacts)
                |     Retrieves all the roots of facts from the rule base.
                |
                |     Parameters:
                |
                |         oRootsOfFacts
                |             array of roots of facts.

        :param tuple o_roots_of_facts:
        :return: None
        """
        return self.com_object.GetRootsOfFacts(o_roots_of_facts)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_roots_of_facts'
        # vba_code = """
        # Public Function get_roots_of_facts(expert_rule_base_runtime)
        #     Dim oRootsOfFacts (2)
        #     expert_rule_base_runtime.GetRootsOfFacts oRootsOfFacts
        #     get_roots_of_facts = oRootsOfFacts
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def import_(self, i_rule_set: ExpertRuleSet, i_force: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Import(ExpertRuleSet iRuleSet,boolean iForce)
                |     Import from RuleSet.
                | 
                |     Parameters:
                | 
                |         iRuleSet
                |             CATIAExpertRuleSet : the RuleSet user want to import. 
                |         iForce
                |             Boolean : if True (= 1), then if imported rules already
                |             exist in target representation, rules of target representation are replaced.
                | 
                |         To operate this import, you must have the Knowledge Expert Runtime
                |         license.

        :param ExpertRuleSet i_rule_set:
        :param bool i_force:
        :return: None
        """
        return self.com_object.Import(i_rule_set.com_object, i_force)

    def reload_fact(self, i_fact: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReloadFact(AnyObject iFact)
                |     Reloads a fact in the rule base resolution.
                | 
                |     Parameters:
                | 
                |         iFact
                |             Fact to be reloaded 
                | 
                |     Example:
                | 
                |          Dim aRuleBaseSet as ExpertRuleBasesSet
                |          Set aRuleBaseSet  = ...
                |          Dim rulebase as ExpertRuleBaseRuntime
                |          Set rulebase = aRuleBaseSet.Collection.Item("RuleBase")
                | 
                |          Dim part1 as Part
                |          Set part1 = ...
                |          Dim pad3 as Shape
                |          Set pad3 = part1.MainBody.Shapes.Item("Pad3")
                |          rulebase.ReloadFact (pad3)

        :param AnyObject i_fact:
        :return: None
        """
        return self.com_object.ReloadFact(i_fact.com_object)

    def remove_fact(self, i_fact: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveFact(AnyObject iFact)
                |     Removes a fact from the rule base resolution.
                | 
                |     Parameters:
                | 
                |         iFact
                |             Fact to be removed 
                | 
                |     Example:
                | 
                |          Dim aRuleBaseSet as ExpertRuleBasesSet
                |          Set aRuleBaseSet  = ...
                |          Dim rulebase as ExpertRuleBaseRuntime
                |          Set rulebase = aRuleBaseSet.Collection.Item("RuleBase")
                | 
                |          Dim part1 as Part
                |          Set part1 = ...
                |          Dim pad3 as Shape
                |          Set pad3 = part1.MainBody.Shapes.Item("Pad3")
                |          rulebase.RemoveFact (pad3)

        :param AnyObject i_fact:
        :return: None
        """
        return self.com_object.RemoveFact(i_fact.com_object)

    def remove_root_of_facts(self, i_root_facts: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveRootOfFacts(AnyObject iRootFacts)
                |     Removes a root of facts from the rule base.
                | 
                |     Parameters:
                | 
                |         iRootFacts
                |             root of facts to be removed.

        :param AnyObject i_root_facts:
        :return: None
        """
        return self.com_object.RemoveRootOfFacts(i_root_facts.com_object)

    def report(self, really_start_browser: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Report(boolean reallyStartBrowser)
                |     Launch a Report. The default output format is HTML
                | 
                |     Parameters:
                | 
                |         reallyStartBrowser
                |             Boolean : if True (= 1), then the browser is started on the report To operate this solve, you must have the Knowledge Expert Runtime license.

        :param bool really_start_browser:
        :return: None
        """
        return self.com_object.Report(really_start_browser)

    def solve(self, i_complete_solve: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Solve(boolean iCompleteSolve)
                |     Launch a Forward chaining Solve on the current RuleBase.
                | 
                |     Parameters:
                | 
                |         iCompleteSolve
                |             Boolean : if False (= 0), use this value when you use AddFact 
                |         Example:
                | 
                |              Dim aRuleBaseSet as ExpertRuleBasesSet
                |              Set aRuleBaseSet  = ...
                |              Dim rulebase as ExpertRuleBaseRuntime
                |              Set rulebase = aRuleBaseSet.Collection.Item("RuleBase")
                |              rulebase.Solve(false) ()
                |              
                | 
                |         To operate this solve, you must have the Knowledge Expert Runtime
                |         license.

        :param bool i_complete_solve:
        :return: None
        """
        return self.com_object.Solve(i_complete_solve)

    def solve_with_load(self, i_complete_solve: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SolveWithLoad(boolean iCompleteSolve)
                |     Launch a Forward chaining Solve on the current RuleBase. All
                |     representations not loaded will be loaded.
                | 
                |     Parameters:
                | 
                |         iCompleteSolve
                |             Boolean : if False (= 0), use this value when you use AddFact 
                |         Example:
                | 
                |              Dim aRuleBaseSet as ExpertRuleBasesSet
                |              Set aRuleBaseSet  = ...
                |              Dim rulebase as ExpertRuleBaseRuntime
                |              Set rulebase = aRuleBaseSet.Collection.Item("RuleBase")
                |              rulebase.SolveWithLoad(false) ()
                |              
                | 
                |         To operate this solve, you must have the Knowledge Expert Runtime
                |         license.

        :param bool i_complete_solve:
        :return: None
        """
        return self.com_object.SolveWithLoad(i_complete_solve)

    def synchronize_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func SynchronizeStatus() As boolean
                |     Returns the Synchronize information. The synchronize status
                |     indicates for a linked rule base if the rulebase is synchronized.
                |     Be careful : on volatile rulebases ( ExpertRuleBase.VolatileCopy ),
                |     it raises an error.
                | 
                |     Returns:
                |         Synchronize status

        :return: bool
        """
        return self.com_object.SynchronizeStatus()

    def __repr__(self):
        return f'ExpertRuleBaseRuntime(name="{self.name}")'
