"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.setting_controller import SettingController


class MacrosSettingAtt(SettingController):
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
                |                         MacrosSettingAtt
                | 
                | Setting controller for the Macros tab page.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_default_macro_libraries(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetDefaultMacroLibraries() As CATSafeArrayVariant
                |     Returns the list of default macro libraries.

        :return: tuple
        """
        return self.com_object.GetDefaultMacroLibraries()

    def get_default_macro_libraries_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetDefaultMacroLibrariesInfo(CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves environment informations for the default macro libraries
                |     setting.
                |     Role:Retrieves the state of the parameter default macro libraries setting
                |     in the current environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value.

        :param str admin_level:
        :param str o_locked:
        :return: bool
        """
        return self.com_object.GetDefaultMacroLibrariesInfo(admin_level, o_locked)

    def get_external_references(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetExternalReferences() As CATSafeArrayVariant
                |     Returns the list of external references.

        :return: tuple
        """
        return self.com_object.GetExternalReferences()

    def get_external_references_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetExternalReferencesInfo(CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves environment informations for the external references
                |     setting.
                |     Role:Retrieves the state of the parameter external references setting in
                |     the current environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value.

        :param str admin_level:
        :param str o_locked:
        :return: bool
        """
        return self.com_object.GetExternalReferencesInfo(admin_level, o_locked)

    def get_language_editor(self, i_language: int) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLanguageEditor(CATScriptLanguage iLanguage) As CATBSTR
                |     Returns the editor path for the specified language.

        :param int i_language:
        :return: str
        """
        return self.com_object.GetLanguageEditor(i_language)

    def get_language_editor_info(self, admin_level: str, o_locked: str) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func GetLanguageEditorInfo(CATBSTR AdminLevel,CATBSTR oLocked) As
                | boolean
                |     Retrieves environment informations for the language editors
                |     setting.
                |     Role:Retrieves the state of the parameter language editors setting in the
                |     current environment.
                | 
                |     Parameters:
                | 
                |         AdminLevel
                | 
                |             If the parameter is locked, AdminLevel gives the administration
                |             level that imposes the value of the parameter.
                |             If the parameter is not locked, AdminLevel gives the administration
                |             level that will give the value of the parameter after a reset.
                |             
                |         oLocked
                |             Indicates if the parameter has been locked. 
                |         oModified
                |             Indicates if the parameter has been explicitly modified or remain
                |             to the administrated value.

        :param str admin_level:
        :param str o_locked:
        :return: bool
        """
        return self.com_object.GetLanguageEditorInfo(admin_level, o_locked)

    def set_default_macro_libraries(self, i_libraries: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetDefaultMacroLibraries(CATSafeArrayVariant iLibraries)
                |     Sets the list of default macro libraries.

        :param tuple i_libraries:
        :return: None
        """
        return self.com_object.SetDefaultMacroLibraries(i_libraries)

    def set_default_macro_libraries_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetDefaultMacroLibrariesLock(boolean iLocked)
                |     Locks or unlocks the default macro libraries setting.
                |     Role:Locks or unlocks the default macro libraries setting if it is possible
                |     in the current administrative context. In user mode this method will always
                |     return E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             True : to lock the parameter.
                |             False: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.com_object.SetDefaultMacroLibrariesLock(i_locked)

    def set_external_references(self, i_references: tuple) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetExternalReferences(CATSafeArrayVariant iReferences)
                |     Sets the list of external references.

        :param tuple i_references:
        :return: None
        """
        return self.com_object.SetExternalReferences(i_references)

    def set_external_references_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetExternalReferencesLock(boolean iLocked)
                |     Locks or unlocks the external references setting.
                |     Role:Locks or unlocks the external references setting if it is possible in
                |     the current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             True : to lock the parameter.
                |             False: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.com_object.SetExternalReferencesLock(i_locked)

    def set_language_editor(self, i_language: int, i_editor_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetLanguageEditor(CATScriptLanguage iLanguage,CATBSTR
                | iEditorPath)
                |     Sets the editor path for the specified language.

        :param CATScriptLanguage i_language:
        :param str i_editor_path:
        :return: None
        """
        return self.com_object.SetLanguageEditor(i_language, i_editor_path)

    def set_language_editor_lock(self, i_locked: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub SetLanguageEditorLock(boolean iLocked)
                |     Locks or unlocks the language editors setting.
                |     Role:Locks or unlocks the language editors setting if it is possible in the
                |     current administrative context. In user mode this method will always return
                |     E_FAIL.
                | 
                |     Parameters:
                | 
                |         iLocked
                |             the locking operation to be performed Legal
                |             values:
                |             True : to lock the parameter.
                |             False: to unlock the parameter.

        :param bool i_locked:
        :return: None
        """
        return self.com_object.SetLanguageEditorLock(i_locked)

    def __repr__(self):
        return f'MacrosSettingAtt(name="{self.name}")'
