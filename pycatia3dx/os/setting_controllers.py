"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.os.macros_setting_att import MacrosSettingAtt
from pycatia3dx.system.collection import Collection
from pycatia3dx.system.dl_name_setting_att import DLNameSettingAtt
from pycatia3dx.system.dyn_license_setting_att import DynLicenseSettingAtt
from pycatia3dx.system.license_setting_att import LicenseSettingAtt
from pycatia3dx.system.setting_controller import SettingController


class SettingControllers(Collection):
    """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SettingControllers
                | 
                | A collection of all the setting controllers objects currently managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=SettingController)
        self.com_object = com_object

    def item(self, i_index: str) -> SettingController:
        """
        .. note::

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(CATBSTR iIndex) As SettingController
                |     Returns a setting controller using its name from the setting controllers
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The name of the window to retrieve from the collection of setting
                |             controller. As a string. 
                | 
                |     Returns:
                |         The retrieved setting controller.

        Class Name           i_index
        DLNameSettingAtt     CATSysDLNameSettingCtrl
        DynLicenseSettingAtt CATSysDynLicenseSettingCtrl
        LicenseSettingAtt    CATSysLicenseSettingCtrl
        MacrosSettingAtt     CATScriptMacrosSettingCtrl

        :param str i_index:
        :return: SettingController
        """

        if i_index == "CATSysDLNameSettingCtrl":
            return DLNameSettingAtt(self.com_object.Item(i_index))
        if i_index == "CATSysDynLicenseSettingCtrl":
            return DynLicenseSettingAtt(self.com_object.Item(i_index))
        if i_index == "CATSysLicenseSettingCtrl":
            return LicenseSettingAtt(self.com_object.Item(i_index))
        if i_index == "CATScriptMacrosSettingCtrl":
            return MacrosSettingAtt(self.com_object.Item(i_index))

        return SettingController(self.com_object.Item(i_index))

    def __getitem__(self, n: int) -> SettingController:
        if (n + 1) > self.count:
            raise StopIteration

        return SettingController(self.com_object.Item(n + 1))

    def __iter__(self) -> Iterator[SettingController]:
        for i in range(self.count):
            yield SettingController(self.com_object.Item(i + 1))

    def __repr__(self):
        return f'SettingControllers(name="{self.name}")'
