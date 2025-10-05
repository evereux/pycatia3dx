"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrManufacturingFastener(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrManufacturingFastener
                | 
                | Represents an object that is Manufacturing Fastener Role: To manage
                | Manufacturing Fasteners
                | 
                | See also:
                |     DrManufacturingFastener
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def create_user_parameter(self, i_name: str, i_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub CreateUserParameter(CATBSTR iName,long iType)
                |     Create a parameter of specified type.
                | 
                |     Parameters:
                | 
                |         iName
                |             The name of the parameter. 
                |         iType
                |             The type of the parameter. 0 - String 1 - Integer 2 - Length 3 -
                |             Angle 4 - Real 5 - Bool

        :param str i_name:
        :param int i_type:
        :return: None
        """
        return self.com_object.CreateUserParameter(i_name, i_type)

    def get3_d_rep(self, oh3_d_rep: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Get3DRep(AnyObject oh3DRep)
                |     Get the 3D representation
                | 
                |     Parameters:
                | 
                |         oh3DRep
                |             The associated 3D Part

        :param AnyObject oh3_d_rep:
        :return: None
        """
        return self.com_object.Get3DRep(oh3_d_rep.com_object)

    def get_boolean_value(self, i_parameter_name: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetBooleanValue(CATBSTR iParameterName) As boolean
                |     Get the value of the parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The boolean value. 
                |         iParameterName
                |             parameter name.

        :param str i_parameter_name:
        :return: bool
        """
        return self.com_object.GetBooleanValue(i_parameter_name)

    def get_fastener(self, oh_geometry: AnyObject, oh_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetFastener(AnyObject ohGeometry,AnyObject ohProduct)
                |     Get the Geometry or design fastener.
                | 
                |     Parameters:
                | 
                |         ohGeometry
                |             Geometry pointed by the fastener. It can be a design point or a PLM
                |             fastener object. 
                |         ohProduct
                |             Product containing the geometry. NULL_var in case of PLM fastener
                |             object.

        :param AnyObject oh_geometry:
        :param AnyObject oh_product:
        :return: None
        """
        return self.com_object.GetFastener(oh_geometry.com_object, oh_product.com_object)

    def get_integer_value(self, i_parameter_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetIntegerValue(CATBSTR iParameterName) As long
                |     Get the value of the parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The integer value. 
                |         iParameterName
                |             parameter name.

        :param str i_parameter_name:
        :return: int
        """
        return self.com_object.GetIntegerValue(i_parameter_name)

    def get_listof_user_names(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetListofUserNames() As CATSafeArrayVariant
                |     Get the list of User parameters.
                | 
                |     Parameters:
                | 
                |         oListNames
                |             The names of user parameters. 
                |         oListTypes
                |             The types of user parameters. 0 - String 1 - Integer 2 - Length 3 -
                |             Angle 4 - Real 5 - Bool

        :return: tuple
        """
        return self.com_object.GetListofUserNames()

    def get_listof_user_types(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetListofUserTypes() As CATSafeArrayVariant

        :return: tuple
        """
        return self.com_object.GetListofUserTypes()

    def get_position(self, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetPosition(double X,double Y,double Z,double Yaw,double Pitch,double
                | Roll)
                |     Get the position.
                | 
                |     Parameters:
                | 
                |         oPosition
                |             The position of Manufacturing Fastener.

        :param float x:
        :param float y:
        :param float z:
        :param float yaw:
        :param float pitch:
        :param float roll:
        :return: None
        """
        return self.com_object.GetPosition(x, y, z, yaw, pitch, roll)

    def get_string_value(self, i_parameter_name: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetStringValue(CATBSTR iParameterName) As CATBSTR
                |     Get the value of the parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The string value. 
                |         iParameterName
                |             parameter name.

        :param str i_parameter_name:
        :return: str
        """
        return self.com_object.GetStringValue(i_parameter_name)

    def get_tail_frame_position(self, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub GetTailFramePosition(double X,double Y,double Z,double Yaw,double
                | Pitch,double Roll)
                |     Get the Tail frame position in absolute coords.
                | 
                |     Parameters:
                | 
                |         X
                |             The X coord of the position in absolute coordinates
                |             
                |         Y
                |             The Y coord of the position in absolute coordinates
                |             
                |         Z
                |             The Z coord of the position in absolute coordinates
                |             
                |         Yaw
                |             The Yaw of the position in absolute coordinates 
                |         Pitch
                |             The Pitch of the position in absolute coordinates 
                |         Roll
                |             The Roll of the position in absolute coordinates

        :param float x:
        :param float y:
        :param float z:
        :param float yaw:
        :param float pitch:
        :param float roll:
        :return: None
        """
        return self.com_object.GetTailFramePosition(x, y, z, yaw, pitch, roll)

    def get_user_access(self, i_parameter_name: str) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetUserAccess(CATBSTR iParameterName) As long
                |     Get the user access/editability/visibility flag of the
                |     parameter.
                | 
                |     Parameters:
                | 
                |         oUserAccess
                |             The user access/editability flag 1->Editable, 0->Noneditable,
                |             -1->Hidden 
                |         iParameterName
                |             parameter name.

        :param str i_parameter_name:
        :return: int
        """
        return self.com_object.GetUserAccess(i_parameter_name)

    def get_value(self, i_parameter_name: str) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func GetValue(CATBSTR iParameterName) As double
                |     Get the value of the parameter.
                | 
                |     Parameters:
                | 
                |         oValue
                |             The double value. 
                |         iParameterName
                |             parameter name.

        :param str i_parameter_name:
        :return: float
        """
        return self.com_object.GetValue(i_parameter_name)

    def set3_d_rep(self, ih3_d_rep: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Set3DRep(AnyObject ih3DRep)
                |     Set the 3D representation
                | 
                |     Parameters:
                | 
                |         ih3DRep
                |             The 3D Part that needs to be set

        :param AnyObject ih3_d_rep:
        :return: None
        """
        return self.com_object.Set3DRep(ih3_d_rep.com_object)

    def set_boolean_value(self, i_parameter_name: str, i_value: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetBooleanValue(CATBSTR iParameterName,boolean iValue)
                |     Set the value of the parameter.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             parameter name. 
                |         iValue
                |             The boolean value.

        :param str i_parameter_name:
        :param bool i_value:
        :return: None
        """
        return self.com_object.SetBooleanValue(i_parameter_name, i_value)

    def set_design_point(self, ih_point: AnyObject, ih_product: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetDesignPoint(AnyObject ihPoint,AnyObject ihProduct)
                |     Set the link to Design Point
                | 
                |     Parameters:
                | 
                |         ihPoint
                |             The design point 
                |         ihProduct
                |             Product containing the design Point

        :param AnyObject ih_point:
        :param AnyObject ih_product:
        :return: None
        """
        return self.com_object.SetDesignPoint(ih_point.com_object, ih_product.com_object)

    def set_fastener(self, ih_fastener: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetFastener(AnyObject ihFastener)
                |     Set the link to PLM fastener
                | 
                |     Parameters:
                | 
                |         ihFastener
                |             PLM fastener object

        :param AnyObject ih_fastener:
        :return: None
        """
        return self.com_object.SetFastener(ih_fastener.com_object)

    def set_integer_value(self, i_parameter_name: str, i_value: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetIntegerValue(CATBSTR iParameterName,long iValue)
                |     Set the integer value of the parameter.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             parameter name. 
                |         iValue
                |             The integer value.

        :param str i_parameter_name:
        :param int i_value:
        :return: None
        """
        return self.com_object.SetIntegerValue(i_parameter_name, i_value)

    def set_position_offset(self, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetPositionOffset(double X,double Y,double Z,double Yaw,double Pitch,double
                | Roll)
                |     Set the position offset.
                | 
                |     Parameters:
                | 
                |         iOffset
                |             The position offset.

        :param float x:
        :param float y:
        :param float z:
        :param float yaw:
        :param float pitch:
        :param float roll:
        :return: None
        """
        return self.com_object.SetPositionOffset(x, y, z, yaw, pitch, roll)

    def set_string_value(self, i_parameter_name: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetStringValue(CATBSTR iParameterName,CATBSTR iValue)
                |     Set the value of the parameter.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             parameter name. 
                |         iValue
                |             The string value.

        :param str i_parameter_name:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetStringValue(i_parameter_name, i_value)

    def set_tail_frame_offset(self, x: float, y: float, z: float, yaw: float, pitch: float, roll: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetTailFrameOffset(double X,double Y,double Z,double Yaw,double
                | Pitch,double Roll)
                |     Set the Tail frame offset.
                | 
                |     Parameters:
                | 
                |         X
                |             The X coord w.r.t design position 
                |         Y
                |             The Y coord w.r.t design position 
                |         Z
                |             The Z coord w.r.t design position 
                |         Yaw
                |             The Yaw w.r.t design position 
                |         Pitch
                |             The Pitch w.r.t design position 
                |         Roll
                |             The Roll w.r.t design position

        :param float x:
        :param float y:
        :param float z:
        :param float yaw:
        :param float pitch:
        :param float roll:
        :return: None
        """
        return self.com_object.SetTailFrameOffset(x, y, z, yaw, pitch, roll)

    def set_user_access(self, i_parameter_name: str, i_user_access: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetUserAccess(CATBSTR iParameterName,long iUserAccess)
                |     Set the user access/editability/visibility flag of the
                |     parameter.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             parameter name. 
                |         iUserAccess
                |             The user access/editability flag 1->Editable, 0->Noneditable,
                |             -1->Hidden

        :param str i_parameter_name:
        :param int i_user_access:
        :return: None
        """
        return self.com_object.SetUserAccess(i_parameter_name, i_user_access)

    def set_value(self, i_parameter_name: str, i_value: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub SetValue(CATBSTR iParameterName,double iValue)
                |     Set the value of the parameter.
                | 
                |     Parameters:
                | 
                |         iParameterName
                |             parameter name. 
                |         iValue
                |             The double/integer value.

        :param str i_parameter_name:
        :param float i_value:
        :return: None
        """
        return self.com_object.SetValue(i_parameter_name, i_value)

    def update(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Update()
                |     Update the Manufacturing Fastener if something is out of date

        :return: None
        """
        return self.com_object.Update()

    def __repr__(self):
        return f'DrManufacturingFastener(name="{ self.name }")'
