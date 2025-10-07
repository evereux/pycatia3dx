"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.dnb_igp_olp_use.olp_gun import OLPGun
from pycatia3dx.dnb_igp_olp_use.olp_profile import OLPProfile


class OLPPaintProfile(OLPProfile):

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
                |                         OlpPaintProfile
                | 
                | A paint profile used for translating a robot program.
                | 
                | This interface can only be used by a translator within the Robotics Off-line
                | Programming (OLP) Download or Upload command.
                | 
                | The behavior of this object depends on where it was retrieved from. If the
                | object was retrieved from a OlpTriggerAction then this object is used to
                | configure the paint properties of that trigger. The parameters specified with
                | the iMatch input equal to TRUE will be used to find an existing profile to
                | reuse for this instruction. If no matching profile is found, a new one will be
                | created. If the object was retrieved from OlpController.PaintProfileList then
                | any modifications to this object will change an existing or new profile's
                | values directly.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_air_pressure(self, i_gun: OLPGun) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAirPressure(OlpGun iGun) As double
                |     Get shaping air pressure in pascals (N/m^2).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The value.

        :param OLPGun i_gun:
        :return: float
        """
        return self.com_object.GetAirPressure(i_gun.com_object)

    def get_air_volume(self, i_gun: OLPGun) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAirVolume(OlpGun iGun) As double
                |     Get shaping air flow rate in cubic meters per second
                |     (m^3/s).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The value.

        :param OLPGun i_gun:
        :return: float
        """
        return self.com_object.GetAirVolume(i_gun.com_object)

    def get_enabled_guns(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEnabledGuns() As CATSafeArrayVariant
                |     Get the list of enabled guns.
                | 
                |     Parameters:
                | 
                |         oGuns
                |             List of OlpGun objects

        :return: tuple
        """
        return self.com_object.GetEnabledGuns()

    def get_flow_rate(self, i_gun: OLPGun) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFlowRate(OlpGun iGun) As double
                |     Get the flow rate in cubic meters per second (m^3/s).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The value.

        :param OLPGun i_gun:
        :return: float
        """
        return self.com_object.GetFlowRate(i_gun.com_object)

    def get_gun_enabled(self, i_gun: OLPGun) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGunEnabled(OlpGun iGun) As boolean
                |     Get whether the specified gun is enabled.
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         True if enabled.

        :param OLPGun i_gun:
        :return: bool
        """
        return self.com_object.GetGunEnabled(i_gun.com_object)

    def get_param_index(self, i_gun: OLPGun) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParamIndex(OlpGun iGun) As long
                |     Get the parameter set index.
                |     If not set, GetParamIndex will fail.
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The index.

        :param OLPGun i_gun:
        :return: int
        """
        return self.com_object.GetParamIndex(i_gun.com_object)

    def get_param_index_set(self, i_gun: OLPGun) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetParamIndexSet(OlpGun iGun) As boolean
                |     Get whether the parameter set index is set.
                |     If not set, GetParamIndex will fail.
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         True if set.

        :param OLPGun i_gun:
        :return: bool
        """
        return self.com_object.GetParamIndexSet(i_gun.com_object)

    def get_percent_solids(self, i_gun: OLPGun) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetPercentSolids(OlpGun iGun) As double
                |     Get the percent solids as fraction (0.5 is 50%).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The value.

        :param OLPGun i_gun:
        :return: float
        """
        return self.com_object.GetPercentSolids(i_gun.com_object)

    def get_rotation_speed(self, i_gun: OLPGun) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetRotationSpeed(OlpGun iGun) As double
                |     Get the rotation speed in rad/sec.
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The value.

        :param OLPGun i_gun:
        :return: float
        """
        return self.com_object.GetRotationSpeed(i_gun.com_object)

    def get_transfer_efficiency(self, i_gun: OLPGun) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTransferEfficiency(OlpGun iGun) As double
                |     Get the transfer efficiency as fraction (0.5 is 50%).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The value.

        :param OLPGun i_gun:
        :return: float
        """
        return self.com_object.GetTransferEfficiency(i_gun.com_object)

    def get_voltage(self, i_gun: OLPGun) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetVoltage(OlpGun iGun) As double
                |     Get voltage in volts (V).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                | 
                |     Returns:
                |         The value.

        :param OLPGun i_gun:
        :return: float
        """
        return self.com_object.GetVoltage(i_gun.com_object)

    def set_air_pressure(self, i_gun: OLPGun, i_air_pressure: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAirPressure(OlpGun iGun,double iAirPressure,boolean
                | iMatch)
                |     Set the shaping air pressure in pascals (N/m^2).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iAirPressure
                |             The value 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPGun i_gun:
        :param float i_air_pressure:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAirPressure(i_gun.com_object, i_air_pressure, i_match)

    def set_air_volume(self, i_gun: OLPGun, i_air_volume: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetAirVolume(OlpGun iGun,double iAirVolume,boolean iMatch)
                |     Set the shaping air flow rate in cubic meters per second
                |     (m^3/s).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iAirVolume
                |             The value 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPGun i_gun:
        :param float i_air_volume:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetAirVolume(i_gun.com_object, i_air_volume, i_match)

    def set_flow_rate(self, i_gun: OLPGun, i_flow_rate: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFlowRate(OlpGun iGun,double iFlowRate,boolean iMatch)
                |     Set the flow rate in cubic meters per second (m^3/s).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iFlowRate
                |             The value 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPGun i_gun:
        :param float i_flow_rate:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetFlowRate(i_gun.com_object, i_flow_rate, i_match)

    def set_gun_enabled(self, i_gun: OLPGun, i_enabled: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGunEnabled(OlpGun iGun,boolean iEnabled)
                |     Set whether the specified gun is enabled.
                |     Gun enabled status is always matched.
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iEnabled
                |             True if enabled.

        :param OLPGun i_gun:
        :param bool i_enabled:
        :return: None
        """
        return self.com_object.SetGunEnabled(i_gun.com_object, i_enabled)

    def set_param_index(self, i_gun: OLPGun, i_index: int, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetParamIndex(OlpGun iGun,long iIndex,boolean iMatch)
                |     Set the parameter set index.
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iIndex
                |             The index value 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPGun i_gun:
        :param int i_index:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetParamIndex(i_gun.com_object, i_index, i_match)

    def set_percent_solids(self, i_gun: OLPGun, i_percent_solids: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetPercentSolids(OlpGun iGun,double iPercentSolids,boolean
                | iMatch)
                |     Set the percent solids as fraction (0.5 is 50%).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iPercentSolids
                |             The value 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPGun i_gun:
        :param float i_percent_solids:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetPercentSolids(i_gun.com_object, i_percent_solids, i_match)

    def set_rotation_speed(self, i_gun: OLPGun, i_rotation_speed: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetRotationSpeed(OlpGun iGun,double iRotationSpeed,boolean
                | iMatch)
                |     Set the rotation speed in rad/sec.
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iRotationSpeed
                |             The value 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPGun i_gun:
        :param float i_rotation_speed:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetRotationSpeed(i_gun.com_object, i_rotation_speed, i_match)

    def set_transfer_efficiency(self, i_gun: OLPGun, i_transfer_efficiency: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTransferEfficiency(OlpGun iGun,double iTransferEfficiency,boolean
                | iMatch)
                |     Set the transfer efficiency as fraction (0.5 is 50%).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iTransferEfficiency
                |             The value 
                |         iMatch
                |             If TRUE use value to find existing profile.

        :param OLPGun i_gun:
        :param float i_transfer_efficiency:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetTransferEfficiency(i_gun.com_object, i_transfer_efficiency, i_match)

    def set_voltage(self, i_gun: OLPGun, i_voltage: float, i_match: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetVoltage(OlpGun iGun,double iVoltage,boolean iMatch)
                |     Set voltage in volts (V).
                | 
                |     Parameters:
                | 
                |         iGun
                |             The gun object. 
                |         iVoltage
                |             The value 
                |         iMatch
                |             If TRUE use value to find existing profile. 

        :param OLPGun i_gun:
        :param float i_voltage:
        :param bool i_match:
        :return: None
        """
        return self.com_object.SetVoltage(i_gun.com_object, i_voltage, i_match)

    def __repr__(self):
        return f'OLPPaintProfile(name="{ self.name }")'
