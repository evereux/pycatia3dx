"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscKinematicsRelations(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscKinematicsRelations
                | 
                | Interface to access the resource symbolic kinematics
                | relations.
                | Role: This interface provides methods to access the kinematics
                | relations.
                | This API manages the different symbolic kinematics relations on a resource
                | controller. There are used to define the formulaes on non-command joint to be
                | fonction of command joints.
                | 
                | Example:
                |     Let assume there is a robot opened as a root entity in a given
                |     editor.
                | 
                |      Dim MainResource As Variant
                |      Set MainResource = CATIA.ActiveEditor.ActiveObject
                | 
                |      Dim MySelectedResource As RscKinematicsRelations
                |      Set MySelectedResource = MainResource.GetItem("CAARscKinematicsRelations")
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def list_non_command_joints(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListNonCommandJoints() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of non-command joint of the current resource that can have
                |     relations. Rigid joints are not included in the output
                |     list.
                | 
                |     Returns:
                |         List of non-command joints managed by the current
                |         resource.
                | 
                |         Example:
                | 
                |          Dim ListJoints 'array for VBScript
                |          ListJoints = MySelectedResource.ListNonCommandJoints
                |          Dim NbJoint As Integer
                |          NbJoint = UBound(ListJoints) + 1
                |          'uncomment next line to display value
                |          'MsgBox ("Number of non-command joint: " &
                |          CStr(NbJoint))
                |          Dim MyJoint
                |          For II = LBound(ListJoints) To UBound(ListJoints)
                |            MyJoint = ListJoints(II)
                |            'uncomment next line to display value
                |            'MsgBox ("My joint name is:" & MyJoint.Name)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListJoints() As Variant 'array for VBA
                |          ListJoints = MySelectedResource.ListNonCommandJoints

        :return: tuple
        """

        return self.com_object.ListNonCommandJoints

    @property
    def list_user_variables_i_ds(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ListUserVariablesIDs() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of existing user variables defined.
                | 
                |     Returns:
                |         The list of user variables defined on the current
                |         resource.
                | 
                |         Example:
                | 
                |          Dim ListUserVarID 'array for VBScript
                |          ListUserVarID = MySelectedResource.ListUserVariablesIDs
                |          Dim NbVariables As Integer
                |          NbVariables = UBound(ListUserVarID) + 1
                |          'uncomment next line to display value
                |          'MsgBox ("Number of user variables: " &
                |          CStr(NbVariables))
                |          Dim UserVarID As String
                |          For II = LBound(ListUserVarID) To UBound(ListUserVarID)
                |            UserVarID = ListUserVarID(II)
                |            'uncomment next line to display value
                |            'MsgBox ("UserVarID:" & UserVarID)
                |          Next
                | 
                |         Note: previous example is for CATScript. In case of VBA, the syntax is
                |         slightly different for array declaration:
                | 
                |          Dim ListUserVarID() As Variant 'array for VBA
                |          ListUserVarID = MySelectedResource.ListUserVariablesIDs

        :return: tuple
        """

        return self.com_object.ListUserVariablesIDs

    @property
    def support_kinematics_relations(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportKinematicsRelations() As boolean (Read Only)
                |     Indicates if the current resource supports symbolic kinematics
                |     relations.
                | 
                |     Parameters:
                | 
                |         oSupportKinematicsRelations
                |             [out] TRUE if the resource node is OK (FALSE otherwise).
                |             
                | 
                |     Returns:
                |         Indicates if the current resource supports symbolic kinematics
                |         relations.

        :return: bool
        """

        return self.com_object.SupportKinematicsRelations

    def clear_joint_relation_expression(self, i_joint: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ClearJointRelationExpression(AnyObject iJoint)
                |     Removes the expression for a given joint.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             [in] Input parameter for the joint retrieved through
                |             ListNonCommandJoints. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not modify to the
                |             data.
                |             E_INVALIDARG in case the argument is not valid.
                |             E_FAIL otherwise.

        :param AnyObject i_joint:
        :return: None
        """
        return self.com_object.ClearJointRelationExpression(i_joint.com_object)

    def create_user_variable_expression(self, i_user_var_id: str, i_expression: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateUserVariableExpression(CATBSTR iUserVarID,CATBSTR
                | iExpression)
                |     Creates a new user variable with its related expression.
                | 
                |     Parameters:
                | 
                |         iUserVarID
                |             [in] String input parameter that must different from
                |             ListUserVariablesIDs. 
                |         iExpression
                |             [in] Expression assigned to the current user variable.
                |             
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not allowed modify to the
                |             data.
                |             E_INVALIDARG in case the argument is not valid.
                |             E_FAIL otherwise.

        :param str i_user_var_id:
        :param str i_expression:
        :return: None
        """
        return self.com_object.CreateUserVariableExpression(i_user_var_id, i_expression)

    def get_joint_relation_expression(self, i_joint: AnyObject) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetJointRelationExpression(AnyObject iJoint) As CATBSTR
                |     Retrieves the expression for a given joint.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             [in] Input parameter for the joint retrieved through
                |             ListNonCommandJoints. 
                |         oExpression
                |             [out] Expression assigned to the current joint. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not allowed to access the
                |             data.
                |             E_FAIL otherwise.

        :param AnyObject i_joint:
        :return: str
        """
        return self.com_object.GetJointRelationExpression(i_joint.com_object)

    def get_user_variable_expression(self, i_user_var_id: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetUserVariableExpression(CATBSTR iUserVarID) As CATBSTR
                |     Retrieves the user variable expression for a given user variable
                |     names.
                | 
                |     Parameters:
                | 
                |         iUserVarID
                |             [in] String input parameter through ListUserVariablesIDs.
                |             
                |         oExpression
                |             [out] Expression assigned to the current user variable.
                |             
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not allowed to access the
                |             data.
                |             E_FAIL otherwise.

        :param str i_user_var_id:
        :return: str
        """
        return self.com_object.GetUserVariableExpression(i_user_var_id)

    def remove_user_variable_expression(self, i_user_var_id: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveUserVariableExpression(CATBSTR iUserVarID)
                |     Removes an existing a new user variable with its related
                |     expression.
                | 
                |     Parameters:
                | 
                |         iUserVarID
                |             [in] String input parameter through ListUserVariablesIDs.
                |             
                |         iExpression
                |             [in] Expression assigned to the current user variable.
                |             
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not allowed modify to the
                |             data.
                |             E_INVALIDARG in case the argument is not valid.
                |             E_FAIL otherwise.

        :param str i_user_var_id:
        :return: None
        """
        return self.com_object.RemoveUserVariableExpression(i_user_var_id)

    def set_joint_relation_expression(self, i_joint: AnyObject, i_expression: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetJointRelationExpression(AnyObject iJoint,CATBSTR
                | iExpression)
                |     Sets the expression for a given joint.
                | 
                |     Parameters:
                | 
                |         iJoint
                |             [in] Input parameter for the joint retrieved through
                |             ListNonCommandJoints. 
                |         iExpression
                |             [in] Expression to assigned to the current joint. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not modify to the
                |             data.
                |             E_INVALIDARG in case the argument is not valid.
                |             E_FAIL otherwise.

        :param AnyObject i_joint:
        :param str i_expression:
        :return: None
        """
        return self.com_object.SetJointRelationExpression(i_joint.com_object, i_expression)

    def set_user_variable_expression(self, i_user_var_id: str, i_expression: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUserVariableExpression(CATBSTR iUserVarID,CATBSTR
                | iExpression)
                |     Retrieves the user variable expression for a given user variable
                |     names.
                | 
                |     Parameters:
                | 
                |         iUserVarID
                |             [in] String input parameter through ListUserVariablesIDs.
                |             
                |         iExpression
                |             [in] Expression assigned to the current user variable.
                |             
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not allowed to modify to the
                |             data.
                |             E_INVALIDARG in case the argument is not valid.
                |             E_FAIL otherwise.

        :param str i_user_var_id:
        :param str i_expression:
        :return: None
        """
        return self.com_object.SetUserVariableExpression(i_user_var_id, i_expression)

    def validate_kinematic_expression(self, i_user_expression: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func ValidateKinematicExpression(CATBSTR iUserExpression) As
                | long
                |     Validates the user variable expression. This method is called by any user
                |     variable edition API. It is meant to help callers understand better the types
                |     of errors.
                | 
                |     Parameters:
                | 
                |         iUserExpression
                |             [in] Expression assigned to the current user variable.
                |             
                |         oErrorCode
                |             [out] Error code indicating the type of error:
                | 
                |                 0: no error
                |                 1:.
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |             S_OK if the operation succeeds
                |             E_ACCESSDENIED in case the user is not allowed to access the
                |             data.
                |             E_FAIL otherwise.

        :param str i_user_expression:
        :return: int
        """
        return self.com_object.ValidateKinematicExpression(i_user_expression)

    def __repr__(self):
        return f'RscKinematicsRelations(name="{ self.name }")'
