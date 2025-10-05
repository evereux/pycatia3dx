"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimVoidRatio(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimVoidRatio
                | 
                | Represents the Void Ratio object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimVoidRatio as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyVoidRatio As SimVoidRatio
                |      Set MyVoidRatio = MyFeatures.Add("SimVoidRatio")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimVoidRatio named "Void
                |     Ratio.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyVoidRatio As SimVoidRatio
                |      Set MyVoidRatio = MyFeatures.Item("Void Ratio.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimVoidRatio as
                |     following:
                | 
                |      ...
                |      myVoidRatio = myFeatures.Add("SimVoidRatio")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimVoidRatio
                |     named "Void Ratio.1" as following:
                | 
                |      ...
                |      myVoidRatio = myFeatures.Item("Void Ratio.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. See SimFeatures.GetSpecTreeCategory for usage.

        :return: str
        """

        return self.com_object.SpecTreeCategory

    @property
    def void_ratio(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VoidRatio() As double
                |     Returns or sets the void ratio. Quantity: DIMENSIONLESS, units: None.

        :return: float
        """

        return self.com_object.VoidRatio

    @void_ratio.setter
    def void_ratio(self, value: float):
        """
        :param float value:
        """

        self.com_object.VoidRatio = value

    def __repr__(self):
        return f'SimVoidRatio(name="{ self.name }")'
