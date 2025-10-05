"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.sma_mpa_foundation.sim_general_vector_field import SimGeneralVectorField
from pycatia3dx.system.any_object import AnyObject


class SimSurfaceTraction(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSurfaceTraction
                | 
                | Represents the Surface Traction object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimSurfaceTraction as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySurfaceTraction As SimSurfaceTraction
                |      Set MySurfaceTraction = MyFeatures.Add("SimSurfaceTraction")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimSurfaceTraction named
                |     "Surface Traction.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MySurfaceTraction As SimSurfaceTraction
                |      Set MySurfaceTraction = MyFeatures.Item("Surface Traction.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimSurfaceTraction
                |     as following:
                | 
                |      ...
                |      mySurfaceTraction = myFeatures.Add("SimSurfaceTraction")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimSurfaceTraction named "Surface Traction.1" as
                |     following:
                | 
                |      ...
                |      mySurfaceTraction = myFeatures.Item("Surface Traction.1")
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
                |     Returns the axis system used for the surface traction.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def constant_resultant_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConstantResultantFlag() As boolean
                |     Returns or sets the flag that determines if the surface traction is
                |     integrated over the surface in the reference
                |     configuration.
                |     Only applicable if the uniform traction flag is TRUE.
                |     TRUE: the surface traction is integrated over the surface in the reference
                |     configuration.
                |     FALSE: the surface traction is integrated over the surface in the current
                |     configuration.

        :return: bool
        """

        return self.com_object.ConstantResultantFlag

    @constant_resultant_flag.setter
    def constant_resultant_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ConstantResultantFlag = value

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
    def follower_load_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FollowerLoadFlag() As boolean
                |     Returns or sets the flag that determines if the surface traction should
                |     follow the deformation of the support.
                |     Only applicable if the uniform traction flag is TRUE.
                |     TRUE: the surface traction remains normal to the support as it
                |     deforms.
                |     FALSE: the surface traction remains in its original orientation as the
                |     support deforms.

        :return: bool
        """

        return self.com_object.FollowerLoadFlag

    @follower_load_flag.setter
    def follower_load_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.FollowerLoadFlag = value

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
    def uniform_traction_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformTractionFlag() As boolean (Read Only)
                |     Returns the flag that determines if the surface traction is
                |     uniform.
                |     TRUE: the surface traction is uniform.
                |     FALSE: the surface traction is not uniform.

        :return: bool
        """

        return self.com_object.UniformTractionFlag

    @property
    def vector_field(self) -> SimGeneralVectorField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VectorField() As SimGeneralVectorField (Read Only)
                |     Returns the vector field.

        :return: SimGeneralVectorField
        """

        return SimGeneralVectorField(self.com_object.VectorField)

    def get_uniform_traction(self, o_traction: float, o_x_comp: float, o_y_comp: float, o_z_comp: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetUniformTraction(double oTraction,double oXComp,double oYComp,double
                | oZComp)
                |     Retrieves the uniform traction and its components.
                |     Only applicable if the uniform traction flag is TRUE.
                | 
                |     Parameters:
                | 
                |         oTraction[out]
                |             Magnitude of traction. Quantity: PRESSURE, Units: N_m2.
                |             
                |         oXComp[out]
                |             X component of the traction vector direction. 
                |         oYComp[out]
                |             Y component of the traction vector direction. 
                |         oZComp[out]
                |             Z component of the traction vector direction.

        :param float o_traction:
        :param float o_x_comp:
        :param float o_y_comp:
        :param float o_z_comp:
        :return: None
        """
        return self.com_object.GetUniformTraction(o_traction, o_x_comp, o_y_comp, o_z_comp)

    def set_uniform_traction(self, i_traction: float, i_x_comp: float, i_y_comp: float, i_z_comp: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUniformTraction(double iTraction,double iXComp,double iYComp,double
                | iZComp)
                |     Sets the uniform traction and its components.
                |     Only applicable if the uniform traction flag is TRUE.
                | 
                |     Parameters:
                | 
                |         iTraction[in]
                |             Magnitude of traction. Quantity: PRESSURE, Units: N_m2.
                |             
                |         iXComp[in]
                |             X component of the traction vector direction. 
                |         iYComp[in]
                |             Y component of the traction vector direction. 
                |         iZComp[in]
                |             Z component of the traction vector direction. 

        :param float i_traction:
        :param float i_x_comp:
        :param float i_y_comp:
        :param float i_z_comp:
        :return: None
        """
        return self.com_object.SetUniformTraction(i_traction, i_x_comp, i_y_comp, i_z_comp)

    def __repr__(self):
        return f'SimSurfaceTraction(name="{ self.name }")'
