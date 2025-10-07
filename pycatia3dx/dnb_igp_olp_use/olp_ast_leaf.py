"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.dnb_igp_olp_use.olp_ast_node import OLPAstNode


class OLPAstLeaf(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpAstLeaf
                | 
                | Represents a leaf node of the Abstract Syntax Tree (AST).
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | An OLP AST is a parsed version of a robot program in the native language of the
                | robot. A leaf is a node which has no children.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def editable_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EditableType() As DELOlpEditableType
                |     Editor type to create for a node that can be edited in NRL teach.

        :return: DELOlpEditableType
        """

        return self.com_object.EditableType

    @editable_type.setter
    def editable_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.EditableType = value

    @property
    def editable_type_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EditableTypeString() As CATBSTR
                |     Editor type to create for a node that can be edited in NRL teach. Valid
                |     string values are "None", "String", "Int", "Double", "Combo" and
                |     "EditableCombo".

        :return: str
        """

        return self.com_object.EditableTypeString

    @editable_type_string.setter
    def editable_type_string(self, value: str):
        """
        :param str value:
        """

        self.com_object.EditableTypeString = value

    @property
    def editor_id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EditorId() As CATBSTR
                |     Editor ID for a node that can be edited in NRL teach. Set to a value that
                |     identifies the type of attribute being edited. When the user modifies the
                |     value, the translator can query the editor ID to know how to process the
                |     modification.

        :return: str
        """

        return self.com_object.EditorId

    @editor_id.setter
    def editor_id(self, value: str):
        """
        :param str value:
        """

        self.com_object.EditorId = value

    @property
    def hidden_instructions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HiddenInstructions() As CATSafeArrayVariant
                |     The list of instructions that should be hidden in the teach table. These
                |     instructions will be hidden in teach when custom columns are enabled. This is a
                |     subset of OlpAstNode.Instructions. If no instructions have been set on this
                |     node, the associated hidden instructions are retrieved from the parent. Each
                |     value in the array is a OlpInstruction.

        :return: tuple
        """

        return self.com_object.HiddenInstructions

    @hidden_instructions.setter
    def hidden_instructions(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.HiddenInstructions = value

    @property
    def id(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Id() As CATBSTR
                |     Identifies the function of the node or otherwise helps the translator find
                |     a node among its siblings.
                |     For example an id could be used to identify a part of a motion statement
                |     (speed) or to identify the variable name in a list of declarations.

        :return: str
        """

        return self.com_object.Id

    @id.setter
    def id(self, value: str):
        """
        :param str value:
        """

        self.com_object.Id = value

    @property
    def instructions(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Instructions() As CATSafeArrayVariant
                |     The DELMIA instructions associated with this AST node. If it has not been
                |     set, the associated instructions are retrieved from the parent. Each value in
                |     the array is a OlpInstruction.

        :return: tuple
        """

        return self.com_object.Instructions

    @instructions.setter
    def instructions(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.Instructions = value

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As DELOlpAstNodeType
                |     Classifies the language element stored in this node.
                |     For example: keyword, variable, comment, statement, or header.

        :return: DELOlpAstNodeType
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    @property
    def value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Value() As CATBSTR
                |     The text contained by this node.

        :return: str
        """

        return self.com_object.Value

    @value.setter
    def value(self, value: str):
        """
        :param str value:
        """

        self.com_object.Value = value

    def clone(self) -> OLPAstNode:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Clone() As OlpAstNode
                |     Create a deep copy of the node.
                |     A node cannot have 2 parents, so you must clone it before adding it to
                |     another branch.
                | 
                |     Returns:
                |         The new copy.

        :return: OLPAstNode
        """
        return OLPAstNode(self.com_object.Clone())

    def export_to_file(self, i_file_path: str, i_pretty_print: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ExportToFile(CATBSTR iFilePath,boolean iPrettyPrint)
                |     Exports the node in XML form at the desired filepath.
                | 
                |     Parameters:
                | 
                |         iFilePath
                |             The path to the export file 
                |         iPrettyPrint
                |             Pretty print the outputted XML 

        :param str i_file_path:
        :param bool i_pretty_print:
        :return: None
        """
        return self.com_object.ExportToFile(i_file_path, i_pretty_print)

    def __repr__(self):
        return f'OLPAstLeaf(name="{ self.name }")'
