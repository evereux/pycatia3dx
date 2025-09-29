"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.knowledge_activate_object import KnowledgeActivateObject
from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class Relation(KnowledgeActivateObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     KnowledgeIDLItf.KnowledgeObject
                |                        
                |                        KnowledgeIDLItf.KnowledgeActivateObject
                |                             Relation
                | 
                | Represents the relation object.
                | It is an abstract object which is not intended to be created as such, but from
                | which the check, design table, formula, rule, objects derive.
                | 
                | See also:
                |     Check, DesignTable, Formula, Rule
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def comment(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Comment() As CATBSTR
                |     Returns or sets the comment associated with the relation. The comment
                |     explains the relation's purpose. It is passed as the second input argument of
                |     the relation creation methods of the Relations collection.
                | 
                |     Example:
                |         This example retrieves the maximummass relation comment and displays it
                |         in a message box:
                | 
                |          relcomment = maximummass.Comment
                |          MsgBox "maximummass comment : " & relcomment

        :return: str
        """

        return self.com_object.Comment

    @comment.setter
    def comment(self, value: str):
        """
        :param str value:
        """

        self.com_object.Comment = value

    @property
    def context(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Context() As AnyObject (Read Only)
                |     Returns the context of the parameter.
                |     The context of a parameter can be a mechanical part, a product, a drafting,
                |     or a process root, depending on where the parameter is.
                | 
                |     Returns:
                |         The context 
                |     See also:
                |         Part, CATIAProduct, CATIADrawing, CATIAProcess

        :return: AnyObject
        """

        return AnyObject(self.com_object.Context)

    @property
    def nb_in_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property NbInParameters() As long (Read Only)
                |     Returns the number of input parameters of the relation.

        :return: int
        """

        return self.com_object.NbInParameters

    @property
    def nb_out_parameters(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property NbOutParameters() As long (Read Only)
                |     Returns the number of output parameters of the relation.
                |     The output parameters of the relation are those constrained by the
                |     relation.

        :return: int
        """

        return self.com_object.NbOutParameters

    @property
    def value(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Value() As CATBSTR (Read Only)
                |     Returns the definition of the relation. It returns an empty string if the
                |     relation is not an expressional one (for example for a design table). The
                |     definition is the body to be executed to compute one or several parameters. It
                |     is passed as the last input argument of the relation creation methods of the
                |     Relations collection.
                | 
                |     Example:
                |         This example retrieves the maximummass relation definition and displays
                |         it in a message box:
                | 
                |          reldef = maximummass.Value
                |          MsgBox "maximummass relation is defined as " & reldef

        :return: str
        """

        return self.com_object.Value

    def get_in_parameter(self, i_index: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetInParameter(long iIndex) As AnyObject
                |     Returns an input parameter of the relation.
                |     This method can return an object that is not a parameter, that is, you
                |     cannot handle it as a Parameter object. For example, in a relation
                |     like
                | 
                |     Area.1 = area(PartBody\\Pad.1\\Sketch.1)
                | 
                |     the object PartBody\\Pad.1\\Sketch.1 is a sketch and not a
                |     parameter.
                |     To use such an object, call the Visual Basic TypeName function to retrieve
                |     its real type.
                | 
                |      Dim objectType
                |      objectType = TypeName(oParameter)
                |      If objectType = "Parameter" Then
                |      ...
                |      
                | 
                |     Parameters:
                | 
                |         iIndex
                | 
                |     Returns:
                |         The searched input parameter index in the relation.
                |         Legal values: 1 ≤ iIndex ≤ NbInParameters

        :param int i_index:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetInParameter(i_index))

    def get_out_parameter(self, i_index: int) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func GetOutParameter(long iIndex) As Parameter
                |     Returns an output parameter of the relation. Use TypeName method on the
                |     returned parameter to get the real type of the parameter.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The searched input parameter index in the
                |             relation.
                |             Legal values: 1 ≤ iIndex ≤ NbOutParameters 
                | 
                |     Returns:
                |         the output parameter

        :param int i_index:
        :return: Parameter
        """
        return Parameter(self.com_object.GetOutParameter(i_index))

    def modify(self, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Modify(CATBSTR iValue)
                |     Modifies the relation.
                | 
                |     Parameters:
                | 
                |         iValue
                |             The new relation value Except on formula, this method requires the
                |             KWA license (Knowledge Advisor).

        :param str i_value:
        :return: None
        """
        return self.com_object.Modify(i_value)

    def rename(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Rename(CATBSTR iName)
                |     Renames the relation.
                | 
                |     Parameters:
                | 
                |         iName
                |             The new relation name

        :param str i_name:
        :return: None
        """
        return self.com_object.Rename(i_name)

    def __repr__(self):
        return f'Relation(name="{self.name}")'
