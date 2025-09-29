"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class MaterialBehaviorOptions(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     MaterialBehaviorOptions

    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_material_behavior_option: AnyObject, o_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Add(CATBaseDispatch iMaterialBehaviorOption,short oIndex)
                |     Allow to add an option in list.
                | 
                |     Parameters:
                | 
                |         iMaterialBehaviorOption
                |             The option to add to this behavior. 
                |         oIndex
                |             Index of the added Option in the list.

        :param AnyObject i_material_behavior_option:
        :param int o_index:
        :return: None
        """
        return self.com_object.Add(i_material_behavior_option.com_object, o_index)

    def get_option(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetOption(CATVariant iIndex) As CATBaseDispatch
                |     Allow to retrieve an option in list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The option index to retrieve. 
                |         oMaterialOption
                |             The material option.

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.GetOption(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Allow to remove an option in list.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The option index to remove.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'MaterialBehaviorOptions(name="{self.name}")'
