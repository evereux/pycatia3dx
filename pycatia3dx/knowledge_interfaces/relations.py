"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.knowledge_interfaces.check import Check
from pycatia3dx.knowledge_interfaces.design_table import DesignTable
from pycatia3dx.knowledge_interfaces.formula import Formula
from pycatia3dx.knowledge_interfaces.law import Law
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.knowledge_interfaces.relation import Relation
from pycatia3dx.knowledge_interfaces.rule import Rule
from pycatia3dx.knowledge_interfaces.set_of_equation import SetOfEquation
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Relations(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Relations
                | 
                | Represents the collection of relations of the part or the
                | product.
                | 
                | A relation computes values. A relation can belong to one of the following
                | types:
                | 
                | Formula
                |     It combines parameters to compute the value of one output parameter only.
                |     For example, the mass of a cuboid can be the output parameter of a formula,
                |     while the value is computed using the following
                |     parameters:
                | 
                |      
                |      FormulaBody = (height*width*depth)*density
                |      
                | 
                | Program
                |     It combines conditions and actions on parameters to compute one or several
                |     output parameter values. For example, the following is a
                |     program:
                | 
                |      ProgramBody = if (mass>2kg) { depth=2mm length=10mm } else { depth=1mm length=5mm }  
                |      
                | 
                | Check
                |     It only contains conditions on parameter values. For example, the following
                |     is a check:
                | 
                |      CheckBody = mass<10kg
                |      
                | 
                | The parameters should be defined previously.
                | 
                | The following example shows how to retrieve the collection of relations from a
                | newly created 3DShape :
                | 
                |  Dim part As Part
                |  Set part = ...
                |  Dim relations As Relations
                |  Set relations = part.Relations
                |  
                | 
                | See also:
                |     Formula, Rule, Check, DesignTable
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=Relation)
        self.com_object = com_object

    def create_check(self, i_name: str, i_comment: str, i_check_body: str) -> Check:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateCheck(CATBSTR iName,CATBSTR iComment,CATBSTR iCheckBody) As
                | Check
                |     Creates a check relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The check name 
                |         iComment
                |             A description of the check 
                |         iCheckBody
                |             The check definition 
                | 
                |     Returns:
                |         The created check 
                |     Example:
                |         This example creates the maximummass check relation and adds it to the
                |         newly created part:
                | 
                |          Dim part As Part
                |          Set part = ...
                |          Dim massCheck As Check 
                |          Set massCheck    = part.Relations.CreateCheck
                |                              ("maximummass",
                |                               "Ensures that the mass is less than 10
                |                               kg",
                |                              "mass<10kg")
                |          
                | 
                |     This method requires the KWA license (Knowledge Advisor).

        :param str i_name:
        :param str i_comment:
        :param str i_check_body:
        :return: Check
        """
        return Check(self.com_object.CreateCheck(i_name, i_comment, i_check_body))

    def create_design_table_with_rep_ref(
            self,
            i_name: str,
            i_comment: str,
            i_copy_mode: bool,
            i_sheet_ref: AnyObject
    ) -> DesignTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateDesignTableWithRepRef(CATBSTR iName,CATBSTR iComment,boolean
                | iCopyMode,AnyObject iSheetRef) As DesignTable
                |     Creates a design table based on a rep ref of a file organized in a vertical
                |     way.
                | 
                |     Parameters:
                | 
                |         iName
                |             The design table name. 
                |         iComment
                |             A description of the design table. 
                |         iCopyMode
                |             Boolean for copying or not the table content. 
                |         iSheetRef
                |             Representation reference of the file containing the table
                |             
                | 
                |     Returns:
                |         The created design table

        :param str i_name:
        :param str i_comment:
        :param bool i_copy_mode:
        :param AnyObject i_sheet_ref:
        :return: DesignTable
        """
        return DesignTable(
            self.com_object.CreateDesignTableWithRepRef(
                i_name, i_comment, i_copy_mode, i_sheet_ref.com_object
            )
        )

    def create_formula(
            self,
            i_name: str,
            i_comment: str,
            i_output_parameter: Parameter,
            i_formula_body: str
    ) -> Formula:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateFormula(CATBSTR iName,CATBSTR iComment,Parameter
                | iOutputParameter,CATBSTR iFormulaBody) As Formula
                |     Creates a formula relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The formula name 
                |         iComment
                |             A description of the formula 
                |         iOutputParameter
                |             The parameter which stores the result of the formula
                |             
                |         iFormulaBody
                |             The formula definition 
                | 
                |     Returns:
                |         The created formula 
                |     Example:
                |         This example creates the computemass formula relation and adds it to
                |         the newly created part:
                | 
                |          Dim part As Part
                |          Set part = ...
                |          Dim massFormula As Formula
                |          Set massFormula = part.Relations.CreateFormula
                |                             ("computemass",
                |                             "Computes the cuboid mass",
                |                              mass,
                |                             "(height*width*depth)*density")

        :param str i_name:
        :param str i_comment:
        :param Parameter i_output_parameter:
        :param str i_formula_body:
        :return: Formula
        """
        return Formula(self.com_object.CreateFormula(i_name, i_comment, i_output_parameter.com_object, i_formula_body))

    def create_horizontal_design_table_with_rep_ref(
            self, i_name: str,
            i_comment: str,
            i_copy_mode: bool,
            i_sheet_ref: AnyObject
    ) -> DesignTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateHorizontalDesignTableWithRepRef(CATBSTR iName,CATBSTR
                | iComment,boolean iCopyMode,AnyObject iSheetRef) As DesignTable
                |     Creates a design table based on a rep ref of a file organized in a
                |     horizontal way.
                | 
                |     Parameters:
                | 
                |         iName
                |             The design table name 
                |         iComment
                |             A description of the design table 
                |         iCopyMode
                |             Boolean for copying or not the table content 
                |         iSheetRef
                |             Representation reference of the file containing the table
                |             
                | 
                |     Returns:
                |         The created design table

        :param str i_name:
        :param str i_comment:
        :param bool i_copy_mode:
        :param AnyObject i_sheet_ref:
        :return: DesignTable
        """
        return DesignTable(
            self.com_object.CreateHorizontalDesignTableWithRepRef(
                i_name,
                i_comment,
                i_copy_mode,
                i_sheet_ref.com_object
            )
        )

    def create_law(self, i_name: str, i_comment: str, i_law_body: str) -> Law:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateLaw(CATBSTR iName,CATBSTR iComment,CATBSTR iLawBody) As
                | Law
                |     Creates a law relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The law name 
                |         iComment
                |             A description of the law 
                |         iLawBody
                |             The law definition 
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
                |     Creates a program relation and adds it to the part's collection of
                |     relations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The program name 
                |         iComment
                |             A description of the program 
                |         iProgramBody
                |             The program definition 
                | 
                |     Returns:
                |         The created program 
                |     Example:
                |         This example creates the selectdepth program relation and adds it to
                |         the newly created part:
                | 
                |          Dim part As Part
                |          Set part = ...
                |          Dim depthProgram As Program
                |          Set depthProgram = part.Relations.CreateProgram
                |                              ("selectdepth",
                |                              "Select depth with respect to
                |                              mass",
                |                             "if (mass>2kg) { depth=2mm } else { depth=1 mm
                |                             }")
                |          
                | 
                |     This method requires the KWA license (Knowledge Advisor).

        :param str i_name:
        :param str i_comment:
        :param str i_program_body:
        :return: Rule
        """
        return Rule(self.com_object.CreateProgram(i_name, i_comment, i_program_body))

    def create_rule_base(self, i_name: str) -> Relation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateRuleBase(CATBSTR iName) As Relation
                |     Creates a rulebase.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the rulebase. 
                | 
                |     Returns:
                |         The created rulebase. 
                |     See also:
                |         ExpertRuleBase

        :param str i_name:
        :return: Relation
        """
        return Relation(self.com_object.CreateRuleBase(i_name))

    def create_set_of_equations(self, i_name: str, i_comment: str, i_formula_body: str) -> SetOfEquation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func CreateSetOfEquations(CATBSTR iName,CATBSTR iComment,CATBSTR iFormulaBody)
                | As SetOfEquation
                |     Creates a set of equations.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the set of equation. 
                |         iComment
                |             The comment of the set of equation. 
                |         iFormulaBody
                |             The body of the set of equation " a==b+4; c ≤ 90".
                |             
                | 
                |     Returns:
                |         The created set of equations This method requires the KWA license
                |         (Knowledge Advisor).

        :param str i_name:
        :param str i_comment:
        :param str i_formula_body:
        :return: SetOfEquation
        """
        return SetOfEquation(self.com_object.CreateSetOfEquations(i_name, i_comment, i_formula_body))

    def create_set_of_relations(self, i_parent: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub CreateSetOfRelations(AnyObject iParent)
                |     Creates a set of relations and appends it to a parent
                |     object.
                | 
                |     Parameters:
                | 
                |         iParent
                |             The object to which the set is appended This method requires the
                |             KWA license (Knowledge Advisor).

        :param AnyObject i_parent:
        :return: None
        """
        return self.com_object.CreateSetOfRelations(i_parent.com_object)

    def generate_xml_report_for_checks(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub GenerateXMLReportForChecks(CATBSTR iName)
                |     Generates an XML Report on all checks in the current representation
                |     reference.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the XML file

        :param str i_name:
        :return: None
        """
        return self.com_object.GenerateXMLReportForChecks(i_name)

    def item(self, i_index: CATVariant) -> Relation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func Item(CATVariant iIndex) As Relation
                |     Retrieves a relation using its index or its name from the Relations
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the relation to retrieve from the
                |             collection of relations. As a numerics, this index is the rank of the relation
                |             in the collection. The index of the first relation in the collection is 1, and
                |             the index of the last relation is Count. As a string, it is the name you
                |             assigned to the relation using the AnyObject.Name property or when creating the
                |             relation. 
                | 
                |     Returns:
                |         The retrieved relation 
                |     Example:
                |         This example retrieves the last relation in the relations
                |         collection.
                | 
                |          Dim lastRelation As Relation
                |          Set lastRelation = relations.Item(relations.Count)

        :param CATVariant i_index:
        :return: Relation
        """
        return Relation(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Remove(CATVariant iIndex)
                |     Removes a relation from the Relations collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the relation to remove from the collection
                |             of relations. As a numerics, this index is the rank of the relation in the
                |             collection. The index of the first relation in the collection is 1, and the
                |             index of the last relation is Count. As a string, it is the name you assigned
                |             to the relation using the AnyObject.Name property or when creating the
                |             relation. 
                | 
                |     Example:
                |         This example removes the relation named density from the relations
                |         collection.
                | 
                |          relations.Remove("density")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def sub_list(self, i_feature: AnyObject, i_recursively: bool) -> 'Relations':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func SubList(AnyObject iFeature,boolean iRecursively) As
                | Relations
                |     Returns a sub-collection of relations aggregated to an
                |     object.
                | 
                |     Parameters:
                | 
                |         iFeature
                |             The object used to filter the whole relation collection to get
                |             the resulting sub-collection. 
                |         iRecursively
                |             A flag to specify if children parameters are to be searched for in
                |             the returned collection 
                | 
                |     Returns:
                |         The resulting sub-collection 
                |     Example:
                |         This example shows how to get a collection of relations that are under
                |         a Pad
                | 
                |          Dim part As Part
                |          Set part = ...
                |          Dim Relations1 As Relations
                |          Set Relations1 = part.Relations ' gets the collection of relations in the part
                |          Dim Body0 As AnyObject
                |          Set Body0 = part.Bodies.Item ( "MechanicalTool.1" ) 
                |          Dim Pad1 As AnyObject
                |          Set Pad1 = Body0.Shapes.Item ( "Pad.1" ) ' gets the pad Pad.1
                |          Dim Relations2 As Relations
                |          Set Relations2 = Relations1.SubList(Pad1, TRUE) ' gets the collection of relations that are under the pad Pad.1

        :param AnyObject i_feature:
        :param bool i_recursively:
        :return: Relations
        """
        return Relations(self.com_object.SubList(i_feature.com_object, i_recursively))

    def __getitem__(self, n: int) -> Relation:
        if (n + 1) > self.count:
            raise StopIteration

        return Relation(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[Relation]:
        for i in range(self.count):
            yield Relation(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'Relations(name="{self.name}")'
