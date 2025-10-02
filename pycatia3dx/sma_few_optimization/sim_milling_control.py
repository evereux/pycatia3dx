"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimMillingControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMillingControl
                | 
                | Represents the casting control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimMillingControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyMillingControl As SimMillingControl
                |      Set MyMillingControl = MyFeatures.Add("SimMillingControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimMillingControl named "Milling Control.1" as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyMillingControl As SimMillingControl
                |      Set MyMillingControl = MyFeatures.Item("Milling Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimMillingControl as following:
                | 
                |      ...
                |      MyMillingControl = MyFeatures.Add("SimMillingControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimMillingControl named "Milling Variable.1" as following:
                | 
                |      ...
                |      MyMillingControl = MyFeatures.Item("Milling Variable.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def milling_axis(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MillingAxis() As CATBaseDispatch (Read Only)
                |     Returns the milling axis direction.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MillingAxis)

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
        return f'SimMillingControl(name="{ self.name }")'
