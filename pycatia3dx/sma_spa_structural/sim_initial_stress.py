"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_symmetric_tensor_field import SimSymmetricTensorField
from pycatia3dx.system.any_object import AnyObject


class SimInitialStress(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimInitialStress
                | 
                | Represents the Initial Stress object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimInitialStress as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialStress As SimInitialStress
                |      Set MyInitialStress = MyFeatures.Add("SimInitialStress")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimInitialStress named
                |     "Initial Stress.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyInitialStress As SimInitialStress
                |      Set MyInitialStress = MyFeatures.Item("Initial Stress.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimInitialStress as
                |     following:
                | 
                |      ...
                |      myInitialStress = myFeatures.Add("SimInitialStress")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimInitialStress
                |     named "Initial Stress.1" as following:
                | 
                |      ...
                |      myInitialStress = myFeatures.Item("Initial Stress.1")
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
    def rebar_prestress(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RebarPrestress() As double
                |     Returns or sets the rebar prestress. Quantity: STRESS, units: N_m2

        :return: float
        """

        return self.com_object.RebarPrestress

    @rebar_prestress.setter
    def rebar_prestress(self, value: float):
        """
        :param float value:
        """

        self.com_object.RebarPrestress = value

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
    def stress_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StressType() As SimInitialStressType
                |     Returns or sets the stress type.

        :return: SimInitialStressType
        """

        return self.com_object.StressType

    @stress_type.setter
    def stress_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.StressType = value

    @property
    def tensor_field(self) -> SimSymmetricTensorField:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TensorField() As SimSymmetricTensorField (Read Only)
                |     Returns the tensor field.

        :return: SimSymmetricTensorField
        """

        return SimSymmetricTensorField(self.com_object.TensorField)

    @property
    def uniform_tensor_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UniformTensorFlag() As boolean (Read Only)
                |     Retrieves the flag that determines if the initial stress is uniform on the
                |     support.
                | 
                |     Parameters:
                | 
                |         oIsUniform[out]
                |             TRUE: the initial stress is uniform.
                |             FALSE: the initial stress is not uniform. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: bool
        """

        return self.com_object.UniformTensorFlag

    def get_uniform_tensor_components(self, o_sigma11: float, o_sigma22: float, o_sigma33: float, o_sigma12: float, o_sigma13: float, o_sigma23: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetUniformTensorComponents(double oSigma11,double oSigma22,double
                | oSigma33,double oSigma12,double oSigma13,double oSigma23)
                |     Retrieves the uniform tensor stress components.
                |     This method is only applicable if the uniform tensor flag is
                |     TRUE.
                | 
                |     Parameters:
                | 
                |         oSigma11[out]
                |             The Sigma 11 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         oSigma22[out]
                |             The Sigma 22 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         oSigma33[out]
                |             The Sigma 33 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         oSigma12[out]
                |             The Sigma 12 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         oSigma13[out]
                |             The Sigma 13 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         oSigma23[out]
                |             The Sigma 23 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                | 
                |     Returns:
                |         S_OK if successful.

        :param float o_sigma11:
        :param float o_sigma22:
        :param float o_sigma33:
        :param float o_sigma12:
        :param float o_sigma13:
        :param float o_sigma23:
        :return: None
        """
        return self.com_object.GetUniformTensorComponents(o_sigma11, o_sigma22, o_sigma33, o_sigma12, o_sigma13, o_sigma23)

    def set_uniform_tensor_components(self, i_sigma11: float, i_sigma22: float, i_sigma33: float, i_sigma12: float, i_sigma13: float, i_sigma23: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetUniformTensorComponents(double iSigma11,double iSigma22,double
                | iSigma33,double iSigma12,double iSigma13,double iSigma23)
                |     Sets the uniform tensor stress components.
                |     This method is only applicable if the uniform tensor flag is
                |     TRUE.
                | 
                |     Parameters:
                | 
                |         iSigma11[in]
                |             The Sigma 11 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         iSigma22[in]
                |             The Sigma 22 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         iSigma33[in]
                |             The Sigma 33 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         iSigma12[in]
                |             The Sigma 12 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         iSigma13[in]
                |             The Sigma 13 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                |         iSigma23[in]
                |             The Sigma 23 component of the stress tensor. Quantity: STRESS,
                |             units: N_m2 
                | 
                |     Returns:
                |         S_OK if successful. 

        :param float i_sigma11:
        :param float i_sigma22:
        :param float i_sigma33:
        :param float i_sigma12:
        :param float i_sigma13:
        :param float i_sigma23:
        :return: None
        """
        return self.com_object.SetUniformTensorComponents(i_sigma11, i_sigma22, i_sigma33, i_sigma12, i_sigma13, i_sigma23)

    def __repr__(self):
        return f'SimInitialStress(name="{ self.name }")'
