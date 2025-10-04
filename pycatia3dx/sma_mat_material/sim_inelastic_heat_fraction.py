"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimInelasticHeatFraction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimInelasticHeatFraction
                | 
                | Represents the Inelastic Heat Fraction object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a
                |     SimInelasticHeatFraction as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyInelasticHeatFraction As SimInelasticHeatFraction
                |      Set MyInelasticHeatFraction = MyMaterialOptions.Add("SimInelasticHeatFraction")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a
                |     SimInelasticHeatFraction named "Inelastic Heat Fraction.1" as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyInelasticHeatFraction As SimInelasticHeatFraction
                |      Set MyInelasticHeatFraction = MyMaterialOptions.Item("Inelastic Heat Fraction.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimInelasticHeatFraction as following:
                | 
                |      ...
                |      myInelasticHeatFraction = myMaterialOptions.Add("SimInelasticHeatFraction")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimInelasticHeatFraction named "Inelastic Heat Fraction.1" as
                |     following:
                | 
                |      ...
                |      myInelasticHeatFraction = myMaterialOptions.Item("Inelastic Heat Fraction.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def inelastic_heat_fraction(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InelasticHeatFraction() As double
                |     Inelastic Heat Fraction. Quantity : Real, Units : None 

        :return: float
        """

        return self.com_object.InelasticHeatFraction

    @inelastic_heat_fraction.setter
    def inelastic_heat_fraction(self, value: float):
        """
        :param float value:
        """

        self.com_object.InelasticHeatFraction = value

    def __repr__(self):
        return f'SimInelasticHeatFraction(name="{ self.name }")'
