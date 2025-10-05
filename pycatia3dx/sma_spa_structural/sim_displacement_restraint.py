"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimDisplacementRestraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimDisplacementRestraint
                | 
                | Represents the Displacement Restraint object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimDisplacementRestraint as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyDisplacementRestraint As SimDisplacementRestraint
                |      Set MyDisplacementRestraint = MyFeatures.Add("SimDisplacementRestraint")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimDisplacementRestraint
                |     named "Displacement Restraint.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyDisplacementRestraint As SimDisplacementRestraint
                |      Set MyDisplacementRestraint = MyFeatures.Item("Displacement Restraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimDisplacementRestraint as following:
                | 
                |      ...
                |      myDisplacementRestraint = myFeatures.Add("SimDisplacementRestraint")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimDisplacementRestraint named "Displacement Restraint.1" as
                |     following:
                | 
                |      ...
                |      myDisplacementRestraint = myFeatures.Item("Displacement Restraint.1")
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
                |     Returns the axis system.

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
    def secondary_base_applied_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondaryBaseAppliedFlag() As boolean
                |     Returns or sets the flag that determines if secondary base is applied.
                |     TRUE: secondary base is applied
                |     FALSE: secondary base is not applied .

        :return: bool
        """

        return self.com_object.SecondaryBaseAppliedFlag

    @secondary_base_applied_flag.setter
    def secondary_base_applied_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SecondaryBaseAppliedFlag = value

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

    def get_dof_restraint(self, i_degree_of_freedom: int) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetDofRestraint(SimDof iDegreeOfFreedom) As boolean
                |     Retrieves the flag that determines if the displacement is restrained in the
                |     specified DOF.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom. 
                | 
                |     Returns:
                |         TRUE: the specified DOF is restrained.
                |         FALSE: the specified DOF is not restrained.

        :param int i_degree_of_freedom:
        :return: bool
        """
        return self.com_object.GetDofRestraint(i_degree_of_freedom)

    def set_dof_restraint(self, i_degree_of_freedom: int, i_restraint: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDofRestraint(SimDof iDegreeOfFreedom,boolean
                | iRestraint)
                |     Sets the flag that determines if the displacement is restrained in the
                |     specified DOF.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom. 
                |         iRestraint[in]
                |             TRUE: the specified DOF is restrained.
                |             FALSE: the specified DOF is not restrained. 

        :param SimDof i_degree_of_freedom:
        :param bool i_restraint:
        :return: None
        """
        return self.com_object.SetDofRestraint(i_degree_of_freedom, i_restraint)

    def __repr__(self):
        return f'SimDisplacementRestraint(name="{ self.name }")'
