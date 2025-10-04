"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimDamping(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDamping
                | 
                | Represents the Damping object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimDamping as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDamping As SimDamping
                |      Set MyDamping = MyMaterialOptions.Add("SimDamping")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimDamping named
                |     "Damping.1" as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyDamping As SimDamping
                |      Set MyDamping = MyMaterialOptions.Item("Damping.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimDamping as following:
                | 
                |      ...
                |      myDamping = myMaterialOptions.Add("SimDamping")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimDamping named "Damping.1" as following:
                | 
                |      ...
                |      myDamping = myMaterialOptions.Item("Damping.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def alpha(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Alpha() As double
                |     Returns or sets the stiffness proportional damping value. Quantity : FREQUENCY, Units : Hz

        :return: float
        """

        return self.com_object.Alpha

    @alpha.setter
    def alpha(self, value: float):
        """
        :param float value:
        """

        self.com_object.Alpha = value

    @property
    def beta(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Beta() As double
                |     Returns or sets the mass proportional damping value. Quantity : TIME, Units : s

        :return: float
        """

        return self.com_object.Beta

    @beta.setter
    def beta(self, value: float):
        """
        :param float value:
        """

        self.com_object.Beta = value

    @property
    def structural(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Structural() As double
                |     Returns or sets the structural damping value. Quantity : Real, Units : None

        :return: float
        """

        return self.com_object.Structural

    @structural.setter
    def structural(self, value: float):
        """
        :param float value:
        """

        self.com_object.Structural = value

    def __repr__(self):
        return f'SimDamping(name="{ self.name }")'
