"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem


class SimCastingControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCastingControl
                | 
                | Represents the casting control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCastingControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCastingControl As SimCastingControl
                |      Set MyCastingControl = MyFeatures.Add("SimCastingControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimCastingControl named "Casting Control.1" as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCastingControl As SimCastingControl
                |      Set MyCastingControl = MyFeatures.Item("Casting Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCastingControl as following:
                | 
                |      ...
                |      MyCastingControl = MyFeatures.Add("SimCastingControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimCastingControl named "Casting Control.1" as following:
                | 
                |      ...
                |      MyCastingControl = MyFeatures.Item("Casting Control.1")
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
                |     Returns the axis system used for the casting control.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def plane(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Plane() As CATBaseDispatch (Read Only)
                |     Returns the plane associated to the casting control.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Plane)

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

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimCastingControlType
                |     Returns or sets the type of casting control.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def __repr__(self):
        return f'SimCastingControl(name="{ self.name }")'
