"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_feature_history import SimFeatureHistory
from pycatia3dx.system.any_object import AnyObject


class SimConnectorDisplacementRestraint(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimConnectorDisplacementRestraint
                | 
                | Represents the Connector Displacement Restraint object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a
                |     SimConnectorDisplacementRestraint as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyConnectorDisplacementRestraint As
                |      SimConnectorDisplacementRestraint
                |      Set MyConnectorDisplacementRestraint = MyFeatures.Add("SimConnectorDisplacementRestraint")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a
                |     SimConnectorDisplacementRestraint named "Connector Displacement Restraint.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyConnectorDisplacementRestraint As
                |      SimConnectorDisplacementRestraint
                |      Set MyConnectorDisplacementRestraint = MyFeatures.Item("Connector Displacement Restraint.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a
                |     SimConnectorDisplacementRestraint as following:
                | 
                |      ...
                |      myConnectorDisplacementRestraint = myFeatures.Add("SimConnectorDisplacementRestraint")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a
                |     SimConnectorDisplacementRestraint named "Connector Displacement Restraint.1" as
                |     following:
                | 
                |      ...
                |      myConnectorDisplacementRestraint = myFeatures.Item("Connector Displacement Restraint.1")
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
                |     Returns the list of available connector components of relative motion. The list can contains the following values: 1 : the first translation DOF is available, 2 : the second translation DOF is available, 3 : the third translation DOF is available, 4 : the first rotation DOF is available, 5 : the second rotation DOF is available, 6 : the third rotation DOF is available.

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
                |     feature. Possible values are:
                | 
                |         Abstractions
                |         Amplitudes
                |         Controls
                |         Connections
                |         Damping
                |         ElementTypeAssignments
                |         Envelopes
                |         FieldPlots
                |         FlowConditions
                |         HistoryPlots
                |         InitialConditions
                |         Interactions
                |         LinearLoadCases
                |         Loads
                |         LoadSets
                |         OutputRequests
                |         PredefinedFields
                |         Properties
                |         Restraints
                |         Sensors
                |         Streams
                |         ThermalConditions
                |         NotDefined

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

        :param SimDof i_degree_of_freedom:
        :return: bool
        """
        return self.com_object.GetDofRestraint(i_degree_of_freedom)

    def set_dof_restraint(self, i_degree_of_freedom: int, i_restraint_flag: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetDofRestraint(SimDof iDegreeOfFreedom,boolean
                | iRestraintFlag)
                |     Sets the flag that determines if the displacement is restrained in the
                |     specified DOF.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom. 
                |         iRestraintFlag[in]
                |             TRUE: the specified DOF is restrained.
                |             FALSE: the specified DOF is not restrained. 

        :param SimDof i_degree_of_freedom:
        :param bool i_restraint_flag:
        :return: None
        """
        return self.com_object.SetDofRestraint(i_degree_of_freedom, i_restraint_flag)

    def __repr__(self):
        return f'SimConnectorDisplacementRestraint(name="{ self.name }")'
