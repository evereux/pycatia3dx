"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.collection import Collection
from pycatia3dx.dnb_igp_olp_use.olp_ast_leaf import OLPAstLeaf
from pycatia3dx.dnb_igp_olp_use.olp_ast_node import OLPAstNode
from pycatia3dx.types.general import CATVariant


class OLPAstBranch(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     OlpAstBranch
                | 
                | Represents a branch node of the Abstract Syntax Tree (AST).
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | An OLP AST is a parsed version of a robot program in the native language of the
                | robot. A branch is a collection of nodes.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=OLPAstNode)
        self.com_object = com_object

    @property
    def children(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Children() As CATSafeArrayVariant (Read Only)
                |     Returns all children as an array.
                |     Each item in the list is an OlpAstNode. You can also iterate directly on
                |     this branch collection using the syntax. For Each node as OlpAstNode In branch
                |     ... Next

        :return: tuple
        """

        return self.com_object.Children

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
                |     subset of OlpAstNode.Instructions. If it has not been set, the associated
                |     hidden instructions are retrieved from the parent. Each value in the array is a
                |     OlpInstruction.

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
                | Property Value() As CATBSTR (Read Only)
                |     The unparsed text contained by this node and all its children, without line
                |     endings. The value can only be set for leaf nodes.

        :return: str
        """

        return self.com_object.Value

    @property
    def value_with_eol(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ValueWithEOL() As CATBSTR (Read Only)
                |     The unparsed text contained by this node and all its children, with line
                |     endings. The value can only be set for leaf nodes.

        :return: str
        """

        return self.com_object.ValueWithEOL

    def append(self, i_child: OLPAstNode) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Append(OlpAstNode iChild)
                |     Append a child node to this collection.
                |     NULL values are ignored. They are not appended but the function still
                |     succeeds.
                | 
                |     Parameters:
                | 
                |         iChild
                |             The child to append.

        :param OLPAstNode i_child:
        :return: None
        """
        return self.com_object.Append(i_child.com_object)

    def append_eol(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AppendEOL()
                |     Create and append a leaf node whose value is a new line.

        :return: None
        """
        return self.com_object.AppendEOL()

    def append_leaf(self, i_type: int, i_id: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AppendLeaf(DELOlpAstNodeType iType,CATBSTR iID,CATBSTR
                | iValue)
                |     Create and append a leaf node to this collection.
                | 
                |     Parameters:
                | 
                |         iType
                |             The new node's type. 
                |         iID
                |             The new node's ID. 
                |         iValue
                |             The new node's value.

        :param int i_type:
        :param str i_id:
        :param str i_value:
        :return: None
        """
        return self.com_object.AppendLeaf(i_type, i_id, i_value)

    def append_space(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AppendSpace()
                |     Create and append a leaf node whose value is a single space.

        :return: None
        """
        return self.com_object.AppendSpace()

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

    def create_branch(self, i_type: int, i_id: str) -> 'OLPAstBranch':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateBranch(DELOlpAstNodeType iType,CATBSTR iID) As
                | OlpAstBranch
                |     Creates a new branch node. The new node is not added to the children of
                |     this branch.
                | 
                |     Parameters:
                | 
                |         iType
                |             The new node's type. 
                |         iID
                |             The new node's ID. 
                |         oNode
                | 
                |     Returns:
                |         The created node.

        :param int i_type:
        :param str i_id:
        :return: OLPAstBranch
        """
        return OLPAstBranch(self.com_object.CreateBranch(i_type, i_id))

    def create_leaf(self, i_type: int, i_id: str, i_value: str) -> OLPAstLeaf:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateLeaf(DELOlpAstNodeType iType,CATBSTR iID,CATBSTR iValue) As
                | OlpAstLeaf
                |     Creates a new leaf node. The new node is not added to the children of this
                |     branch.
                | 
                |     Parameters:
                | 
                |         iType
                |             The new node's type. 
                |         iID
                |             The new node's ID. 
                |         iValue
                |             The new node's value. 
                |         oNode
                | 
                |     Returns:
                |         The created node.

        :param int i_type:
        :param str i_id:
        :param str i_value:
        :return: OLPAstLeaf
        """
        return OLPAstLeaf(self.com_object.CreateLeaf(i_type, i_id, i_value))

    def exists_child_by_id(self, i_id: str, o_child: OLPAstNode) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ExistsChildByID(CATBSTR iID,OlpAstNode oChild) As boolean
                |     Tests for existence of a child node with given id and if found returns it.
                |     It is assumed that the ID is unique among all children of this
                |     node.
                | 
                |     Parameters:
                | 
                |         iID
                |             The ID of the child to find. 
                |         oChild
                |             The child, if found. 
                | 
                |     Returns:
                |         0 if not found, -1 if found

        :param str i_id:
        :param OLPAstNode o_child:
        :return: bool
        """
        return self.com_object.ExistsChildByID(i_id, o_child.com_object)

    def exists_child_by_type(self, i_type: int, o_child: OLPAstNode) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ExistsChildByType(DELOlpAstNodeType iType,OlpAstNode oChild) As
                | boolean
                |     Tests for existence of a child node with given type and if found returns
                |     it. It is assumed that the ID is unique among all children of this
                |     node.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the child to find. 
                |         oChild
                |             The child, if found. 
                | 
                |     Returns:
                |         0 if not found, -1 if found

        :param int i_type:
        :param OLPAstNode o_child:
        :return: bool
        """
        return self.com_object.ExistsChildByType(i_type, o_child.com_object)

    def exists_children_by_id(self, i_id: str, o_children: tuple) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ExistsChildrenByID(CATBSTR iID,CATSafeArrayVariant oChildren) As
                | boolean
                |     Tests for existence of children with given id and if found returns a list
                |     of nodes.
                | 
                |     Parameters:
                | 
                |         iID
                |             The ID of the children to find. 
                |         oChildren
                |             The children, if found. 
                | 
                |     Returns:
                |         0 if not found, -1 if found

        :param str i_id:
        :param tuple o_children:
        :return: bool
        """
        return self.com_object.ExistsChildrenByID(i_id, o_children)

    def exists_children_by_type(self, i_type: int, o_children: tuple) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ExistsChildrenByType(DELOlpAstNodeType iType,CATSafeArrayVariant
                | oChildren) As boolean
                |     Tests for existence of children with given type and if found returns a list
                |     of nodes.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the children to find. 
                |         oChildren
                |             The children, if found.

        :param int i_type:
        :param tuple o_children:
        :return: bool
        """
        return self.com_object.ExistsChildrenByType(i_type, o_children)

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

    def find_child_by_id(self, i_id: str) -> OLPAstNode:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindChildByID(CATBSTR iID) As OlpAstNode
                |     Finds a child node which has the id and returns it. If a child with that ID
                |     does not exist, an error is generated. It is assumed that the ID is unique
                |     among all children of this node. The ID search is case
                |     insensitive.
                | 
                |     Parameters:
                | 
                |         iID
                |             The ID of the child to find. 
                | 
                |     Returns:
                |         The found child.

        :param str i_id:
        :return: OLPAstNode
        """
        return OLPAstNode(self.com_object.FindChildByID(i_id))

    def find_child_by_type(self, i_type: int) -> OLPAstNode:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindChildByType(DELOlpAstNodeType iType) As OlpAstNode
                |     Finds a child node which has the specified type and returns it. If a child
                |     with that type does not exist, an error is generated. It is assumed that only 1
                |     node has the given type.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the child to find. 
                | 
                |     Returns:
                |         The found child.

        :param int i_type:
        :return: OLPAstNode
        """
        return OLPAstNode(self.com_object.FindChildByType(i_type))

    def find_children_by_id(self, i_id: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindChildrenByID(CATBSTR iID) As CATSafeArrayVariant
                |     Finds each child node which has the id and returns a list of nodes. If a
                |     child with that ID does not exist, an error is generated. The ID search is case
                |     insensitive.
                | 
                |     Parameters:
                | 
                |         iID
                |             The ID of the children to find. 
                | 
                |     Returns:
                |         The found children.

        :param str i_id:
        :return: tuple
        """
        return self.com_object.FindChildrenByID(i_id)

    def find_children_by_type(self, i_type: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindChildrenByType(DELOlpAstNodeType iType) As
                | CATSafeArrayVariant
                |     Finds each child node which has the type and returns a list of nodes. If a
                |     child with that type does not exist, an error is
                |     generated.
                | 
                |     Parameters:
                | 
                |         iType
                |             The type of the children to find. 
                | 
                |     Returns:
                |         The found children.

        :param int i_type:
        :return: tuple
        """
        return self.com_object.FindChildrenByType(i_type)

    def find_grand_child_double_value(self, i_id: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindGrandChildDoubleValue(CATBSTR iID) As double
                |     Finds a child node which has the specified ID and then finds a child of
                |     that node which is of type CONST_DOUBLE and returns the value of that node as a
                |     double.
                |     If the child or grandchild node is not found, or if the value is cannot be
                |     converted to an double, an error is generated. It is assumed that only 1 node
                |     has the given ID or type. The ID search is case
                |     insensitive.
                | 
                |     Parameters:
                | 
                |         iID
                |             The id of the child to find. 
                | 
                |     Returns:
                |         The value of the grandchild node.

        :param str i_id:
        :return: float
        """
        return self.com_object.FindGrandChildDoubleValue(i_id)

    def find_grand_child_int_value(self, i_id: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func FindGrandChildIntValue(CATBSTR iID) As long
                |     Finds a child node which has the specified ID and then finds a child of
                |     that node which is of type CONST_INTEGER and returns the value of that node as
                |     an integer.
                |     If the child or grandchild node is not found, or if the value is cannot be
                |     converted to an integer, an error is generated. It is assumed that only 1 node
                |     has the given ID or type. The ID search is case
                |     insensitive.
                | 
                |     Parameters:
                | 
                |         iID
                |             The id of the child to find. 
                | 
                |     Returns:
                |         The value of the grandchild node.

        :param str i_id:
        :return: int
        """
        return self.com_object.FindGrandChildIntValue(i_id)

    def insert(self, i_relative_child: OLPAstNode, i_before: bool, i_child: OLPAstNode) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Insert(OlpAstNode iRelativeChild,boolean iBefore,OlpAstNode
                | iChild)
                |     Insert a child node to this collection.
                |     NULL values are ignored. They are not inserted but the function still
                |     succeeds.
                | 
                |     Parameters:
                | 
                |         iRelativeChild
                |             The child to insert before or after. If NULL then the child is
                |             inserted at beginning (if iBefore is TRUE), or at the end (if iBefore is
                |             FALSE). 
                |         iBefore
                |             If true iChild is inserted before iRelativeChild, otherwise after.
                |             
                |         iChild
                |             The child to insert.

        :param OLPAstNode i_relative_child:
        :param bool i_before:
        :param OLPAstNode i_child:
        :return: None
        """
        return self.com_object.Insert(i_relative_child.com_object, i_before, i_child.com_object)

    def item(self, i_index: CATVariant) -> OLPAstNode:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As OlpAstNode
                |     Retrieves a child node using its index or its ID.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the ID of the node to retrieve from the collection of
                |             nodes. As a number, this index is the index of the parameter in the collection.
                |             The index of the first parameter in the collection is 1, and the index of the
                |             last parameter is Count. As a string, it is the ID you assigned to the node
                |             using the OlpAstNode.Id property or when the node was created.
                |             
                | 
                |     Returns:
                |         The node retrieved.

        :param CATVariant i_index:
        :return: OLPAstNode
        """
        return OLPAstNode(self.com_object.Item(i_index))

    def remove(self, i_child: OLPAstNode) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(OlpAstNode iChild)
                |     Remove a child node from the branch.
                |     NULL values are ignored. They are not removed but the function still
                |     succeeds.
                | 
                |     Parameters:
                | 
                |         iChild
                |             The child to remove.

        :param OLPAstNode i_child:
        :return: None
        """
        return self.com_object.Remove(i_child.com_object)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAll()
                |     Remove all child nodes from the branch.

        :return: None
        """
        return self.com_object.RemoveAll()

    def __repr__(self):
        return f'OLPAstBranch(name="{self.name}")'
