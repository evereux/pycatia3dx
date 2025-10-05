"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class TagPoint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     TagPoint
                | 
                | Interface representing a Tag.
                | 
                | Role: This interface is used to retrieve/assign the attributes from the
                | tag.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Axis() As CATSafeArrayVariant
                |     This property returns and sets the relative location of the tag w.r.t to
                |     ist logical owner.
                | 
                |     Returns:
                |         oAxis The Axis of the tag. 
                |     Parameters:
                | 
                |         iAxis
                |             The Axis of the tag. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objTag As TagPoint
                |                   ......
                |         Dim oAxis
                |         oAxis = objTag.Axis

        :return: tuple
        """

        return self.com_object.Axis

    @axis.setter
    def axis(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.Axis = value

    @property
    def type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CATBSTR
                |     This property returns and sets the Type of the tag.
                | 
                |     Returns:
                |         oType The Type of the tag. 
                |     Parameters:
                | 
                |         iType
                |             The Type of the tag. 
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objTag As TagPoint
                |                   ......
                |         Dim oType
                |         oType = objTag.Type

        :return: str
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: str):
        """
        :param str value:
        """

        self.com_object.Type = value

    def get_absolute_axis(self, i_context: AnyObject, i_tag_owner: AnyObject) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAbsoluteAxis(AnyObject iContext,AnyObject iTagOwner) As
                | CATSafeArrayVariant
                |     Retrieves the underlying axis of the Tag. This will return the Tag's
                |     location wrt the specified context If no context is specified, this will return
                |     the Tag's location wrt the global context
                | 
                |     Parameters:
                | 
                |         iContext
                |             The context in which Tag's location is required 
                |         iTagOwner
                |             Occurrence of the Tag owner product in the root context.
                |             
                | 
                |     Returns:
                |         oAxis The underlying Axis. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTag As TagPoint
                |                   ......
                |         Dim iContext, iTagOwner
                |                   ......
                |         Dim oAbsAxis(0 To 5)
                |         Call objTag.GetAbsoluteAxis(iContext, iTagOwner,
                |         oAbsAxis)

        :param AnyObject i_context:
        :param AnyObject i_tag_owner:
        :return: tuple
        """
        return self.com_object.GetAbsoluteAxis(i_context.com_object, i_tag_owner.com_object)

    def get_name(self, o_prefix: str, o_index: str, o_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetName(CATBSTR oPrefix,CATBSTR oIndex,CATBSTR oSuffix)
                |     Retrieves the name of the tag.
                | 
                |     Parameters:
                | 
                |         oPrefix
                |             The Prefix used in the tag name. 
                |         oIndex
                |             The Index used in the tag name. 
                |         oSuffix
                |             The Suffix used in the tag name. 
                | 
                |     Returns:
                |         oAxis The underlying Axis. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTag As TagPoint
                |                   ......
                |         Dim oPrefix As String, oIndex As String, oSuffix As
                |         String
                |         Call objTag.GetName(oPrefix, oIndex, oSuffix)

        :param str o_prefix:
        :param str o_index:
        :param str o_suffix:
        :return: None
        """
        return self.com_object.GetName(o_prefix, o_index, o_suffix)

    def set_absolute_axis(self, i_axis: tuple, i_context: AnyObject, i_tag_owner: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAbsoluteAxis(CATSafeArrayVariant iAxis,AnyObject iContext,AnyObject
                | iTagOwner)
                |     Sets axis of the Tag. This will set the Tag's location wrt the specified
                |     context If no context is specified, this will set the Tag's location wrt the
                |     global context
                | 
                |     Returns:
                |         iAxis The underlying Axis. 
                |     Parameters:
                | 
                |         iContext
                |             The context in which Tag's location is required 
                |         iTagOwner
                |             Occurrence of the Tag owner product in the root context.
                |             
                | 
                |     Example:
                | 
                |            
                | 
                |            Dim objTag As TagPoint
                |         Dim iContext, iTagOwner
                |                   ......
                |         Dim oAbsAxis(0 To 5)
                |                   ......
                |         Call oTag.SetAbsoluteAxis(iContext, iTagOwner,
                |         oAbsAxis)
                |                   ......

        :param tuple i_axis:
        :param AnyObject i_context:
        :param AnyObject i_tag_owner:
        :return: None
        """
        return self.com_object.SetAbsoluteAxis(i_axis, i_context.com_object, i_tag_owner.com_object)

    def set_name(self, i_prefix: str, i_index: str, i_suffix: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetName(CATBSTR iPrefix,CATBSTR iIndex,CATBSTR iSuffix)
                |     Sets the name of the tag.
                | 
                |     Parameters:
                | 
                |         iPrefix
                |             The Prefix used in the tag name. 
                |         iIndex
                |             The Index used in the tag name. 
                |         iSuffix
                |             The Suffix used in the tag name. 
                | 
                |     Returns:
                |         oAxis The underlying Axis. 
                |     Example:
                | 
                |            
                | 
                |            Dim objTag As TagPoint
                |                   ......
                |         Dim oPrefix As String, oIndex As String, oSuffix As
                |         String
                |                   ......
                |         Call objTag.SetName(oPrefix, oIndex, oSuffix)

        :param str i_prefix:
        :param str i_index:
        :param str i_suffix:
        :return: None
        """
        return self.com_object.SetName(i_prefix, i_index, i_suffix)

    def __repr__(self):
        return f'TagPoint(name="{ self.name }")'
