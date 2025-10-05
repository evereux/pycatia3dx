"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.sma_mpa_foundation.sim_vector_field import SimVectorField
from pycatia3dx.system.any_object import AnyObject


class SimBodyForce(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimBodyForce
                | 
                | Represents the Body Force object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimBodyForce as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBodyForce As SimBodyForce
                |      Set MyBodyForce = MyFeatures.Add("SimBodyForce")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimBodyForce named "Body
                |     Force.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyBodyForce As SimBodyForce
                |      Set MyBodyForce = MyFeatures.Item("Body Force.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimBodyForce as
                |     following:
                | 
                |      ...
                |      myBodyForce = myFeatures.Add("SimBodyForce")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimBodyForce
                |     named "Body Force.1" as following:
                | 
                |      ...
                |      myBodyForce = myFeatures.Item("Body Force.1")
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
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system used for the body force.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

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
                |     Returns the flag that determines if the magnitude is
                |     uniform.
                |     TRUE: the magnitude is uniform.
                |     FALSE: the magnitude is not uniform.

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

    def get_uniform_magnitude(self, o_fx: float, o_fy: float, o_fz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetUniformMagnitude(double oFx,double oFy,double oFz)
                |     Retrieves the uniform magnitude.
                | 
                |     Parameters:
                | 
                |         oFx[out]
                |             X component of the body force. Quantity: VOLFORCE, units: N_m3.
                |             
                |         oFy[out]
                |             Y component of the body force. Quantity: VOLFORCE, units: N_m3.
                |             
                |         oFz[out]
                |             Z component of the body force. Quantity: VOLFORCE, units: N_m3.
                |             
                | 
                |     Returns:
                |         S_OK if successful.

        :param float o_fx:
        :param float o_fy:
        :param float o_fz:
        :return: None
        """
        return self.com_object.GetUniformMagnitude(o_fx, o_fy, o_fz)

    def set_uniform_magnitude(self, i_fx: float, i_fy: float, i_fz: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUniformMagnitude(double iFx,double iFy,double iFz)
                |     Sets the uniform magnitude.
                | 
                |     Parameters:
                | 
                |         iFx[in]
                |             X component of the body force. Quantity: VOLFORCE, units: N_m3.
                |             
                |         iFy[in]
                |             Y component of the body force. Quantity: VOLFORCE, units: N_m3.
                |             
                |         iFz[in]
                |             Z component of the body force. Quantity: VOLFORCE, units: N_m3.
                |             
                | 
                |     Returns:
                |         S_OK if successful. 

        :param float i_fx:
        :param float i_fy:
        :param float i_fz:
        :return: None
        """
        return self.com_object.SetUniformMagnitude(i_fx, i_fy, i_fz)

    def __repr__(self):
        return f'SimBodyForce(name="{ self.name }")'
