"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sma_mpa_base.sim_axis_system import SimAxisSystem


class SimExtrusionControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimExtrusionControl
                | 
                | Represents the casting control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimExtrusionControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyExtrusionControl As SimExtrusionControl
                |      Set MyExtrusionControl = MyFeatures.Add("SimExtrusionControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimExtrusionControl named "Extrusion Control.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyExtrusionControl As SimExtrusionControl
                |      Set MyExtrusionControl = MyFeatures.Item("Extrusion Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimExtrusionControl as following:
                | 
                |      ...
                |      MyExtrusionControl = MyFeatures.Add("SimExtrusionControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimExtrusionControl named "Extrusion Control.1" as
                |     following:
                | 
                |      ...
                |      MyExtrusionControl = MyFeatures.Item("Extrusion Control.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system used for extrusion control.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def prevent_material_removal_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PreventMaterialRemovalFlag() As boolean
                |     Returns or sets the flag to prevent material removal in preserved region's shadow.
                |     FALSE : No prevention for material removal,
                |     TRUE : Prevention for material removal in applied.

        :return: bool
        """

        return self.com_object.PreventMaterialRemovalFlag

    @prevent_material_removal_flag.setter
    def prevent_material_removal_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PreventMaterialRemovalFlag = value

    def __repr__(self):
        return f'SimExtrusionControl(name="{ self.name }")'
