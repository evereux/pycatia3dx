#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.setting_controller import SettingController


class LicenseSettingAtt(SettingController):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     System.SettingController
                |                         LicenseSettingAtt
                | 
                | Interface to handle the licensing settings.
                | Role: This interface is implemented by a component which represents the
                | controller of the static Licenses.
                | To access this property page:
                | Click the Options command in the Tools menu
                | Click General
                | Click the Licensing Property Page
                | 
                | This interface defines:
                | A method to set each License
                | A method to get the value of each License
                | A method to lock/unlock each parameter
                | A method to retrieve the information concerning each parameter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def frequency(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property Frequency() As float
                |     Retrieves or Sets the contact frequency.
                |     Role: Retrieves or sets the value of the parameter describing the server
                |     contact frequency. Note that a null value represents the maximum contact
                |     frequency value in minutes. For more information about the range and maximum,
                |     refers to the Infrastructure documentation.

        :return: float
        """

        return self.com_object.Frequency

    @frequency.setter
    def frequency(self, value: float):
        """
        :param float value:
        """

        self.com_object.Frequency = value

    @property
    def nodelock_alert(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property NodelockAlert() As long
                |     Retrieves or Sets the license expiry alert.
                |     Role: Retrieves or sets the value of the parameter describing the
                |     license expiry alertt in days. For more information about the range and
                |     maximum, refers to the Infrastructure documentation.

        :return: int
        """

        return self.com_object.NodelockAlert

    @nodelock_alert.setter
    def nodelock_alert(self, value: int):
        """
        :param int value:
        """

        self.com_object.NodelockAlert = value

    @property
    def server_time_out(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ServerTimeOut() As float
                |     Retrieves or Sets the server time out.
                |     Role: Retrieves or sets the value of the parameter describing the licensing
                |     server time out in minutes. For more information about the range and maximum,
                |     refers to the Infrastructure documentation.

        :return: float
        """

        return self.com_object.ServerTimeOut

    @server_time_out.setter
    def server_time_out(self, value: float):
        """
        :param float value:
        """

        self.com_object.ServerTimeOut = value

    @property
    def show_license(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property ShowLicense() As boolean
                |     Retrieves or Sets the show license .
                |     Role: Retrieves or sets the value of the parameter describing the complete
                |     license information. When the parameter is set, the user gets more information
                |     about the reason of the failure to request a license.

        :return: bool
        """

        return self.com_object.ShowLicense

    @show_license.setter
    def show_license(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ShowLicense = value

    def get_frequency_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetFrequencyInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves information about the Frequency setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetFrequencyInfo(io_admin_level, io_locked)

    def get_license(self, i_license: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLicense(CATBSTR iLicense) As CATBSTR
                |     Retrieves the value of the license.
                |     Role: Retrieves the mapping between a name of a license and the value of
                |     the license. The license does not need to be returned by GetLicensesList(). But
                |     if the license is not installed the license will be
                |     "NotRequested"
                | 
                |     Parameters:
                | 
                |         iLicense
                |             the name of the License: "PMG.prd", "_MD2.slt+", "_MD2.slt+GSD" for
                |             example.
                |             "PMG.prd" represent the license of the product PMG
                |             "_MD2.slt+" represent the license of the solution
                |             MD2
                |             "_MD2.slt+GSD" represent the license of the solution MD2, with the
                |             AddOn product GSD 
                | 
                |     Returns:
                |         the value of the License:
                |         Not requested : License is not Requested.
                |         key : the name of the license, the default available license has been chosen by the user. License is Requested.
                |         License Number : a specific license number has been chosen by the user. License is Requested.

        :param str i_license:
        :return: str
        """
        return self.com_object.GetLicense(i_license)

    def get_license_info(self, i_license: str, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLicenseInfo(CATBSTR iLicense,CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves information about the License setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str i_license:
        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetLicenseInfo(i_license, io_admin_level, io_locked)

    def get_licenses_list(self, i_default_licenses: int) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLicensesList(long iDefaultLicenses) As
                | CATSafeArrayVariant
                |     Retrieves the list of the requested or locked licenses.
                |     Role: Retrieves the list of the requested or locked licenses. There is no
                |     SetLicensesList() because the list is initialized using
                |     LUM.
                | 
                |     Parameters:
                | 
                |         iDefaultLicenses
                |             If iDefaultLicenses!=0 and the settings are empty, returns the default licenses, that is, the visible nodolocked licenses. If iDefaultLicenses = 0 and the settings are empty, returns the selected licenses (not yet stored, because not yet validated by OK button). 
                | 
                |     Returns:
                |         The array of Licenses.
                |         character meaning in license name:
                |         "_": internal notation for a license configuration
                |         "+": you chose "Any license" mode, example of returned value:
                |         _ME1.slt+FS1
                |         When the return value is a serial number (_ME1.slt_SerialNumber), you
                |         have chosen the "Explicit" license mode. In this case the add on product is not
                |         indicated in the license name.

        :param int i_default_licenses:
        :return: tuple
        """
        return self.com_object.GetLicensesList(i_default_licenses)

    def get_licenses_list_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLicensesListInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves information about the LicensesList setting
                |     parameter.
                |     Role: Retrieves information about the LicensesList setting locking state
                |     (global lock for the LicensesList). It is used to get the lock status of the
                |     List of the Licenses. If the LicensesList is locked all the licenses are
                |     locked. When the licenses are locked, it means that an administrator has locked
                |     the attribute. It does not means that an administrator has changed the value of
                |     the attribute. The value of the setting is not updatable because it refers to a
                |     lock on a list. That is why the return value is false.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel
                |             Level of administrator. 
                |         ioLocked
                |             Locked/Unlocked. 
                | 
                |     Returns:
                |         False.
                |         Information returned in the dump:
                |         Parameter 1 : "Value taken in case of reset" : useless. Default value : "Default value"
                |         Parameter 2 : "Locking state" value : unlocked / locked / locked at Admin Level n
                |         Parameter 3 : "Returned value" : useless, default value : False
                | 
                |         Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetLicensesListInfo(io_admin_level, io_locked)

    def get_nodelock_alert_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetNodelockAlertInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves information about the license expiry alert setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetNodelockAlertInfo(io_admin_level, io_locked)

    def get_server_time_out_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetServerTimeOutInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves information about the TimeOut setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetServerTimeOutInfo(io_admin_level, io_locked)

    def get_show_license_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetShowLicenseInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves information about the ShowLicense setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetShowLicenseInfo(io_admin_level, io_locked)

    def set_frequency_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetFrequencyLock(boolean iLock)
                |     Locks or unlocks the Frequency setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.com_object.SetFrequencyLock(i_lock)

    def set_license(self, i_license: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetLicense(CATBSTR iLicense,CATBSTR iValue)
                |     Sets the License.
                |     Role: Sets the value of the license.
                | 
                |     Parameters:
                | 
                |         iLicense
                |             the name of the License: "PMG.prd", "_MD2.slt+", "_MD2.slt+gSD" for
                |             example.
                |             "PMG.prd" represent the license of the product PMG
                |             "_MD2.slt+" represent the license of the solution
                |             MD2
                |             "_MD2.slt+GSD" represent the license of the solution MD2, with the
                |             AddOn product GSD 
                |         iValue
                |             the value of the License:
                |             Not requested : License is not Requested.
                |             key : the name of the license, the default available license has been chosen by the user. License is Requested.
                |             License Number : a specific license number has been chosen by the user. License is Requested.

        :param str i_license:
        :param str i_value:
        :return: None
        """
        return self.com_object.SetLicense(i_license, i_value)

    def set_license_lock(self, i_license: str, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetLicenseLock(CATBSTR iLicense,boolean iLock)
                |     Locks or unlocks the License setting parameter.
                |     Refer to SettingController for a detailed description.

        :param str i_license:
        :param bool i_lock:
        :return: None
        """
        return self.com_object.SetLicenseLock(i_license, i_lock)

    def set_licenses_list_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetLicensesListLock(boolean iLock)
                |     Locks or unlocks the LicensesList setting parameter.
                |     Role:Locks or unlocks the LicensesList setting parameter. Locks or unlocks
                |     the parameter describing the list of installed licenses, if the operation is
                |     allowed in the current administrated environment. It is the global lock on all
                |     the licenses. When the LicenseList is locked all the licenses are locked. When
                |     the LicenseList is unlocked all the licenses are unlocked.
                | 
                |     Parameters:
                | 
                |         iLock
                |             the locking operation to be performed:
                |             True: to lock the parameter.
                |             False: to unlock the parameter.
                |             Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.com_object.SetLicensesListLock(i_lock)

    def set_nodelock_alert_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetNodelockAlertLock(boolean iLock)
                |     Locks or unlocks the license expiry alert setting
                |     parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.com_object.SetNodelockAlertLock(i_lock)

    def set_server_time_out_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetServerTimeOutLock(boolean iLock)
                |     Locks or unlocks the TimeOut setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.com_object.SetServerTimeOutLock(i_lock)

    def set_show_license_lock(self, i_lock: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetShowLicenseLock(boolean iLock)
                |     Locks or unlocks the ShowLicense setting parameter.
                |     Refer to SettingController for a detailed description.

        :param bool i_lock:
        :return: None
        """
        return self.com_object.SetShowLicenseLock(i_lock)

    def __repr__(self):
        return f'LicenseSettingAtt(name="{self.name}")'
