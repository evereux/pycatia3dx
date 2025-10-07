"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class OLPTransform(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     OlpTransform
                | 
                | Represents an interface that handles basic parameters of a
                | transform.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | A new transform can be created with
                | OlpTranslatorHelper.CreateTransform.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

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

    def get_axis_angle(self, o_vx: float, o_vy: float, o_vz: float, o_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAxisAngle(double oVx,double oVy,double oVz,double
                | oAngle)
                |     Method returns the Euler Axis-Angle representation of the
                |     transform.
                |     This method assumes returns an unary axis vector and an angle in
                |     rad
                |     Role NA
                | 
                |     Parameters:
                | 
                |         oVx
                |             X component of rotation vector 
                |         oVy
                |             Y component of rotation vector 
                |         oVz
                |             Z component of rotation vector 
                |         oAngle
                |             Angle (in radians) to rotate around Vx,Vy,Vz

        :param float o_vx:
        :param float o_vy:
        :param float o_vz:
        :param float o_angle:
        :return: None
        """
        return self.com_object.GetAxisAngle(o_vx, o_vy, o_vz, o_angle)

    def get_oat(self, o_o: float, o_a: float, o_t: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetOAT(double oO,double oA,double oT)
                |     Method returns orientation of the transform in form of Kawasaki
                |     OAT
                |     Role: Used in robot programming languages such as AS by
                |     Kawasaki.
                | 
                |     Parameters:
                | 
                |         oO
                |             O component of orientation in degrees 
                |         oA
                |             A component of orientation in degrees 
                |         oT
                |             T component of orientation in degrees

        :param float o_o:
        :param float o_a:
        :param float o_t:
        :return: None
        """
        return self.com_object.GetOAT(o_o, o_a, o_t)

    def get_quaternions(self, o_q1: float, o_q2: float, o_q3: float, o_q4: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetQuaternions(double oQ1,double oQ2,double oQ3,double
                | oQ4)
                |     Method returns orientation of the transform in form of
                |     quaternions.
                |     Role: Used in robot programming languages such as Rapid by
                |     ABB.
                | 
                |     Parameters:
                | 
                |         oQ1
                |             1st quaternion value. (W) 
                |         oQ2
                |             2nd quaternion value. (X) 
                |         oQ3
                |             3rd quaternion value. (Y) 
                |         oQ4
                |             4th quaternion value. (Z)

        :param float o_q1:
        :param float o_q2:
        :param float o_q3:
        :param float o_q4:
        :return: None
        """
        return self.com_object.GetQuaternions(o_q1, o_q2, o_q3, o_q4)

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

    def get_rpy2(self, o_roll: float, o_pitch: float, o_yaw: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRPY2(double oRoll,double oPitch,double oYaw)
                |     Method returns Roll, Pitch and Yaw values of the
                |     transform.
                |     Role: Used to get alternative rpy solution as needed by
                |     Kobelco.
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
        return self.com_object.GetRPY2(o_roll, o_pitch, o_yaw)

    def get_rotation_vector(self, o_vx: float, o_vy: float, o_vz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRotationVector(double oVx,double oVy,double oVz)
                |     Method returns the rotation vector components of the
                |     transform.
                |     Rotation Vector is a vector with the same orientation as
                |     the
                |     Euler axis representation of the rotation matrix, with its
                |     length equal to the angle of rotation in radians
                |     Role: Used for UniversalRobots rotation representation
                | 
                |     Parameters:
                | 
                |         oVx
                |             X component of rotation vector 
                |         oVy
                |             Y component of rotation vector 
                |         oVz
                |             Z component of rotation vector

        :param float o_vx:
        :param float o_vy:
        :param float o_vz:
        :return: None
        """
        return self.com_object.GetRotationVector(o_vx, o_vy, o_vz)

    def get_xyz(self, o_x: float, o_y: float, o_z: float) -> None:
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

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :return: None
        """
        return self.com_object.GetXYZ(o_x, o_y, o_z)

    def get_zyz(self, o_z1: float, o_y: float, o_z2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetZYZ(double oZ1,double oY,double oZ2)
                |     Method returns orientation of the transform in form of ZYZ Euler
                |     angles
                |     Role: Used in robot programming languages such as Daihen
                |     ASCII.
                | 
                |     Parameters:
                | 
                |         oZ1
                |             Z component of orientation in degrees 
                |         oY
                |             Y component of orientation in degrees 
                |         oZ2
                |             Z component of orientation in degrees

        :param float o_z1:
        :param float o_y:
        :param float o_z2:
        :return: None
        """
        return self.com_object.GetZYZ(o_z1, o_y, o_z2)

    def inverse(self) -> 'OLPTransform':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Inverse() As OlpTransform
                |     Method returns an inverse of the current transform.
                |     Role: The method calculates and returns a transform that is the inverse of
                |     the current transform. Location parameters of the current transform will not be
                |     modified
                | 
                |     Returns:
                |         Transform that is the inverse of the current transform.

        :return: OLPTransform
        """
        return OLPTransform(self.com_object.Inverse())

    def is_equal_to(self, i_transform: 'OLPTransform') -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsEqualTo(OlpTransform iTransform) As boolean
                |     Test if 2 transforms are equivalent.
                |     Role: 2 transforms are equivalent if the positions are within 0.01mm and
                |     the rotation is within 0.01 radians. Two transforms may be equivalent even if
                |     the euler angles are not equal due to the problems of multiple equivalent euler
                |     angle combinations.
                | 
                |     Returns:
                |         TRUE if the transforms are equivalent.

        :param OLPTransform i_transform:
        :return: bool
        """
        return self.com_object.IsEqualTo(i_transform.com_object)

    def multiply(self, i_transform: 'OLPTransform') -> 'OLPTransform':
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Multiply(OlpTransform iTransform) As OlpTransform
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

        :param OLPTransform i_transform:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.Multiply(i_transform.com_object))

    def set_axis_angle(self, i_vx: float, i_vy: float, i_vz: float, i_angle: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAxisAngle(double iVx,double iVy,double iVz,double
                | iAngle)
                |     Method sets the Euler Axis-Angle representation of the
                |     transform.
                |     This method assumes returns an unary axis vector and an angle in
                |     rad
                |     Role NA
                | 
                |     Parameters:
                | 
                |         iVx
                |             X component of rotation vector 
                |         iVy
                |             Y component of rotation vector 
                |         iVz
                |             Z component of rotation vector 
                |         iAngle
                |             Angle (in radians) to rotate around Vx,Vy,Vz

        :param float i_vx:
        :param float i_vy:
        :param float i_vz:
        :param float i_angle:
        :return: None
        """
        return self.com_object.SetAxisAngle(i_vx, i_vy, i_vz, i_angle)

    def set_nsa_vectors(self, i_nx: float, i_ny: float, i_nz: float, i_sx: float, i_sy: float, i_sz: float, i_ax: float, i_ay: float, i_az: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetNSAVectors(double iNx,double iNy,double iNz,double iSx,double iSy,double
                | iSz,double iAx,double iAy,double iAz)
                |     Method sets the vector components of the transform.
                | 
                |     Parameters:
                | 
                |         iNx
                |             X component of x vector 
                |         iNy
                |             Y component of x vector 
                |         iNz
                |             Z component of x vector 
                |         iSx
                |             X component of y vector 
                |         iSy
                |             Y component of y vector 
                |         iSz
                |             Z component of y vector 
                |         iAx
                |             X component of z vector 
                |         iAy
                |             Y component of z vector 
                |         iAz
                |             Z component of z vector

        :param float i_nx:
        :param float i_ny:
        :param float i_nz:
        :param float i_sx:
        :param float i_sy:
        :param float i_sz:
        :param float i_ax:
        :param float i_ay:
        :param float i_az:
        :return: None
        """
        return self.com_object.SetNSAVectors(i_nx, i_ny, i_nz, i_sx, i_sy, i_sz, i_ax, i_ay, i_az)

    def set_oat(self, i_o: float, i_a: float, i_t: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetOAT(double iO,double iA,double iT)
                |     Method sets orientation of the transform in form of Kawasaki
                |     OAT
                |     Role: Used in robot programming languages such as AS by
                |     Kawasaki.
                | 
                |     Parameters:
                | 
                |         iO
                |             O component of orientation in degrees 
                |         iA
                |             A component of orientation in degrees 
                |         iT
                |             T component of orientation in degrees

        :param float i_o:
        :param float i_a:
        :param float i_t:
        :return: None
        """
        return self.com_object.SetOAT(i_o, i_a, i_t)

    def set_quaternions(self, i_q1: float, i_q2: float, i_q3: float, i_q4: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetQuaternions(double iQ1,double iQ2,double iQ3,double
                | iQ4)
                |     Method sets orientation of the transform in form of
                |     quaternions.
                |     Role: Used in robot programming languages such as Rapid by
                |     ABB.
                | 
                |     Parameters:
                | 
                |         iQ1
                |             1st quaternion value. (W) 
                |         iQ2
                |             2nd quaternion value. (X) 
                |         iQ3
                |             3rd quaternion value. (Y) 
                |         iQ4
                |             4th quaternion value. (Z)

        :param float i_q1:
        :param float i_q2:
        :param float i_q3:
        :param float i_q4:
        :return: None
        """
        return self.com_object.SetQuaternions(i_q1, i_q2, i_q3, i_q4)

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

    def set_rotation_vector(self, i_vx: float, i_vy: float, i_vz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRotationVector(double iVx,double iVy,double iVz)
                |     Method sets the rotation vector components of the
                |     transform.
                |     A Rotation Vector is a vector with the same orientation as
                |     the
                |     Euler axis representation of the rotation matrix, with its
                |     length equal to the angle of rotation in radians
                |     Role: Used for UniversalRobots rotation representation
                | 
                |     Parameters:
                | 
                |         iVx
                |             X component of rotation vector 
                |         iVy
                |             Y component of rotation vector 
                |         iVz
                |             Z component of rotation vector

        :param float i_vx:
        :param float i_vy:
        :param float i_vz:
        :return: None
        """
        return self.com_object.SetRotationVector(i_vx, i_vy, i_vz)

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

    def set_zyz(self, i_z1: float, i_y: float, i_z2: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetZYZ(double iZ1,double iY,double iZ2)
                |     Method converts ZYZ angles to Euler angles (RPY) and sets
                |     it
                |     Role: Used in robot programming languages such as Daihen
                |     ASCII.
                | 
                |     Parameters:
                | 
                |         iZ1
                |             Z component of orientation in degrees 
                |         iY
                |             Y component of orientation in degrees 
                |         iZ2
                |             Z component of orientation in degrees 

        :param float i_z1:
        :param float i_y:
        :param float i_z2:
        :return: None
        """
        return self.com_object.SetZYZ(i_z1, i_y, i_z2)

    def __repr__(self):
        return f'OLPTransform(name="{ self.name }")'
