"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class RscTransform(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     RscTransform
                | 
                | Interface to manipulate transformation for resources.
                | Role: This interface provides methods to access the mathematical transformation
                | commonly used when dealing with resources and their related objects
                | positioning. It provides conversion utilities depending on what is often used
                | in the resource world.
                | 
                | See also:
                |     RscSimulation
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def angular_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AngularTolerance() As double
                |     Manage the angular tolerance for angle comparison. Value is expressed in SI
                |     units (radians). Default value is set to 1e-7.

        :return: float
        """

        return self.com_object.AngularTolerance

    @angular_tolerance.setter
    def angular_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.AngularTolerance = value

    @property
    def is_identity(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsIdentity() As boolean (Read Only)
                |     True if this transform is an identity transform.
                |     X, Y, Z, Yaw, Pitch, and Roll are all zero for an identity transform.

        :return: bool
        """

        return self.com_object.IsIdentity

    @property
    def linear_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LinearTolerance() As double
                |     Manage the linear tolerance for length comparison. Value is expressed in SI
                |     units (meters). Default value is set to 0.1 micron (1e-7).

        :return: float
        """

        return self.com_object.LinearTolerance

    @linear_tolerance.setter
    def linear_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.LinearTolerance = value

    def duplicate(self) -> 'RscTransform':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Duplicate() As RscTransform
                |     Method returns a copy of the current transform.
                |     Role: The method creates a new copy of the current
                |     transform
                | 
                |     Returns:
                |         Transform that is the copy of the current transform.

        :return: RscTransform
        """
        return RscTransform(self.com_object.Duplicate())

    def get_oat(self, o_o: float, o_a: float, o_t: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOAT(double oO,double oA,double oT)
                |     Method returns orientation of the transform in form of Kawasaki
                |     OAT.
                |     Role: Used in robot programming languages such as AS by
                |     Kawasaki.
                | 
                |     Parameters:
                | 
                |         oO
                |             O component of orientation in radians. 
                |         oA
                |             A component of orientation in radians. 
                |         oT
                |             T component of orientation in radians.

        :param float o_o:
        :param float o_a:
        :param float o_t:
        :return: None
        """
        return self.com_object.GetOAT(o_o, o_a, o_t)

    def get_quaternions(self, o_qx: float, o_qy: float, o_qz: float, o_qw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetQuaternions(double oQX,double oQY,double oQZ,double
                | oQW)
                |     Method returns orientation of the transform in form of
                |     quaternions.
                |     Role: Used in robot programming languages such as Rapid by
                |     ABB.
                | 
                |     Parameters:
                | 
                |         oQX
                |             X component of axis of rotation in meters 
                |         oQY
                |             Y component of axis of rotation in meters 
                |         oQZ
                |             X component of axis of rotation in meters 
                |         oQW
                |             Rotation about axis in radians

        :param float o_qx:
        :param float o_qy:
        :param float o_qz:
        :param float o_qw:
        :return: None
        """
        return self.com_object.GetQuaternions(o_qx, o_qy, o_qz, o_qw)

    def get_rpy(self, o_roll: float, o_pitch: float, o_yaw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRPY(double oRoll,double oPitch,double oYaw)
                |     Method returns Roll, Pitch and Yaw values of the
                |     transform.
                | 
                |     Parameters:
                | 
                |         oRoll
                |             Roll angle of the transform in radians 
                |         oPitch
                |             Pitch angle of the transform in radians 
                |         oYaw
                |             Yaw angle of the transform in radians

        :param float o_roll:
        :param float o_pitch:
        :param float o_yaw:
        :return: None
        """
        return self.com_object.GetRPY(o_roll, o_pitch, o_yaw)

    def get_transform_coefficients(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetTransformCoefficients(CATSafeArrayVariant oValues)
                |     Retrieves the coefficients of this DELMIARscTransform in an array[] of
                |     doubles.
                |     If iNbCoeff=12, the array is:
                |     oCoeffa11 a12 a13 u1
                |     a21 a22 a23 u2
                |     a31 a32 a33 u3
                |     and the coefficients are given COLUMN by COLUMN.

        :return: tuple
        """
        return self.com_object.GetTransformCoefficients()
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_transform_coefficients'
        # vba_code = """
        # Public Function get_transform_coefficients(rsc_transform)
        #     Dim oValues (2)
        #     rsc_transform.GetTransformCoefficients oValues
        #     get_transform_coefficients = oValues
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_vector(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetVector(long iType,double oX,double oY,double oZ)
                |     Returns the XYZ vector coordinates of the transform orientation
                |     matrix.
                | 
                |     Parameters:
                | 
                |         iType
                |             Input parameter to indicate which axis:
                | 
                |                 1: X axis
                |                 2: Y axis
                |                 3: Z axis
                | 
                |         oX
                |             Output parameter for the X component of the vector.
                |             
                |         oY
                |             Output parameter for the Y component of the vector.
                |             
                |         oZ
                |             Output parameter for the Z component of the vector.

        :return: tuple
        """
        return self.com_object.GetVector(tuple)

    def get_xyz(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetXYZ(double oX,double oY,double oZ)
                |     Method returns X, Y and Z values of the transform.
                | 
                |     Parameters:
                | 
                |         oX
                |             X coordinate of the transform in meters 
                |         oY
                |             Y coordinate of the transform in meters 
                |         oZ
                |             Z coordinate of the transform in meters

        :return: tuple
        """
        return self.com_object.GetXYZ()

    def get_zyz(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetZYZ(double oZ1,double oY,double oZ2)
                |     Method returns orientation of the transform in form of ZYZ Euler
                |     angles.
                |     Role: Used in robot programming languages such as Daihen
                |     ASCII.
                | 
                |     Parameters:
                | 
                |         oZ1
                |             Z component of orientation in radians. 
                |         oY
                |             Y component of orientation in radians. 
                |         oZ2
                |             Z component of orientation in radians.

        :return: tuple
        """
        return self.com_object.GetZYZ()

    def inverse(self) -> 'RscTransform':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Inverse() As RscTransform
                |     Method returns an inverse of the current transform.
                |     Role: The method calculates and returns a transform that is the inverse of
                |     the current transform. Location parameters of the current transform will not be
                |     modified
                | 
                |     Returns:
                |         Transform that is the inverse of the current transform.

        :return: RscTransform
        """
        return RscTransform(self.com_object.Inverse())

    def is_equal_to(self, i_transform: 'RscTransform') -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsEqualTo(RscTransform iTransform) As boolean
                |     Test if 2 transforms are equivalent.
                |     Role: 2 transforms are equivalent if the positions are within the defined
                |     LinearTolerance and AngularTolerance. Two transforms may be equivalent even if
                |     the euler angles are not equal due to the problems of multiple equivalent euler
                |     angle combinations.
                | 
                |     Returns:
                |         TRUE if the transforms are equivalent.

        :param RscTransform i_transform:
        :return: bool
        """
        return self.com_object.IsEqualTo(i_transform.com_object)

    def multiply(self, i_transform: 'RscTransform') -> 'RscTransform':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Multiply(RscTransform iTransform) As RscTransform
                |     Method performs post-multiplication of the current transform with the
                |     transform passed as an argument.
                |     Role: The method returns a result of multiplication of the current
                |     transform with the transform passed as an argument. Location parameters of the
                |     current transform will not be modified
                | 
                |     Parameters:
                | 
                |         iTransform
                |             Transform to use in post-multiplication 
                | 
                |     Returns:
                |         The result of the multiplication.

        :param RscTransform i_transform:
        :return: RscTransform
        """
        return RscTransform(self.com_object.Multiply(i_transform.com_object))

    def rotate(self, i_type: int, i_rotate_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Rotate(long iType,double iRotateAngle)
                |     Performs a rotation along a given axis.
                | 
                |     Parameters:
                | 
                |         iType
                |             Input parameter to indicate which axis:
                | 
                |                 1: X axis
                |                 2: Y axis
                |                 3: Z axis
                | 
                |         iRotateAngle
                |             Rotation angle to apply, along specified axis.

        :param int i_type:
        :param float i_rotate_angle:
        :return: None
        """
        return self.com_object.Rotate(i_type, i_rotate_angle)

    def set_oat(self, i_o: float, i_a: float, i_t: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOAT(double iO,double iA,double iT)
                |     Method sets orientation of the transform in form of Kawasaki
                |     OAT.
                |     Role: Used in robot programming languages such as AS by
                |     Kawasaki.
                | 
                |     Parameters:
                | 
                |         iO
                |             O component of orientation in radians. 
                |         iA
                |             A component of orientation in radians. 
                |         iT
                |             T component of orientation in radians.

        :param float i_o:
        :param float i_a:
        :param float i_t:
        :return: None
        """
        return self.com_object.SetOAT(i_o, i_a, i_t)

    def set_quaternions(self, i_qx: float, i_qy: float, i_qz: float, i_qw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetQuaternions(double iQX,double iQY,double iQZ,double
                | iQW)
                |     Method sets orientation of the transform in form of
                |     quaternions.
                |     Role: Used in robot programming languages such as Rapid by
                |     ABB.
                | 
                |     Parameters:
                | 
                |         iQX
                |             X component of axis of rotation in meters 
                |         iQY
                |             Y component of axis of rotation in meters 
                |         iQZ
                |             Z component of axis of rotation in meters 
                |         iQW
                |             Rotation about axis in radians

        :param float i_qx:
        :param float i_qy:
        :param float i_qz:
        :param float i_qw:
        :return: None
        """
        return self.com_object.SetQuaternions(i_qx, i_qy, i_qz, i_qw)

    def set_rpy(self, i_roll: float, i_pitch: float, i_yaw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRPY(double iRoll,double iPitch,double iYaw)
                |     Method sets orientation of the transform in RPY format
                | 
                |     Parameters:
                | 
                |         iRoll
                |             Roll angle of the transform in radians 
                |         iPitch
                |             Pitch angle of the transform in radians 
                |         iYaw
                |             Yaw angle of the transform in radians

        :param float i_roll:
        :param float i_pitch:
        :param float i_yaw:
        :return: None
        """
        return self.com_object.SetRPY(i_roll, i_pitch, i_yaw)

    def set_transform_coefficients(self, i_values: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetTransformCoefficients(CATSafeArrayVariant iValues)
                |     Modifies the coefficients of this DELMIARscTransform from an array[] of
                |     doubles.
                |     If iNbCoeff=12, the array is:
                |     iCoeffa11 a12 a13 u1
                |     a21 a22 a23 u2
                |     a31 a32 a33 u3
                |     and the coefficients must be given COLUMN by COLUMN.

        :param tuple i_values:
        :return: None
        """
        return self.com_object.SetTransformCoefficients(i_values)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_transform_coefficients'
        # vba_code = """
        # Public Function set_transform_coefficients(rsc_transform)
        #     Dim iValues (2)
        #     rsc_transform.SetTransformCoefficients iValues
        #     set_transform_coefficients = iValues
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_vector(self, i_type: int, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVector(long iType,double iX,double iY,double iZ)
                |     Sets the XYZ vector coordinates of the transform orientation
                |     matrix.
                | 
                |     Parameters:
                | 
                |         iType
                |             Input parameter to indicate which axis:
                | 
                |                 1: X axis
                |                 2: Y axis
                |                 3: Z axis
                | 
                |         iX
                |             Input parameter for the X component of the vector.
                |             
                |         iY
                |             Input parameter for the Y component of the vector.
                |             
                |         iZ
                |             Input parameter for the Z component of the vector.

        :param int i_type:
        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: None
        """
        return self.com_object.SetVector(i_type, i_x, i_y, i_z)

    def set_xyz(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetXYZ(double iX,double iY,double iZ)
                |     Method set X, Y and Z values of the transform.
                | 
                |     Parameters:
                | 
                |         iX
                |             X coordinate of the transform in meters 
                |         iY
                |             Y coordinate of the transform in meters 
                |         iZ
                |             Z coordinate of the transform in meters 

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: None
        """
        return self.com_object.SetXYZ(i_x, i_y, i_z)

    def __repr__(self):
        return f'RscTransform(name="{self.name}")'
