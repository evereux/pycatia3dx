"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_spa_structural.sim_general_global_damping import SimGeneralGlobalDamping


class SimSubstructureGenerationStep(SimStep):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaFoundationIDLItf.SimStep
                |                         SimSubstructureGenerationStep
                | 
                | Represents the Substructure Generation Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimSubstructureGenerationStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MySubstructureGenerationStep As
                |      SimSubstructureGenerationStep
                |      Set MySubstructureGenerationStep = MySteps.Add("SubstructureGenerationStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimSubstructureGenerationStep
                |     named "Substructure Generation Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MySubstructureGenerationStep As
                |      SimSubstructureGenerationStep
                |      Set MySubstructureGenerationStep = MySteps.Item("Substructure Generation Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a
                |     SimSubstructureGenerationStep as following:
                | 
                |      ...
                |      mySubstructureGenerationStep = mySteps.Add("SimSubstructureGenerationStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a
                |     SimSubstructureGenerationStep named "Substructure Generation Step.1" as
                |     following:
                | 
                |      ...
                |      mySubstructureGenerationStep = mySteps.Item("Substructure Generation Step.1")
                |      
                | 
                | See also:
                |     SimSteps
    
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
    def frequency_for_dependent_properties(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FrequencyForDependentProperties() As double
                |     Returns or sets the frequency at which the solver evaluates
                |     frequency-dependent material properties. Quantity: FREQUENCY, Units: Hz.

        :return: float
        """

        return self.com_object.FrequencyForDependentProperties

    @frequency_for_dependent_properties.setter
    def frequency_for_dependent_properties(self, value: float):
        """
        :param float value:
        """

        self.com_object.FrequencyForDependentProperties = value

    @property
    def global_damping(self) -> SimGeneralGlobalDamping:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GlobalDamping() As SimGeneralGlobalDamping (Read
                | Only)
                |     Returns the global damping.

        :return: SimGeneralGlobalDamping
        """

        return SimGeneralGlobalDamping(self.com_object.GlobalDamping)

    @property
    def gravity_load_vectors_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GravityLoadVectorsFlag() As boolean
                |     Returns or sets the flag that determines if the gravity vectors will be
                |     generated.
                |     TRUE: the gravity vectors will be generated.
                |     FALSE: the gravity vectors will not be generated.

        :return: bool
        """

        return self.com_object.GravityLoadVectorsFlag

    @gravity_load_vectors_flag.setter
    def gravity_load_vectors_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.GravityLoadVectorsFlag = value

    @property
    def interface_support(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterfaceSupport() As CATBaseDispatch (Read Only)
                |     Returns the interface support.

        :return: AnyObject
        """

        return AnyObject(self.com_object.InterfaceSupport)

    @property
    def motion_analysis_data_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MotionAnalysisDataFlag() As boolean
                |     Returns or sets the flag that determines if the Simpack flexible body will
                |     be generated.
                |     TRUE: the Simpack flexible body will be generated.
                |     FALSE: the Simpack flexible body will not be generated.

        :return: bool
        """

        return self.com_object.MotionAnalysisDataFlag

    @motion_analysis_data_flag.setter
    def motion_analysis_data_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.MotionAnalysisDataFlag = value

    @property
    def recovery_domain(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RecoveryDomain() As CATBaseDispatch (Read Only)
                |     Returns the recovery domain.

        :return: AnyObject
        """

        return AnyObject(self.com_object.RecoveryDomain)

    @property
    def recovery_domain_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property RecoveryDomainFlag() As boolean
                |     Returns or sets the flag that determines if the recovery domain is
                |     specified.
                |     TRUE: the recovery domain is specified.
                |     FALSE: the recovery domain is not specified.

        :return: bool
        """

        return self.com_object.RecoveryDomainFlag

    @recovery_domain_flag.setter
    def recovery_domain_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.RecoveryDomainFlag = value

    @property
    def reduced_mass_matrix_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReducedMassMatrixFlag() As boolean
                |     Returns or sets the flag that determines if a reduced mass matrix will be
                |     generated.
                |     TRUE: reduced mass matrix will be generated.
                |     FALSE: reduced mass matrix will not be generated.

        :return: bool
        """

        return self.com_object.ReducedMassMatrixFlag

    @reduced_mass_matrix_flag.setter
    def reduced_mass_matrix_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ReducedMassMatrixFlag = value

    @property
    def reduced_structural_damping_matrix_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReducedStructuralDampingMatrixFlag() As boolean
                |     Returns or sets the flag that determines if a reduced structural damping
                |     matrix will be generated.
                |     TRUE: reduced structural damping matrix will be generated.
                |     FALSE: reduced structural damping matrix will not be generated.

        :return: bool
        """

        return self.com_object.ReducedStructuralDampingMatrixFlag

    @reduced_structural_damping_matrix_flag.setter
    def reduced_structural_damping_matrix_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ReducedStructuralDampingMatrixFlag = value

    @property
    def reduced_viscous_damping_matrix_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ReducedViscousDampingMatrixFlag() As boolean
                |     Returns or sets the flag that determines if a reduced viscous damping
                |     matrix will be generated.
                |     TRUE: reduced viscous damping matrix will be generated.
                |     FALSE: reduced viscous damping matrix will not be generated.

        :return: bool
        """

        return self.com_object.ReducedViscousDampingMatrixFlag

    @reduced_viscous_damping_matrix_flag.setter
    def reduced_viscous_damping_matrix_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ReducedViscousDampingMatrixFlag = value

    @property
    def substructure_fem(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubstructureFEM() As CATBaseDispatch (Read Only)
                |     Returns the substructure FEM.

        :return: AnyObject
        """

        return AnyObject(self.com_object.SubstructureFEM)

    @property
    def substructure_identifier(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SubstructureIdentifier() As long
                |     Returns or sets the substructure identifier. Quantity: DIMENSIONLESS,
                |     Units: None.

        :return: int
        """

        return self.com_object.SubstructureIdentifier

    @substructure_identifier.setter
    def substructure_identifier(self, value: int):
        """
        :param int value:
        """

        self.com_object.SubstructureIdentifier = value

    def create_substructure_fem(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CreateSubstructureFEM() As CATBaseDispatch
                |     Creates the substructure FEM.

        :return: AnyObject
        """
        return self.com_object.CreateSubstructureFEM()

    def remove_substructure_fem(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveSubstructureFEM()
                |     Removes the substructure FEM. 

        :return: None
        """
        return self.com_object.RemoveSubstructureFEM()

    def __repr__(self):
        return f'SimSubstructureGenerationStep(name="{ self.name }")'
