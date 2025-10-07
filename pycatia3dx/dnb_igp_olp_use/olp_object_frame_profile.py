"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_controller import OLPController
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile
from pycatia3dx.dnb_igp_olp_use.olp_transform import OLPTransform


class OLPObjectFrameProfile(OLPProfile):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DNBIgpOlpUseItf.OlpProfile
                |                         OlpObjectFrameProfile
                | 
                | An object frame profile used for translating a robot program.
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_attached_device(self) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttachedDevice() As OlpController
                |     Gets the associated device that the object frame is attached
                |     to.
                |     This controlling device might not exist. In this case, this property will
                |     be NULL
                | 
                |     Returns:
                |         The attached device controller. It might be nothing if there is no
                |         device attached.

        :return: OLPController
        """
        return OLPController(self.com_object.GetAttachedDevice())

    def get_fixed_tcp(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFixedTCP() As boolean
                |     Get whether this object frame profile is used for fixed TCP moves.

        :return: bool
        """
        return self.com_object.GetFixedTCP()

    def get_movable(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMovable() As boolean
                |     Get whether this object frame profile is movable.
                |     A movable object frame is one that is moved by an aux device of the robot
                |     during simulation.

        :return: bool
        """
        return self.com_object.GetMovable()

    def get_transform(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTransform(DELOlpPositionRef iOrigin) As OlpTransform
                |     Get the transform that represents the object frame
                |     location.
                |     For normal (fixed) object frames profiles, this is a transformation from
                |     the world, robot base, etc. For object frames that are used in a fixed TCP
                |     motion, this offset is from the mount plate of the robot. An object frame
                |     should not be used with both a fixed TCP motion and a non-fixed TCP
                |     motion.
                |     If the object frame profile has not been set (the X,Y,Z,Yaw,Pitch, and Roll
                |     values are a zero), then the object frame is assumed to be a the origin of
                |     whatever coordinate system you specify. This means that if the translator
                |     downloads in delOlpRobotBase coordinates and the object profile has not been
                |     set, then all motion positions will be the transform from the robot base to the
                |     target location.
                |     The delOlpRobotBase reference origin can only be used with object frame
                |     profiles which are zero. This is because delOlpRobotBase coordinates move with
                |     the robot if the robot is mounted on a rail. DELMIA does not currently allow
                |     for object frames to be defined relative to a moving object for Cartesian
                |     targets. Instead you should use delOlpRailOrigin or request that the user set
                |     the object frame profile to all zeros. As a result, you must use the same
                |     reference frame when getting/setting the position from
                |     OlpRobotMotionTarget.GetTransform as you do here.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The location that the transform is relative to.
                |             For profiles used in a fixed TCP motion this must be delOlpMount.
                |             For normal profiles, it can be any other value. 
                | 
                |     Returns:
                |         The object frame.

        :param int i_origin:
        :return: OLPTransform
        """
        return OLPTransform(self.com_object.GetTransform(i_origin))

    def set_attached_device(self, i_attached_device: OLPController, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAttachedDevice(OlpController iAttachedDevice,boolean
                | iMatch)
                |     Sets the associated device the object frame is attached
                |     to.
                | 
                |     Parameters:
                | 
                |         iAttachedDevice
                |             The device. 
                |         iMatch
                |             Whether to include the device when deciding if an existing profile
                |             should be reused.

        :param OLPController i_attached_device:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAttachedDevice(i_attached_device.com_object, i_match)

    def set_fixed_tcp(self, i_is_fixed_tcp: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFixedTCP(boolean iIsFixedTCP,boolean iMatch)
                |     Set whether this object frame profile is used for fixed TCP
                |     moves.
                | 
                |     Parameters:
                | 
                |         iIsFixedTCP
                |             Object frame profile is for a fixed tool.
                |         iMatch
                |             Should the parameter be used when deciding if an existing profile
                |             should be reused.

        :param bool i_is_fixed_tcp:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetFixedTCP(i_is_fixed_tcp, i_match)

    def set_movable(self, i_is_movable: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMovable(boolean iIsMovable,boolean iMatch)
                |     Set whether this object frame profile is movable.
                |     A movable object frame is one that is moved by an aux device of the robot
                |     during simulation.
                | 
                |     Parameters:
                | 
                |         iIsFixedTCP
                |             Object frame profile is movable.
                |         iMatch
                |             Should the parameter be used when deciding if an existing profile
                |             should be reused.

        :param bool i_is_movable:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetMovable(i_is_movable, i_match)

    def set_transform(self, i_origin: int, i_frame: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransform(DELOlpPositionRef iOrigin,OlpTransform
                | iFrame)
                |     Set the transform that represents the object frame
                |     location.
                |     See GetTransform for details.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The location that the transform is relative to.
                |             For profiles used in a fixed TCP motion this must be delOlpMount.
                |             For normal profiles, it can be any other value. 
                |         iFrame
                |             The object frame. 

        :param int i_origin:
        :param OLPTransform i_frame:
        :return: None
        """
        return self.com_object.SetTransform(i_origin, i_frame.com_object)

    def __repr__(self):
        return f'OLPObjectFrameProfile(name="{ self.name }")'
