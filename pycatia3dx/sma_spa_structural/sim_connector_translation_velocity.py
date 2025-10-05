"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimConnectorTranslationVelocity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimConnectorTranslationVelocity
                | 
                | Represents the Connector Translation Velocity object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a
                |     SimConnectorTranslationVelocity as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyConnectorTranslationVelocity As
                |      SimConnectorTranslationVelocity
                |      Set MyConnectorTranslationVelocity = MyFeatures.Add("SimConnectorTranslationVelocity")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a
                |     SimConnectorTranslationVelocity named "Connector Translation Velocity.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyConnectorTranslationVelocity As
                |      SimConnectorTranslationVelocity
                |      Set MyConnectorTranslationVelocity = MyFeatures.Item("Connector Translation Velocity.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimConnectorTranslationVelocity as following:
                | 
                |      ...
                |      myConnectorTranslationVelocity = myFeatures.Add("SimConnectorTranslationVelocity")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimConnectorTranslationVelocity named "Connector Translation Velocity.1" as
                |     following:
                | 
                |      ...
                |      myConnectorTranslationVelocity = myFeatures.Item("Connector Translation Velocity.1")
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
    def available_connector_components(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AvailableConnectorComponents() As CATSafeArrayVariant (Read
                | Only)
                |     Returns the list of available connector components of relative
                |     motion.
                |     The list can contains the following values:
                |     1 : the first translation DOF is available.
                |     2 : the second translation DOF is available.
                |     3 : the third translation DOF is available.

        :return: tuple
        """

        return self.com_object.AvailableConnectorComponents

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
    def variation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VariationType() As
                | SimConnectorTranslationVelocityVariationType
                |     Returns or sets the variation type.

        :return: int
        """

        return self.com_object.VariationType

    @variation_type.setter
    def variation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.VariationType = value

    def get_translation_velocity(self, i_degree_of_freedom: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTranslationVelocity(SimDof iDegreeOfFreedom) As double
                |     Retrieves the velocity value for a degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom.
                |             Valid input values are : SimTranslation1, SimTranslation2 and SimTranslation3 
                |         oTranslationVelocity[out]
                |             The velocity value. Quantity: SPEED, Units: m_s.

        :param int i_degree_of_freedom:
        :return: float
        """
        return self.com_object.GetTranslationVelocity(i_degree_of_freedom)

    def get_translation_velocity_activation_flag(self, i_degree_of_freedom: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTranslationVelocityActivationFlag(SimDof iDegreeOfFreedom) As
                | boolean
                |     Retrieves the flag which determines if a translation velocity is active on
                |     a degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom.
                |             Valid input values are : SimTranslation1, SimTranslation2 and SimTranslation3 
                |         oTranslationVelocityActivationFlag[out]
                |             The activation flag.
                |             TRUE : the translation velocity is active for the specified DOF.
                |             FALSE : the translation velocity is not active for the specified DOF.

        :param int i_degree_of_freedom:
        :return: bool
        """
        return self.com_object.GetTranslationVelocityActivationFlag(i_degree_of_freedom)

    def set_translation_velocity(self, i_degree_of_freedom: int, i_translation_velocity: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTranslationVelocity(SimDof iDegreeOfFreedom,double
                | iTranslationVelocity)
                |     Sets the velocity value for a degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom.
                |             Valid input values are : SimTranslation1, SimTranslation2 and SimTranslation3 
                |         iTranslationVelocity[in]
                |             The velocity value. Quantity: SPEED, Units: m_s.

        :param int i_degree_of_freedom:
        :param float i_translation_velocity:
        :return: None
        """
        return self.com_object.SetTranslationVelocity(i_degree_of_freedom, i_translation_velocity)

    def set_translation_velocity_activation_flag(self, i_degree_of_freedom: int, i_translation_velocity_activation_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetTranslationVelocityActivationFlag(SimDof iDegreeOfFreedom,boolean
                | iTranslationVelocityActivationFlag)
                |     Set the flag which determines if a translation velocity is active on a
                |     degree of freedom.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom.
                |             Valid input values are : SimTranslation1, SimTranslation2 and SimTranslation3 
                |         iTranslationVelocityActivationFlag[in]
                |             The activation flag.
                |             TRUE : the translation velocity is active for the specified DOF.
                |             FALSE : the translation velocity is not active for the specified DOF. 

        :param SimDof i_degree_of_freedom:
        :param bool i_translation_velocity_activation_flag:
        :return: None
        """
        return self.com_object.SetTranslationVelocityActivationFlag(i_degree_of_freedom, i_translation_velocity_activation_flag)

    def __repr__(self):
        return f'SimConnectorTranslationVelocity(name="{ self.name }")'
