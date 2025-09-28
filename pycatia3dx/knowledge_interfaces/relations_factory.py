"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.check import Check
from pycatia3dx.knowledge_interfaces.design_table import DesignTable
from pycatia3dx.knowledge_interfaces.formula import Formula
from pycatia3dx.knowledge_interfaces.knowledge_factory import KnowledgeFactory
from pycatia3dx.knowledge_interfaces.law import Law
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.knowledge_interfaces.rels_set import RelsSet
from pycatia3dx.knowledge_interfaces.rule import Rule
from pycatia3dx.knowledge_interfaces.set_of_equation import SetOfEquation
from pycatia3dx.system.any_object import AnyObject


class RelationsFactory(KnowledgeFactory):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeFactory
                |                         RelationsFactory
                | 
                | Factory for creating relations and relations sets under a specified
                | root.
                | 
                | See also:
                |     RelsSet.Factory
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_check(self, i_name: str, i_comment: str, i_check_body: str) -> Check:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateCheck(CATBSTR iName,CATBSTR iComment,CATBSTR iCheckBody) As
                | Check
                |     Creates a check. The following example shows how to create a check which
                |     checks if a given mass is less than 10kg. The mass should be defined
                |     previously:
                | 
                |      Dim relFact As RelationsFactory
                |      Set relFact = ...
                |      Dim mass As RealParam
                |      Set mass = ...
                |      Dim maximummass As Check
                |      Set maximummass = relFact.CreateCheck
                |                         ("maximummass",
                |                          "Ensures that mass is less than 10
                |                          kg",
                |                          "mass<10kg")
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the check 
                |         iComment
                |             Comment 
                |         iCheckBody
                |             Body of the check 
                | 
                |     Returns:
                |         The created check This method requires the KWA license (Knowledge
                |         Advisor).

        :param str i_name:
        :param str i_comment:
        :param str i_check_body:
        :return: Check
        """
        return Check(self.com_object.CreateCheck(i_name, i_comment, i_check_body))

    def create_design_table(self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_rep_ref: AnyObject) -> DesignTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateDesignTable(CATBSTR iName,CATBSTR iComment,boolean
                | iCopyMode,AnyObject iSheetRepRef) As DesignTable
                |     Creates a vertical design table (DT).
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the DT 
                |         iComment
                |             Comment 
                |         iCopyMode
                |             Local copy of values or not 
                |         iSheetRepRef
                |             Representation reference where to seek for values. It is a
                |             CATIAVPMRepReference. 
                | 
                |     Returns:
                |         The created DT

        :param str i_name:
        :param str i_comment:
        :param bool i_copy_mode:
        :param AnyObject i_sheet_rep_ref:
        :return: DesignTable
        """
        return DesignTable(self.com_object.CreateDesignTable(i_name, i_comment, i_copy_mode, i_sheet_rep_ref.com_object))

    def create_formula(self, i_name: str, i_comment: str, i_output_parameter: Parameter, i_formula_body: str) -> Formula:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateFormula(CATBSTR iName,CATBSTR iComment,Parameter
                | iOutputParameter,CATBSTR iFormulaBody) As Formula
                |     Creates a formula.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the formula 
                |         iComment
                |             Comment 
                |         iOutputParameter
                |             Parameter to be valuated by the formula 
                |         iFormulaBody
                |             Body of the formula 
                | 
                |     Returns:
                |         The created formula

        :param str i_name:
        :param str i_comment:
        :param Parameter i_output_parameter:
        :param str i_formula_body:
        :return: Formula
        """
        return Formula(self.com_object.CreateFormula(i_name, i_comment, i_output_parameter.com_object, i_formula_body))

    def create_horizontal_design_table(self, i_name: str, i_comment: str, i_copy_mode: bool, i_sheet_rep_ref: AnyObject) -> DesignTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateHorizontalDesignTable(CATBSTR iName,CATBSTR iComment,boolean
                | iCopyMode,AnyObject iSheetRepRef) As DesignTable
                |     Creates a horizontal design table (DT).
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the DT 
                |         iComment
                |             Comment 
                |         iCopyMode
                |             Local copy of values or not 
                |         iSheetRepRef
                |             Representation reference where to seek for values. It is a
                |             CATIAVPMRepReference. 
                | 
                |     Returns:
                |         The created DT

        :param str i_name:
        :param str i_comment:
        :param bool i_copy_mode:
        :param AnyObject i_sheet_rep_ref:
        :return: DesignTable
        """
        return DesignTable(self.com_object.CreateHorizontalDesignTable(i_name, i_comment, i_copy_mode, i_sheet_rep_ref.com_object))

    def create_law(self, i_name: str, i_comment: str, i_law_body: str) -> Law:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateLaw(CATBSTR iName,CATBSTR iComment,CATBSTR iLawBody) As
                | Law
                |     Creates a law.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the law 
                |         iComment
                |             Comment 
                |         iLawBody
                |             Body of the law 
                | 
                |     Returns:
                |         The created law

        :param str i_name:
        :param str i_comment:
        :param str i_law_body:
        :return: Law
        """
        return Law(self.com_object.CreateLaw(i_name, i_comment, i_law_body))

    def create_program(self, i_name: str, i_comment: str, i_program_body: str) -> Rule:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateProgram(CATBSTR iName,CATBSTR iComment,CATBSTR iProgramBody) As
                | Rule
                |     Creates a rule.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the rule 
                |         iComment
                |             Comment 
                |         iProgramBody
                |             Body of the rule 
                | 
                |     Returns:
                |         The created rule This method requires the KWA license (Knowledge
                |         Advisor).

        :param str i_name:
        :param str i_comment:
        :param str i_program_body:
        :return: Rule
        """
        return Rule(self.com_object.CreateProgram(i_name, i_comment, i_program_body))

    def create_relations_set(self, i_name: str) -> RelsSet:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateRelationsSet(CATBSTR iName) As RelsSet
                |     Creates a set of relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the set of relations 
                | 
                |     Returns:
                |         The created set of relations This method requires the KWA license
                |         (Knowledge Advisor).

        :param str i_name:
        :return: RelsSet
        """
        return RelsSet(self.com_object.CreateRelationsSet(i_name))

    def create_set_of_equations(self, i_name: str, i_comment: str, i_set_of_equations_body: str) -> SetOfEquation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateSetOfEquations(CATBSTR iName,CATBSTR iComment,CATBSTR
                | iSetOfEquationsBody) As SetOfEquation
                |     Creates a set of equations (SoE).
                | 
                |     Parameters:
                | 
                |         iName
                |             Name of the SoE 
                |         iComment
                |             Comment 
                |         iSetOfEquationsBody
                |             Body of the SoE 
                | 
                |     Returns:
                |         The created SoE This method requires the KWA license (Knowledge
                |         Advisor).

        :param str i_name:
        :param str i_comment:
        :param str i_set_of_equations_body:
        :return: SetOfEquation
        """
        return SetOfEquation(self.com_object.CreateSetOfEquations(i_name, i_comment, i_set_of_equations_body))

    def __repr__(self):
        return f'RelationsFactory(name="{ self.name }")'
