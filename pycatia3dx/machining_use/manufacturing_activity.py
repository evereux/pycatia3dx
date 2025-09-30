"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingActivity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingActivity
                | 
                | Interface dedicated to manufacturing operation management.
                | Role: This interface offers services mainly to manage links with the tool and
                | the manufacturing or design feature
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def check_tool_changes(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CheckToolChanges()
                |     Check Tool Changes on Activity

        :return: None
        """
        return self.com_object.CheckToolChanges()

    def get_authorized_father_activity(self, i_type: str, o_father: AnyObject, o_father_child: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAuthorizedFatherActivity(CATBSTR iType,AnyObject oFather,AnyObject
                | oFatherChild)
                |     Get the types of allowed tools of our activity
                | 
                |     Parameters:
                | 
                |         iType
                |             Type 
                |         oFather
                |             return father 
                |         oFatherChild
                |             the father child

        :param str i_type:
        :param AnyObject o_father:
        :param AnyObject o_father_child:
        :return: None
        """
        return self.com_object.GetAuthorizedFatherActivity(i_type, o_father.com_object, o_father_child.com_object)

    def get_comment(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetComment() As CATBSTR
                |     Get comment on activity.
                |     Role: Get comment on activity.
                | 
                |     Parameters:
                | 
                |         oComment
                |             [out] activity's comment 
                | 
                |     Returns:
                |         S_OK Succeded

        :return: str
        """
        return self.com_object.GetComment()

    def get_feature(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFeature() As AnyObject
                |     Returns the manufacturing feature or design feature associated with the
                |     manufacturing operation.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetFeature())

    def get_feature_in_context(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFeatureInContext() As AnyObject
                |     Returns the manufacturing feature associated with the manufacturing
                |     operation.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetFeatureInContext())

    def get_part_operation(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPartOperation() As AnyObject
                |     Retrieves the part operation of the Activity.
                | 
                |     Parameters:
                | 
                |         oSetup
                |             The Setup of the activity

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetPartOperation())

    def get_pattern_usage(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPatternUsage() As AnyObject
                |     Get the pattern usage of the activity.
                |     Role: Get the pattern usage of the activity.
                | 
                |     Parameters:
                | 
                |         oPatternUsage
                |             [out] Activity's pattern usage 
                | 
                |     Returns:
                |         S_OK Succeded

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetPatternUsage())

    def get_program(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetProgram() As AnyObject
                |     Retrieves the Program of the Activity.
                | 
                |     Parameters:
                | 
                |         oProgram
                |             The Program of the activity

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetProgram())

    def get_tool(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTool() As AnyObject
                |     Returns the tool associated with the manufacturing operation.

        :return: AnyObject
        """
        return AnyObject(self.com_object.GetTool())

    def get_tool_and_assembly(self, o_tool: AnyObject, o_assembly: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetToolAndAssembly(AnyObject oTool,AnyObject oAssembly)
                |     Returns the tool and the tool assembly associated with the manufacturing
                |     operation.
                | 
                |     Parameters:
                | 
                |         oTool
                |             The tool 
                |         oAssembly
                |             The tool assembly

        :param AnyObject o_tool:
        :param AnyObject o_assembly:
        :return: None
        """
        return self.com_object.GetToolAndAssembly(o_tool.com_object, o_assembly.com_object)

    def is_active(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsActive() As boolean
                |     Return if activity is active or not
                | 
                |     Parameters:
                | 
                |         oIsActive
                |             0 if not active else 1 if active 
                | 
                |     Returns:
                |         S_OK Succeded

        :return: bool
        """
        return self.com_object.IsActive()

    def set_comment(self, i_comment: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetComment(CATBSTR iComment)
                |     Set comment on activity.
                |     Role: Set comment on activity.
                | 
                |     Parameters:
                | 
                |         iComment
                |             [in] Comment to define 
                | 
                |     Returns:
                |         S_OK Succeded

        :param str i_comment:
        :return: None
        """
        return self.com_object.SetComment(i_comment)

    def set_feature(self, i_feature: AnyObject, i_context: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFeature(AnyObject iFeature,AnyObject iContext)
                |     Assign a feature to a Manufacturing Operation.
                | 
                |     Parameters:
                | 
                |         iFeature
                |             The feature to be assigned. It can be a design feature, or a
                |             Manufacturing feature like Pattern or Machinable feature.
                |             
                |         iContext
                |             The product that contains the feature itself (case of a design
                |             feature) or the geometry pointed by the Manufacturing Feature.

        :param AnyObject i_feature:
        :param AnyObject i_context:
        :return: None
        """
        return self.com_object.SetFeature(i_feature.com_object, i_context.com_object)

    def set_pattern_usage(self, i_pattern_usage: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPatternUsage(AnyObject iPatternUsage)
                |     Set the pattern usage of the activity.
                |     Role: Set the pattern usage of the activity.
                | 
                |     Parameters:
                | 
                |         iPatternUsage
                |             [in] Given pattern usage 
                | 
                |     Returns:
                |         S_OK Succeded

        :param AnyObject i_pattern_usage:
        :return: None
        """
        return self.com_object.SetPatternUsage(i_pattern_usage.com_object)

    def set_tool(self, i_tool: AnyObject, i_check_tool_changes: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTool(AnyObject iTool,boolean iCheckToolChanges)
                |     Associates the tool with the manufacturing operation.
                | 
                |     Parameters:
                | 
                |         iTool
                |             The tool 
                |         iCheckToolChanges
                |             A flag to indicate whether the tool changes should be
                |             checked
                |             Legal values:
                | 
                |                 TRUE: the check will be performed
                |                 FALSE: no check

        :param AnyObject i_tool:
        :param bool i_check_tool_changes:
        :return: None
        """
        return self.com_object.SetTool(i_tool.com_object, i_check_tool_changes)

    def __repr__(self):
        return f'ManufacturingActivity(name="{ self.name }")'
