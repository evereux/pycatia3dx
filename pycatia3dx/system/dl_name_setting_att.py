#! usr/bin/python3.9
"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.setting_controller import SettingController


class DlNameSettingAtt(SettingController):
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
                |                         DLNameSettingAtt
                | 
                | Interface to handle the DLNames.
                | Role: This interface is implemented by a component which represents the
                | controller of the DLNames.
                | This interface defines:
                | 
                |     A method to set each DLName
                |     A method to get the value of each DLName
                |     A method to lock/unlock each parameter
                |     A method to retrieve the informations concerning each
                |     parameter
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def dl_name_creation_right(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property DLNameCreationRight() As boolean
                |     Returns or set the right to create new DLNames.
                |     Role: Retrieves or set the right to create new DLNames.

        :return: bool
        """

        return self.com_object.DLNameCreationRight

    @dl_name_creation_right.setter
    def dl_name_creation_right(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.DLNameCreationRight = value

    @property
    def root_dl_name_creation_right(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Property RootDLNameCreationRight() As boolean
                |     Returns or set the right to create new Root DLNames.
                |     Role: Retrieves or set the right to create new Root DLNames.

        :return: bool
        """

        return self.com_object.RootDLNameCreationRight

    @root_dl_name_creation_right.setter
    def root_dl_name_creation_right(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RootDLNameCreationRight = value

    def get_dl_name(self, i_dl_name: str, o_real_name_unix: str, o_real_name_nt: str, o_father: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetDLName(CATBSTR iDLName,CATBSTR oRealNameUnix,CATBSTR oRealNameNT,CATBSTR
                | oFather)
                |     Retrieves the mapping between a logical name and the physical
                |     path.
                |     Role: Retrieves the mapping between a logical name and the physical
                |     path.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                |         oRealNameUnix
                |             the real physical path corresponding to the logical name on Unix.
                |             
                |         oRealNameNT
                |             the real physical path corresponding to the logical name on
                |             Windows. 
                |         iFather
                |             if applicable the Name of the parent DLName 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str o_real_name_unix:
        :param str o_real_name_nt:
        :param str o_father:
        :return: None
        """
        return self.com_object.GetDLName(i_dl_name, o_real_name_unix, o_real_name_nt, o_father)

    def get_dl_name_creation_right_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetDLNameCreationRightInfo(CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves the state of the parameter DLNameCreationRight.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :return: bool
        """
        return self.com_object.GetDLNameCreationRightInfo(admin_level, o_locked)

    def get_dl_name_exp(self, i_dl_name: str, o_real_name_unix: str, o_real_name_nt: str, o_father: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub GetDLNameExp(CATBSTR iDLName,CATBSTR oRealNameUnix,CATBSTR
                | oRealNameNT,CATBSTR oFather)
                |     Retrieves the mapping between a logical name and the physical
                |     path.
                |     Role: Retrieves the mapping between a logical name and the physical path in
                |     a literal form.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                |         oRealNameUnix
                |             the real physical path corresponding to the logical name on Unix.
                |             
                |         oRealNameNT
                |             the real physical path corresponding to the logical name on
                |             Windows. 
                |         iFather
                |             if applicable the Name of the parent DLName 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str o_real_name_unix:
        :param str o_real_name_nt:
        :param str o_father:
        :return: None
        """
        return self.com_object.GetDLNameExp(i_dl_name, o_real_name_unix, o_real_name_nt, o_father)

    def get_dl_name_info(self, i_dl_name: str, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetDLNameInfo(CATBSTR iDLName,CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves the state of the for a given DLName.
                |     Role: This information defines the state of the setting parameter and is
                |     made up of:
                | 
                |         The administration level that sets the current value or the value used
                |         to reset it
                |         The administration level that has locked the setting
                |         parameter.
                |         A flag to indicate whether the setting parameter was
                |         modified.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             a DLname. 
                |         ioAdminLevel
                |             [inout] The administration leve that defines the value used when
                |             resetting the setting parameter.
                | 
                |             Legal values:
                | 
                |                 Default value if the DLName has never been defined in the
                |                 administration concatenation.
                |                 Admin Level n if the setting parameter has been
                |                 administered,
                |                 where n is an integer starting from 0 representing the rank of
                |                 the administration level.
                | 
                |         ioLocked
                |             [inout] A character string to indicate whether the parameter is
                |             locked and the level of administration where the locking has been
                |             proceeded.
                |             Legal values:
                | 
                |                 Locked at Admin Level n if the setting parameter is locked by
                |                 then administration level n,
                |                 where n is an integer starting from 0.
                |                 Upper Locked if the setting parameter is locked by the current
                |                 administration level
                |                 Unlocked if the setting parameter is not
                |                 locked
                | 
                |     Returns:
                |         True to indicate that the DLName value has been defined at the current
                |         administrator or user level. This is only possible with unlocked DLNames. False
                |         means that the DLName is inherited from the
                |         administration.

        :param str i_dl_name:
        :param str admin_level:
        :param str o_locked:
        :return: bool
        """
        return self.com_object.GetDLNameInfo(i_dl_name, admin_level, o_locked)

    def get_dl_name_list(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetDLNameList() As CATSafeArrayVariant
                |     Retrieves the list of the DLNames.
                |     Role: Retrieves the list of the defined DLNames.
                | 
                |     Parameters:
                | 
                |         oTabDLName
                |             a CATSafeArrayVariant of CATBSTR of nb elements. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :return: tuple
        """
        return self.com_object.GetDLNameList()

    def get_dl_name_sub_list(self, i_dl_name: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetDLNameSubList(CATBSTR iDLName) As CATSafeArrayVariant
                |     Retrieves the list of the Sub-DLNames.
                |     Role: Retrieves the list of the DLNames created in a given
                |     DLName.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             The Father DLName. if iDLName=NULL all DLNames created at the root
                |             level are return. 
                |         oNbDLname
                |             The number of defined DLNames. 
                |         oTabDLName
                |             The array of DLNames 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_OUTOFMEMORY: on allocation failure
                |         E_FAIL: on other failures

        :param str i_dl_name:
        :return: tuple
        """
        return self.com_object.GetDLNameSubList(i_dl_name)

    def get_root_dl_name_creation_right_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetRootDLNameCreationRightInfo(CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves the state of the parameter
                |     RootDLNameCreationRight.
                |     Refer to SettingController for a detailled description.

        :param str admin_level:
        :param str o_locked:
        :return: bool
        """
        return self.com_object.GetRootDLNameCreationRightInfo(admin_level, o_locked)

    def remove_dl_name(self, i_dl_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub RemoveDLName(CATBSTR iDLName)
                |     Remove a logical name.
                |     Role: Remove a DLName in the current set if it is
                |     possible.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :return: None
        """
        return self.com_object.RemoveDLName(i_dl_name)

    def rename_dl_name(self, i_dl_name: str, i_new_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub RenameDLName(CATBSTR iDLName,CATBSTR iNewName)
                |     Rename an existing DLName.
                |     Role: Rename a DLName in the current set if it is
                |     possible.
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name to rename. 
                |         iNewName
                |             the new logical name. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str i_new_name:
        :return: None
        """
        return self.com_object.RenameDLName(i_dl_name, i_new_name)

    def set_dl_name(self, i_dl_name: str, i_real_name_unix: str, i_real_name_nt: str, i_father: str,
                    i_verif_directory: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetDLName(CATBSTR iDLName,CATBSTR iRealNameUnix,CATBSTR iRealNameNT,CATBSTR
                | iFather,boolean iVerifDirectory)
                |     Sets the mapping between a logical name and the physical
                |     path.
                |     Role: Sets the value of the cache maximum size in Mo
                | 
                |     Parameters:
                | 
                |         iDLName
                |             the logical name. 
                |         oRealNameUnix
                |             the real physical path corresponding to the logical name on Unix.
                |             
                |         oRealNameNT
                |             the real physical path corresponding to the logical name on
                |             Windows. 
                |         iFather
                |             if applicable the Name of the parent DLName 
                |         iVerifDirectory
                |             if VerifDirectory is set the existence of the directory on the
                |             current platform will be check. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param str i_real_name_unix:
        :param str i_real_name_nt:
        :param str i_father:
        :param bool i_verif_directory:
        :return: None
        """
        return self.com_object.SetDLName(i_dl_name, i_real_name_unix, i_real_name_nt, i_father, i_verif_directory)

    def set_dl_name_creation_right_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetDLNameCreationRightLock(boolean iLocked)
                |     Locks or unlocks the parameter DLNameCreationRight.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :return: None
        """
        return self.com_object.SetDLNameCreationRightLock(i_locked)

    def set_dl_name_lock(self, i_dl_name: str, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetDLNameLock(CATBSTR iDLName,boolean iLocked)
                |     Locks or unlocks the DLName.
                |     Role: Locks or unlocks the given DLName if the operation is allowed in the
                |     current administrated environment. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iDLname
                |             the DLname to be locked. 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             TRUE : to lock the parameter.
                |             FALSE: to unlock the parameter. 
                | 
                |     Returns:
                |         Legal values:
                |         S_OK : on Success
                |         E_FAIL: on failure

        :param str i_dl_name:
        :param bool i_locked:
        :return: None
        """
        return self.com_object.SetDLNameLock(i_dl_name, i_locked)

    def set_root_dl_name_creation_right_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetRootDLNameCreationRightLock(boolean iLocked)
                |     Locks or unlocks the parameter RootDLNameCreationRight.
                |     Refer to SettingController for a detailled description.

        :param bool i_locked:
        :return: None
        """
        return self.com_object.SetRootDLNameCreationRightLock(i_locked)

    def __repr__(self):
        return f'DlNameSettingAtt(name="{self.name}")'
