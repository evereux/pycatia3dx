#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.setting_controller import SettingController


class DynLicenseSettingAtt(SettingController):
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
                |                         DynLicenseSettingAtt
                | 
                | Interface to handle the dynamic licensing settings.
                | Role: This interface is implemented by a component which represents the
                | controller of the dynamic Licenses.
                | To access this property page:
                | Click the Options command in the Tools menu
                | Click General
                | Click the Shareable Products Property Page
                | 
                | This interface defines:
                | A method to lock/unlock each parameter
                | A method to retrieve the information concerning each parameter
                | Note that when a license is selected in user mode, no information is written in
                | the settings, only the lock status is written in the settings.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_license(self, i_license: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLicense(CATBSTR iLicense) As CATBSTR
                |     Retrieves the check_lock value of the license.
                |     Role: Retrieves the mapping between a name of a license and the check_lock
                |     value of the license. Note: This method appears after a dump action by default
                |     in the generated macro when administrator parameters are locked. It does not
                |     return a granted or not granted status on the license. When the license is not
                |     checklocked GetLicense() does not appears in the dump, even when
                |     GetLicenseInfo() appears. Use this call to get the check_lock status of a
                |     license. There is no inheritance of the check_lock status of a license for the
                |     end user: If the check_lock has been requested for any of the administrator,
                |     the license appears locked for the end user, In user mode the license ZZZ.prd
                |     appears locked in the shareable product tab when parameter
                |     iLicense="Check_ZZZ.prd", and the parameter oValue="CheckLockRequested". The
                |     value "CheckNotLockRequested" appears only when the setting exits (a license
                |     check button has been first unchecked, validated with OK button, and then the
                |     license check button has been rechecked).
                |     There is no link between the lock on the license itself which is used when
                |     there are several admin levels. For iLicense="ZZZ.prd", the oValue may be
                |     "Locked" or "Unlocked".
                |     For a package: iLicense="Check_Mypackage.package" and
                |     oValue="CheckLockRequested". (Mypackage is the name of the
                |     package).
                | 
                |     Parameters:
                | 
                |         iLicense
                |             The license name begins with Check_ for checklocks
                |             
                | 
                |     Returns:
                |         the value of the License:
                |         CheckLockRequested : check_lock requested.
                |         CheckLockNotRequested : check_lock not requested.
                |         "": always if the licenses are not checklock. In that case the license
                |         value is not modified. It is the lock status whom cares.

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
                |     Retrieves the state of a given License.
                |     Role: Retrieves the state of a given License. It it is used to get the lock
                |     status of a specific license. When the license is locked, it means that an
                |     administrator has locked the attribute. It does not means that an administrator
                |     has changed the value of the license. The return value is true when the license
                |     is checklocked, because the value of the license is Check_XXX.prd and for a
                |     package Check_Mypackage.package.
                | 
                |     Parameters:
                | 
                |         iLicense:
                |             the name of the License. 
                |         ioAdminLevel:
                |             Level of administrator. 
                |         ioLocked:
                |             Locked/Unlocked.
                |             Refer to SettingController for a detailed
                |             description.
                |             Dump information:
                |             Parameter 1 : the name of the License.
                |             Parameter 2 : "Set at Admin Level j" when locked, "Default value" when unlock.
                |             Parameter 3 : locking state of the licenses Unlocked / Locked / Locked at Admin Level j.
                |             Return value : Always false if the license is not checklock, because the status of the license is not modified, only the lock status is modified. True if the license is checklock, because the value of the license has been changed to Check_XXX.prd.

        :param str i_license:
        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetLicenseInfo(i_license, io_admin_level, io_locked)

    def get_licenses_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLicensesList() As CATSafeArrayVariant
                |     Retrieves the List of the Licenses.
                |     Role: Retrieves the list of the locked Licenses. There is no
                |     SetLicenseList() because the list is initialized using
                |     LUM.
                |     When using packages, the licenses name appears like MyPackage.Package
                |     (Mypackage is the name of the package).
                | 
                |     Returns:
                |         The array of Licenses.

        :return: tuple
        """
        return self.com_object.GetLicensesList()

    def get_licenses_list_info(self, io_admin_level: str, io_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLicensesListInfo(CATBSTR ioAdminLevel,CATBSTR ioLocked) As
                | boolean
                |     Retrieves information about the LicensesList setting locking state (global
                |     lock for the LicensesList).
                |     Role: Retrieves information about the LicensesList setting locking state
                |     (global lock for the LicensesList) It is used to get the lock status of the
                |     List of the Licenses. If the LicensesList is locked all the licenses are
                |     locked. When the licenses are locked, it means that an administrator has locked
                |     the attribute. It does not means that an administrator has changed the value of
                |     the attribute. The value of the setting is not updatable because it refers to a
                |     lock on a list. That is why the return value is false.
                | 
                |     Parameters:
                | 
                |         ioAdminLevel:
                |             Level of administrator. 
                |         ioLocked:
                |             Locked/Unlocked. 
                | 
                |     Returns:
                |         False
                |         Parameter values in dump:
                |         Parameter 1 : "Value taken in case of reset" : useless. Default value: "Default value".
                |         Parameter 2 : "Locking state" value : unlocked / locked / locked at Admin Level n
                |         Parameter 3 : "Returned value" : useless, default value : False
                | 
                |         Refer to SettingController for a detailed description.

        :param str io_admin_level:
        :param str io_locked:
        :return: bool
        """
        return self.com_object.GetLicensesListInfo(io_admin_level, io_locked)

    def set_license(self, i_license: str, i_value: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetLicense(CATBSTR iLicense,CATBSTR iValue)
                |     Sets the check_lock status of license.
                |     Role: Sets the check_lock value of the license. It it not possible to grant
                |     a license with this call. This method shoud be called in administrator mode.
                |     There is no inheritance of the check_lock status of a license for the end user:
                |     If the check_lock has been requested for any of the administrator, the license
                |     appears locked for the end user, In user mode the license ZZZ.prd appears
                |     locked in the shareable product tab when parameter iLicense="Check_ZZZ.prd",
                |     and the parameter iValue="CheckLockRequested". The value
                |     "CheckNotLockRequested" appears only when the setting exits (a license check
                |     button has been first unchecked, validated with OK button, and then the license
                |     check button has been rechecked).
                |     There is no link between the lock on the license itself which is used when
                |     there are several admin levels. For iLicense="ZZZ.prd", the iValue may be
                |     "Locked" or "Unlocked".
                |     For a package: iLicense="Check_Mypackage.package" and
                |     iValue="CheckLockRequested". (Mypackage is the name of the
                |     package).
                | 
                |     Parameters:
                | 
                |         iLicense
                |             The license name begins with Check_ for check locks
                |             
                |         iValue
                |             the value of the License:
                |             CheckLockRequested : check_lock requested.
                |             CheckLockNotRequested : check_lock not requested.
                |             "": always if the licenses are not checklock. In that case the
                |             license value is not modified. It is the lock status whom cares.

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
                |     Role: Locks or unlocks the given License if the operation is allowed in the
                |     current administrated environment.
                | 
                |     Parameters:
                | 
                |         iLicense:
                |             the name of the License. 
                |         iLock
                |             the locking operation to be performed:
                |             True: to lock the parameter.
                |             False: to unlock the parameter.
                |             Refer to SettingController for a detailed description.

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
                |     Role: Locks or unlocks the parameter describing the list of installed
                |     licenses, if the operation is allowed in the current administrated environment.
                |     When the LicenseList is locked all the licenses are locked. When the
                |     LicenseList is unlocked all the licenses are unlocked.
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

    def __repr__(self):
        return f'DynLicenseSettingAtt(name="{self.name}")'
