"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimInitialField(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimInitialField
                | 
                | Represents the Initial Field object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimInitialField as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialField As SimInitialField
                |      Set MyInitialField = MyFeatures.Add("SimInitialField")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimInitialField named
                |     "Initial Field.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialField As SimInitialField
                |      Set MyInitialField = MyFeatures.Item("Initial Field.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimInitialField as
                |     following:
                | 
                |      ...
                |      myInitialField = myFeatures.Add("SimInitialField")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimInitialField
                |     named "Initial Field.1" as following:
                | 
                |      ...
                |      myInitialField = myFeatures.Item("Initial Field.1")
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
    def field_variable_number(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FieldVariableNumber() As long
                |     Returns or sets the field variable number.

        :return: int
        """

        return self.com_object.FieldVariableNumber

    @field_variable_number.setter
    def field_variable_number(self, value: int):
        """
        :param int value:
        """

        self.com_object.FieldVariableNumber = value

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
    def uniform_magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformMagnitude() As double
                |     Returns or sets the uniform magnitude. Quantity: DIMENSIONLESS, units:
                |     None. 

        :return: float
        """

        return self.com_object.UniformMagnitude

    @uniform_magnitude.setter
    def uniform_magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.UniformMagnitude = value

    def __repr__(self):
        return f'SimInitialField(name="{ self.name }")'
