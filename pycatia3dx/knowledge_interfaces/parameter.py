"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 12:30:08.885021

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.relation import Relation
from pycatia3dx.system.any_object import AnyObject


class Parameter(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     Parameter
                | 
                | Represents the parameter.
                | It can be computed from a relation: formula, program, or check. It is an
                | abstract object which is not intended to be created as such, but from which the
                | integer, boolean, real, and string parameters derive. Here is an example to
                | create one:
                | 
                |  Dim aParmFact As ParametersFactory
                |  Set aParmFact = ...
                |  Dim density As RealParam
                |  Set density = aParmFact.CreateReal("density", 2.5)
                |  
                | 
                | See also:
                |     ParametersFactory
    
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
                |     Returns or sets the parameter object comment.

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
                |     Returns the context of the parameter : a part, a product,
                |     a drafting, a process, depending on where the parameter is.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Context)

    @property
    def hidden(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Hidden() As boolean
                |     Returns or sets whether the parameter is hidden or should be hidden. or not.

        :return: bool
        """

        return self.com_object.Hidden

    @hidden.setter
    def hidden(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Hidden = value

    @property
    def is_true_parameter(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property IsTrueParameter() As boolean (Read Only)
                |     Returns a boolean saying if the parameter is a true one (real, dimension,
                |     string, etc.) or a geometrical one (isolated points, curves, surfaces).

        :return: bool
        """

        return self.com_object.IsTrueParameter

    @property
    def optional_relation(self) -> Relation:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property OptionalRelation() As Relation (Read Only)
                |     Returns the relation that can be used to compute the
                |     parameter.
                |     As this relation might not exist, NULL may be returned, so a test is
                |     required.
                | 
                |     Example:
                |         This example checks if there is a relation to compute the param1
                |         parameter, and if no relation exists, displays a message
                |         box:
                | 
                |          Set param1_rel = param1.OptionalRelation
                |          If param1_rel is Nothing Then
                |               MsgBox "No relation to compute param1"
                |          End If

        :return: Relation
        """

        return Relation(self.com_object.OptionalRelation)

    @property
    def read_only(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property ReadOnly() As boolean (Read Only)
                |     Returns whether the parameter can be modified.
                | 
                |     Example:
                |         This example checks if the param1 parameter can be modified, and if it
                |         cannot, displays a message box:
                | 
                |          If ( param1.ReadOnly ) Then
                |               MsgBox "No way to change param1"
                |          End If

        :return: bool
        """

        return self.com_object.ReadOnly

    @property
    def renamed(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property Renamed() As boolean (Read Only)
                |     Returns a boolean saying if the parameter is a renamed parameter or not.

        :return: bool
        """

        return self.com_object.Renamed

    @property
    def user_access_mode(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Property UserAccessMode() As long (Read Only)
                |     Returns the user access mode of the parameter. 
                | 
                | 0
                |     Read only parameter (cannot be destroyed). 
                | 1
                |     Read/write parameter (cannot be destroyed). 
                | 2
                |     User parameter (can be read, written and destroyed).

        :return: int
        """

        return self.com_object.UserAccessMode

    def rename(self, i_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub Rename(CATBSTR iName)
                |     Renames the parameter.
                | 
                |     Parameters:
                | 
                |         iName
                |             The new name of the parameter. If iName contains "Local:" prefix
                |             the rename will affect the local name. If not, it will affect the global name.
                |             
                | 
                |     Example:
                |         This example renames the param1 parameter to
                |         PartSeatbodyMinimumThickness:
                | 
                |          Call param1.Rename("PartSeatbodyMinimumThickness")

        :param str i_name:
        :return: None
        """
        return self.com_object.Rename(i_name)

    def valuate_from_string(self, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Sub ValuateFromString(CATBSTR iValue)
                |     Valuates a parameter using a string as input. The string depends on
                |     parameter nature :
                | 
                |     "True" or "False" for Boolean
                | 
                |     a numerical value for Integer or Real
                | 
                |     a numerical value with or without a unit for Dimension
                | 
                |     Parameters:
                | 
                |         iValue
                |             The value to assign to the dimension parameter 
                | 
                |     Example:
                |         This example sets the value of the existing dimension parameter to a
                |         new value:
                | 
                |          dimension.ValuateFromString("300mm")

        :param str i_value:
        :return: None
        """
        return self.com_object.ValuateFromString(i_value)

    def value_as_string(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 12:30:08.885021)
                | Func ValueAsString() As CATBSTR
                |     Returns the value of the parameter as a string. The string format is
                |     controlled by the "Parameters and Measures" settings.
                | 
                |     Returns:
                |         returned value. 
                | 
                | Example:
                |     This example gets the value of the existing dimension parameter and shows
                |     it in a message box
                | 
                |      Dim str
                |      str = dimension.ValueAsString
                |      MsgBox str

        :return: str
        """
        return self.com_object.ValueAsString()

    def __repr__(self):
        return f'Parameter(name="{ self.name }")'
