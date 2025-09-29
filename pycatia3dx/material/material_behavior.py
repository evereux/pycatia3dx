"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.material.material_behavior_options import MaterialBehaviorOptions
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity


class MaterialBehavior(PLMEntity):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         MaterialBehavior
                | 
                | Represents a Material Behavior.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def behavior_options(self) -> MaterialBehaviorOptions:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BehaviorOptions() As MaterialBehaviorOptions (Read
                | Only)

        :return: MaterialBehaviorOptions
        """

        return MaterialBehaviorOptions(self.com_object.BehaviorOptions)

    def __repr__(self):
        return f'MaterialBehavior(name="{self.name}")'
