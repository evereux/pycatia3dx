"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.sma_mpa_structural_mode.sim_surface_fluid_cavity import SimSurfaceFluidCavity
from pycatia3dx.system.any_object import AnyObject


class SimCavityPressure(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCavityPressure
                | 
                | Represents the Cavity Pressure object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimCavityPressure as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyCavityPressure As SimCavityPressure
                |      Set MyCavityPressure = MyFeatures.Add("SimCavityPressure")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimCavityPressure named
                |     "Cavity Pressure.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyCavityPressure As SimCavityPressure
                |      Set MyCavityPressure = MyFeatures.Item("Cavity Pressure.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimCavityPressure
                |     as following:
                | 
                |      ...
                |      myCavityPressure = myFeatures.Add("SimCavityPressure")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimCavityPressure
                |     named "Cavity Pressure.1" as following:
                | 
                |      ...
                |      myCavityPressure = myFeatures.Item("Cavity Pressure.1")
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
    def cavity(self) -> SimSurfaceFluidCavity:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Cavity() As SimSurfaceFluidCavity
                |     Returns or sets the surface fluid cavity.

        :return: SimSurfaceFluidCavity
        """

        return SimSurfaceFluidCavity(self.com_object.Cavity)

    @cavity.setter
    def cavity(self, value: SimSurfaceFluidCavity):
        """
        :param SimSurfaceFluidCavity value:
        """

        self.com_object.Cavity = value

    @property
    def feature_history(self) -> SimFeatureHistory:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FeatureHistory() As SimFeatureHistory (Read Only)
                |     Returns the feature history.

        :return: SimFeatureHistory
        """

        return SimFeatureHistory(self.com_object.FeatureHistory)

    @property
    def pressure(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Pressure() As double
                |     Returns or sets the cavity pressure. Quantity: PRESSURE, units: N_m2

        :return: float
        """

        return self.com_object.Pressure

    @pressure.setter
    def pressure(self, value: float):
        """
        :param float value:
        """

        self.com_object.Pressure = value

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

    def __repr__(self):
        return f'SimCavityPressure(name="{ self.name }")'
