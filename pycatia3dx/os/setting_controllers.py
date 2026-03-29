"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from typing import Iterator

from pycatia3dx.system.collection import Collection
from pycatia3dx.system.setting_controller import SettingController


class SettingControllers(Collection):
    """
        .. note::
            :class: toggle

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
            :class: toggle

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

        :param str i_index:
        :return: SettingController
        """
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
