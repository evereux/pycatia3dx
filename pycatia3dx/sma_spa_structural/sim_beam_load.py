"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.sma_mpa_foundation.sim_vector_field import SimVectorField
from pycatia3dx.system.any_object import AnyObject


class SimBeamLoad(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBeamLoad
                | 
                | Represents the Beam Load object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimBeamLoad as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBeamLoad As SimBeamLoad
                |      Set MyBeamLoad = MyFeatures.Add("SimBeamLoad")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimBeamLoad named "Beam
                |     Load.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBeamLoad As SimBeamLoad
                |      Set MyBeamLoad = MyFeatures.Item("Beam Load.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimBeamLoad as
                |     following:
                | 
                |      ...
                |      myBeamLoad = myFeatures.Add("SimBeamLoad")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimBeamLoad named
                |     "Beam Load.1" as following:
                | 
                |      ...
                |      myBeamLoad = myFeatures.Item("Beam Load.1")
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
    def component_system(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ComponentSystem() As SimBeamLoadComponentSystem
                |     Returns or sets the component system.

        :return: int
        """

        return self.com_object.ComponentSystem

    @component_system.setter
    def component_system(self, value: int):
        """
        :param int value:
        """

        self.com_object.ComponentSystem = value

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
    def is_local_system_allowed(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IsLocalSystemAllowed() As boolean (Read Only)
                |     Retrieves if the beam load allows local system for
                |     components.
                |     TRUE: the beam load allows local system.
                |     FALSE: the beam load disallows local system.

        :return: bool
        """

        return self.com_object.IsLocalSystemAllowed

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
    def uniform_magnitude_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformMagnitudeFlag() As boolean (Read Only)
                |     Retrieves the flag that determines if the beam load is
                |     uniform.
                |     TRUE: the beam load is uniform.
                |     FALSE: the beam load is not uniform.

        :return: bool
        """

        return self.com_object.UniformMagnitudeFlag

    @property
    def vector_field(self) -> SimVectorField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VectorField() As SimVectorField (Read Only)
                |     Returns the vector field.

        :return: SimVectorField
        """

        return SimVectorField(self.com_object.VectorField)

    def get_magnitude(self, o_fx: float, o_fy: float, o_fz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetMagnitude(double oFx,double oFy,double oFz)
                |     Retrieves the uniform magnitude.
                | 
                |     Parameters:
                | 
                |         oFx[out]
                |             X or 1 component of the beam load. Quantity: FORCE_PER_LENGTH,
                |             units: kg_s2 
                |         oFy[out]
                |             Y or 2 component of the beam load. Quantity: FORCE_PER_LENGTH,
                |             units: kg_s2 
                |         oFz[out]
                |             Z component of the beam load, or ignored. Quantity:
                |             FORCE_PER_LENGTH, units: kg_s2

        :param float o_fx:
        :param float o_fy:
        :param float o_fz:
        :return: None
        """
        return self.com_object.GetMagnitude(o_fx, o_fy, o_fz)

    def set_magnitude(self, i_fx: float, i_fy: float, i_fz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetMagnitude(double iFx,double iFy,double iFz)
                |     Sets the uniform magnitude.
                | 
                |     Parameters:
                | 
                |         iFx[in]
                |             X or 1 component of the beam load. Quantity: FORCE_PER_LENGTH,
                |             units: kg_s2 
                |         iFy[in]
                |             Y or 2 component of the beam load. Quantity: FORCE_PER_LENGTH,
                |             units: kg_s2 
                |         iFz[in]
                |             Z component of the beam load, or ignored. Quantity:
                |             FORCE_PER_LENGTH, units: kg_s2 

        :param float i_fx:
        :param float i_fy:
        :param float i_fz:
        :return: None
        """
        return self.com_object.SetMagnitude(i_fx, i_fy, i_fz)

    def __repr__(self):
        return f'SimBeamLoad(name="{ self.name }")'
