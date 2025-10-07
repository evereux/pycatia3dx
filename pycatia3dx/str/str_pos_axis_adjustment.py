"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.parameter import Parameter
from pycatia3dx.system.any_object import AnyObject


class StrPosAxisAdjustment(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     StrPosAxisAdjustment
                | 
                | Object to access a volatile parameter group for the positioning strategy axis
                | adjustment This interface is used for Standard Opening Positioning Strategy
                | specification data.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def role(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Role() As CATBSTR (Read Only)
                |     Returns the role of this parameter. The role is specific to the element
                |     from which this interface was retrieved.
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the role of the parameter.
                |              
                | 
                |              Dim ObjStrStandardPosStrategyParameters As
                |              StrStandardPosStrategyParameters
                |              Set ObjStrStandardPosStrategyParameters = ObjStrOpeningsMgr.GetStandardPositioningStrategyParms(StdPosStrategyName)
                |              Dim ObjStrPosAxisAdjustment As
                |              StrPosAxisAdjustment
                |              Set ObjStrPosAxisAdjustment = ObjStrStandardPosStrategyParameters.Item(1)
                |              If (TypeName(ObjStrPosAxisAdjustment) = "StrPosAxisAdjustment") Then
                |                  StrRole = ObjStrPosAxisAdjustment.Role
                |              End If

        :return: str
        """

        return self.com_object.Role

    def get_angle_parameter(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAngleParameter() As Parameter
                |     Returns the CKE parameter for axis rotation (around Z).
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the parameter for axis
                |              rotation.
                |              
                | 
                |              Set AngleParm = ObjStrPosAxisAdjustment.GetAngleParameter

        :return: Parameter
        """
        return Parameter(self.com_object.GetAngleParameter())

    def get_u_shift_parameter(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetUShiftParameter() As Parameter
                |     Returns the CKE parameter for position U shift (along the final axis
                |     X).
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the position U shift
                |              parameter.
                |              
                | 
                |              Set UShiftParm = ObjStrPosAxisAdjustment.GetUShiftParameter

        :return: Parameter
        """
        return Parameter(self.com_object.GetUShiftParameter())

    def get_v_shift_parameter(self) -> Parameter:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVShiftParameter() As Parameter
                |     Returns the CKE parameter for position V shift (along the final axis
                |     Y).
                | 
                |     Example:
                | 
                | 
                |              This example retrieves the position V shift
                |              parameter.
                |              
                | 
                |              Set VShiftParm = ObjStrPosAxisAdjustment.GetVShiftParameter

        :return: Parameter
        """
        return Parameter(self.com_object.GetVShiftParameter())

    def __repr__(self):
        return f'StrPosAxisAdjustment(name="{ self.name }")'
