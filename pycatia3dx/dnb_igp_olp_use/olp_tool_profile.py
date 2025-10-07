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


class OLPToolProfile(OLPProfile):

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
                |                         OlpToolProfile
                | 
                | The tool profile interface used for translating robot
                | programs.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | The behavior of this object depends on where it was retrieved from. If the
                | object was retrieved from an OlpRobotMotion or OlpRobotMotionTarget then this
                | object is used to configure the tool properties of that motion. The parameters
                | specified with the iMatch input equal to TRUE will be used to find an existing
                | profile to reuse for this motion. If no matching profile is found a new one
                | will be created. If the object was retrieved from OlpController.ToolProfileList
                | then any modifications to this object will change an existing or new profile's
                | values directly.
                | 
                | You cannot call Get methods for profiles retrieved from a new OlpRobotMotion or
                | OlpRobotMotionTarget until values have been set.
                | 
                | Any set methods which don't have the iMatch input and the writable properties
                | assume iMatch=FALSE.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def fixed_tcp(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FixedTCP() As boolean
                |     Get/Set whether this tool profile is a fixed TCP tool profile.

        :return: bool
        """

        return self.com_object.FixedTCP

    @fixed_tcp.setter
    def fixed_tcp(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FixedTCP = value

    @property
    def mass(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Mass() As double
                |     Tool mass in kilograms.

        :return: float
        """

        return self.com_object.Mass

    @mass.setter
    def mass(self, value: float):
        """
        :param float value:
        """

        self.com_object.Mass = value

    def get_attached_device(self) -> OLPController:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAttachedDevice() As OlpController
                |     Gets the associated controlling device for this tool
                |     profile.
                |     This controlling device might not exist if the tool device does not contain
                |     any mechanisms. In this case, this property will be NULL
                | 
                |     Returns:
                |         The attached device controller. It might be nothing if there is no
                |         device attached.

        :return: OLPController
        """
        return OLPController(self.com_object.GetAttachedDevice())

    def get_centroid(self, o_x: float, o_y: float, o_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetCentroid(double oX,double oY,double oZ)
                |     Gets the centroid of the tool.
                | 
                |     Parameters:
                | 
                |         oX
                |             The X Coordinate in m. 
                |         oY
                |             The Y Coordinate in m. 
                |         oZ
                |             The Z Coordinate in m.

        :param float o_x:
        :param float o_y:
        :param float o_z:
        :return: None
        """
        return self.com_object.GetCentroid(o_x, o_y, o_z)

    def get_inertia(self, o_xx: float, o_yy: float, o_zz: float, o_xy: float, o_yz: float, o_zx: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetInertia(double oXX,double oYY,double oZZ,double oXY,double oYZ,double
                | oZX)
                |     Gets the underlying coefficient of tool inertia
                | 
                |     Parameters:
                | 
                |         oXX
                |             The XX coefficient. 
                |         oYY
                |             The YY coefficient. 
                |         oZZ
                |             The ZZ coefficient. 
                |         oXY
                |             The XY coefficient. 
                |         oYZ
                |             The YZ coefficient. 
                |         oZX
                |             The ZX coefficient.

        :param float o_xx:
        :param float o_yy:
        :param float o_zz:
        :param float o_xy:
        :param float o_yz:
        :param float o_zx:
        :return: None
        """
        return self.com_object.GetInertia(o_xx, o_yy, o_zz, o_xy, o_yz, o_zx)

    def get_transform(self, i_origin: int) -> OLPTransform:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTransform(DELOlpPositionRef iOrigin) As OlpTransform
                |     Get the transform that represents the TCP location.
                |     For normal (mobile) tool profiles, this is the offset from the robot mount
                |     plate to the TCP. For fixed TCP tool profiles, this is the transform from the
                |     iOrigin location to the TCP.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The location that the transform is relative to.
                |             For normal (mobile) tool profiles this must be delOlpMount. For
                |             fixed TCP tool profiles it can be any other value except delOlpRobotBase since
                |             that would mean that the fixed TCP moves with the rail position (when the robot
                |             is on a rail). Instead of delOlpRobotBase you should use delOlpRailOrigin.
                |             
                | 
                |     Returns:
                |         The TCP transform.

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
                |     Sets the associated controlling device for this tool
                |     profile.
                |     The device is of type DELMIAOlpController, and it must have a valid
                |     attachment to the main MCA.
                | 
                |     Parameters:
                | 
                |         The
                |             target device controller.

        :param OLPController i_attached_device:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAttachedDevice(i_attached_device.com_object, i_match)

    def set_centroid(self, i_x: float, i_y: float, i_z: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCentroid(double iX,double iY,double iZ)
                |     Sets the centroid of the tool.
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate in m. 
                |         iY
                |             The Y Coordinate in m. 
                |         iZ
                |             The Z Coordinate in m.

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :return: None
        """
        return self.com_object.SetCentroid(i_x, i_y, i_z)

    def set_centroid_match(self, i_x: float, i_y: float, i_z: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetCentroidMatch(double iX,double iY,double iZ,boolean
                | iMatch)
                |     Sets the centroid of the tool.
                | 
                |     Parameters:
                | 
                |         iX
                |             The X Coordinate in m. 
                |         iY
                |             The Y Coordinate in m. 
                |         iZ
                |             The Z Coordinate in m. 
                |         iMatch
                |             Should the parameter be used to find a controller profile match?

        :param float i_x:
        :param float i_y:
        :param float i_z:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetCentroidMatch(i_x, i_y, i_z, i_match)

    def set_fixed_tcp_match(self, i_is_fixed_tcp: bool, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFixedTCPMatch(boolean iIsFixedTCP,boolean iMatch)
                |     Set whether this tool profile is a fixed TCP tool profile.
                | 
                |     Parameters:
                | 
                |         iIsFixedTCP
                |             Tool profile is for a fixed tool.
                |         iMatch
                |             Should the parameter be used to find a controller profile match?

        :param bool i_is_fixed_tcp:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetFixedTCPMatch(i_is_fixed_tcp, i_match)

    def set_inertia(self, i_xx: float, i_yy: float, i_zz: float, i_xy: float, i_yz: float, i_zx: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInertia(double iXX,double iYY,double iZZ,double iXY,double iYZ,double
                | iZX)
                |     Sets the underlying coefficient of tool inertia
                | 
                |     Parameters:
                | 
                |         iXX
                |             The XX coefficient. 
                |         iYY
                |             The YY coefficient. 
                |         iZZ
                |             The ZZ coefficient. 
                |         iXY
                |             The XY coefficient. 
                |         iYZ
                |             The YZ coefficient. 
                |         iZX
                |             The ZX coefficient.

        :param float i_xx:
        :param float i_yy:
        :param float i_zz:
        :param float i_xy:
        :param float i_yz:
        :param float i_zx:
        :return: None
        """
        return self.com_object.SetInertia(i_xx, i_yy, i_zz, i_xy, i_yz, i_zx)

    def set_inertia_match(self, i_xx: float, i_yy: float, i_zz: float, i_xy: float, i_yz: float, i_zx: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetInertiaMatch(double iXX,double iYY,double iZZ,double iXY,double
                | iYZ,double iZX,boolean iMatch)
                |     Sets the underlying coefficient of tool inertia
                | 
                |     Parameters:
                | 
                |         iXX
                |             The XX coefficient. 
                |         iYY
                |             The YY coefficient. 
                |         iZZ
                |             The ZZ coefficient. 
                |         iXY
                |             The XY coefficient. 
                |         iYZ
                |             The YZ coefficient. 
                |         iZX
                |             The ZX coefficient. 
                |         iMatch
                |             Should the parameter be used to find a controller profile match?

        :param float i_xx:
        :param float i_yy:
        :param float i_zz:
        :param float i_xy:
        :param float i_yz:
        :param float i_zx:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetInertiaMatch(i_xx, i_yy, i_zz, i_xy, i_yz, i_zx, i_match)

    def set_mass_match(self, i_mass: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMassMatch(double iMass,boolean iMatch)
                |     Set the tool mass in kilograms.
                | 
                |     Parameters:
                | 
                |         iMass
                |             Tool profile mass.
                |         iMatch
                |             Should the parameter be used to find a controller profile match?

        :param float i_mass:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetMassMatch(i_mass, i_match)

    def set_transform(self, i_origin: int, i_tcp: OLPTransform) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransform(DELOlpPositionRef iOrigin,OlpTransform iTCP)
                |     Set the transform that represents the TCP location.
                |     For normal (mobile) tool profiles, this is the offset from the transform
                |     from the robot mount plate to the TCP. For fixed TCP tool profiles, this is the
                |     transform from the robot base, world, etc. to the TCP, depending on the value
                |     of the parameter iOrigin.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The location that the transform is relative to.
                |             For normal (mobile) tool profiles this must be delOlpMount. For
                |             fixed TCP tool profiles it can be any other value.
                |             
                |         iTCP
                |             The TCP transform.

        :param int i_origin:
        :param OLPTransform i_tcp:
        :return: None
        """
        return self.com_object.SetTransform(i_origin, i_tcp.com_object)

    def set_transform_match(self, i_origin: int, i_tcp: OLPTransform, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransformMatch(DELOlpPositionRef iOrigin,OlpTransform iTCP,boolean
                | iMatch)
                |     Set the transform that represents the TCP location.
                |     For normal (mobile) tool profiles, this is the offset from the transform
                |     from the robot mount plate to the TCP. For fixed TCP tool profiles, this is the
                |     transform from the robot base, world, etc. to the TCP, depending on the value
                |     of the parameter iOrigin.
                | 
                |     Parameters:
                | 
                |         iOrigin
                |             The location that the transform is relative to.
                |             For normal (mobile) tool profiles this must be delOlpMount. For
                |             fixed TCP tool profiles it can be any other value.
                |             
                |         iTCP
                |             The TCP transform. 
                |         iMatch
                |             Should the parameter be used to find a controller profile match?

        :param int i_origin:
        :param OLPTransform i_tcp:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTransformMatch(i_origin, i_tcp.com_object, i_match)

    def __repr__(self):
        return f'OLPToolProfile(name="{ self.name }")'
