"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity
from pycatia3dx.plm_interference.interference_group_objects import InterferenceGroupObjects
from pycatia3dx.plm_interference.interference_results import InterferenceResults


class InterferenceSimulation(PLMEntity):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     PLMModelerBaseIDLItf.PLMEntity
                |                         InterferenceSimulation
                | 
                | Interface representing Interference Simulation Object.
                | This interface enables to manage Interference Simulation.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def clearance_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClearanceValue() As double
                |     Sets or returns the clearance value.
                | 
                |     Example:
                | 
                |            This example sets the value of Clearance of 32 mm to the
                |            InterferenceSimulation iSimu .
                |            
                | 
                |            Dim ValClear As Double
                |            ValClear = 0.032
                |            iSimu.ClearanceValue = ValClear

        :return: float
        """

        return self.com_object.ClearanceValue

    @clearance_value.setter
    def clearance_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.ClearanceValue = value

    @property
    def first_group_objects(self) -> InterferenceGroupObjects:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FirstGroupObjects() As InterferenceGroupObjects (Read
                | Only)
                |     Returns the first Groups.
                | 
                |     Deprecated:
                |         R213. use GetGroupObjects

        :return: InterferenceGroupObjects
        """

        return InterferenceGroupObjects(self.com_object.FirstGroupObjects)

    @property
    def group_computation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GroupComputationType() As
                | CatInterferenceGroupComputationType
                |     Sets or returns the InterferenceGroupComputationType.
                | 
                |     Deprecated:
                |         R213. use GroupComputationType2

        :return: int
        """

        return self.com_object.GroupComputationType

    @group_computation_type.setter
    def group_computation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.GroupComputationType = value

    @property
    def group_computation_type2(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property GroupComputationType2() As
                | CatInterferenceGroupComputationType2
                |     Sets or returns the InterferenceGroupComputationType2 .
                |     If you set the "GroupComputationType2", the number of groups can be
                |     modified in order to have a similar behavior than the method
                |     InterferenceServices.CreateInterferenceSimulation2 .
                |     If the new value of InterferenceGroupComputationType2 is:
                | 
                |         catInterferenceGroupComputationTypeAllAgainstAllInGroup
                |         :
                |             One group is created if there is no existing group because one
                |             group at least is necessary.
                |             In the others cases, the number of group is not
                |             modified.
                |         catInterferenceGroupComputationTypeGroupAgainstGroup :
                |             Two groups are created if there is no existing
                |             group.
                |             One group is created if there is one existing
                |             group.
                |             In the others cases, the number of group is not
                |             modified.
                |         catInterferenceGroupComputationTypeGroupAgainstContext : Only one group is supported in this case. So :
                |             One group is created if there is no existing
                |             group.
                |             If there are more than one group, only the first group is kept, the
                |             others are removed.
                |         catInterferenceGroupComputationTypeAllAgainstAllInContext
                |         :
                |             No group is necessary in this case so, all the existings groups are
                |             removed.
                | 
                | 
                |     Example:
                | 
                |            This example sets the GroupComputationType2
                |            "catInterferenceGroupComputationTypeGroupAgainstGroup" GroupCmpType2 to the
                |            InterferenceSimulation iSimu .
                |            
                | 
                |            Dim GroupCmpType2 As
                |            CatInterferenceGroupComputationType2
                |            GroupCmpType2 = catInterferenceGroupComputationTypeGroupAgainstGroup
                |            iSimu.GroupComputationType2 = GroupCmpType2

        :return: int
        """

        return self.com_object.GroupComputationType2

    @group_computation_type2.setter
    def group_computation_type2(self, value: int):
        """
        :param int value:
        """

        self.com_object.GroupComputationType2 = value

    @property
    def interference_comparison(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterferenceComparison() As CatInterferenceComparison
                |     Sets or returns the InterferenceComparison.
                |     By default, Interference Simulation is created with the option:
                |     catInterferenceComparisonRecomputeModify.
                | 
                |     Example:
                | 
                |            This example sets the mode of comparison
                |            "catInterferenceComparisonDeleteOutOfScope" to the InterferenceSimulation iSimu
                |            .
                |            
                | 
                |            iSimu.InterferenceComparison = catInterferenceComparisonDeleteOutOfScope

        :return: int
        """

        return self.com_object.InterferenceComparison

    @interference_comparison.setter
    def interference_comparison(self, value: int):
        """
        :param int value:
        """

        self.com_object.InterferenceComparison = value

    @property
    def interference_intermediate_representation(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterferenceIntermediateRepresentation() As
                | CatInterferenceIntermediateRepresentation
                |     Sets or returns the option for intermediate
                |     representation.
                |     By default, Interference Simulation is created with the option:
                |     catInterferenceInterRepNone .
                | 
                |     Example:
                | 
                |            This example sets the taken into account of the intermediate
                |            representations during computation for the InterferenceSimulation iSimu
                |            .
                |
                |            Dim InterferenceInterRep As
                |            CatInterferenceIntermediateRepresentation
                |            InterferenceInterRep = catInterferenceInterRepAppend
                |            iSimu.InterferenceIntermediateRepresentation = InterferenceInterRep

        :return: int
        """

        return self.com_object.InterferenceIntermediateRepresentation

    @interference_intermediate_representation.setter
    def interference_intermediate_representation(self, value: int):
        """
        :param int value:
        """

        self.com_object.InterferenceIntermediateRepresentation = value

    @property
    def interference_results(self) -> InterferenceResults:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterferenceResults() As InterferenceResults (Read
                | Only)
                |     Retrieves the Interference Result.
                |     Role: This method retrieves a collection of Interferences results generated
                |     during InterferenceSimulation execution.
                |     see InterferenceResults
                | 
                |     Parameters:
                | 
                |         CATIAInterferenceResults.
                | 
                |     Returns:
                |         InterferenceResult collection.
                |     Example:
                | 
                |            This example retrieves the InterferenceResults ListInterference of
                |            the InterferenceSimulation iSimu .
                |            
                | 
                |            Dim ListInterference As InterferenceResults
                |            Set ListInterference = iSimu.InterferenceResults

        :return: InterferenceResults
        """

        return InterferenceResults(self.com_object.InterferenceResults)

    @property
    def interference_specification_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property InterferenceSpecificationType() As
                | CatInterferenceSpecificationType
                |     Sets or returns the InterferenceSpecificationType.
                |     This concerns only the standard specification of the
                |     simulation.
                |     see AddItfSpecificationTypeEngCnx method to use an engineering connection
                |     specification
                |     see PutRuleSetByName method to use a knowledge rules
                |     specification.
                | 
                |     A specification (standard specification or engineering connection
                |     specification or knowledge rules specification) must always be
                |     active.
                |     So, to remove the taking account of the standard specification
                |     (catInterferenceSpecificationTypeNone), one of the others specifications
                |     (engineering connection specification with the option "No Check" unchecked or
                |     knowledge rules specification) has to be added before.
                | 
                |     Example:
                | 
                |            This example sets the InterferenceSpecificationType ItfSpecTypeStd
                |            of type Clearance to the InterferenceSimulation iSimu
                |            .
                |            
                | 
                |            Dim ItfSpecTypeStd As
                |            CatInterferenceSpecificationType
                |            ItfSpecTypeStd = catInterferenceSpecificationTypeClearance
                |            iSimu.InterferenceSpecificationType = ItfSpecTypeStd

        :return: int
        """

        return self.com_object.InterferenceSpecificationType

    @interference_specification_type.setter
    def interference_specification_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.InterferenceSpecificationType = value

    @property
    def second_group_objects(self) -> InterferenceGroupObjects:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondGroupObjects() As InterferenceGroupObjects (Read
                | Only)
                |     Returns the second Groups.
                | 
                |     Deprecated:
                |         R213. use GetGroupObjects

        :return: InterferenceGroupObjects
        """

        return InterferenceGroupObjects(self.com_object.SecondGroupObjects)

    def add_compute_quantifier(self, i_quantifier_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddComputeQuantifier(CatInterferenceComputeQuantifier
                | iQuantifierMode)
                |     Adds the computation of a quantifier.
                |     By default, Interference Simulation is created without the computation of
                |     any quantifier.
                | 
                |     Example:
                | 
                |            This example adds the computation of the quantifier of minimum
                |            distance to the InterferenceSimulation iSimu .
                |            
                | 
                |            Dim InterferenceQuantifier As
                |            CatInterferenceComputeQuantifier
                |            InterferenceQuantifier = catInterferenceComputeQuantifierMinimumDistance
                |            iSimu.AddComputeQuantifier InterferenceQuantifier

        :param int i_quantifier_mode:
        :return: None
        """
        return self.com_object.AddComputeQuantifier(i_quantifier_mode)

    def add_group_objects(self, o_groups: InterferenceGroupObjects) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddGroupObjects(InterferenceGroupObjects oGroups)
                |     Adds a Group (if possible) and return it.
                |     This method adds a group only if this is possible depending of the value of
                |     the parameter CatInterferenceGroupComputationType2 .
                |     If the value of InterferenceGroupComputationType2 is:
                | 
                |         catInterferenceGroupComputationTypeAllAgainstAllInGroup : groups can be added.
                |         catInterferenceGroupComputationTypeGroupAgainstGroup : groups can be added.
                |         catInterferenceGroupComputationTypeGroupAgainstContext : no group can be added because only one group is supported in this case.
                |         catInterferenceGroupComputationTypeAllAgainstAllInContext : no group can be added because no group is necessary in this case.
                | 
                | 
                |     Example:
                | 
                |            This example sets the GroupComputationType2
                |            "catInterferenceGroupComputationTypeGroupAgainstGroup" GroupCmpType2
                |            
                |            to the InterferenceSimulation iSimu and adds a new group
                |            NewGroup.
                |            
                | 
                |            Dim GroupCmpType2 As
                |            CatInterferenceGroupComputationType2
                |            Dim NewGroup      As InterferenceGroupObjects
                |            GroupCmpType2 = catInterferenceGroupComputationTypeGroupAgainstGroup
                |            iSimu.GroupComputationType2 = GroupCmpType2
                |            iSimu.AddGroupObjects NewGroup

        :param InterferenceGroupObjects o_groups:
        :return: None
        """
        return self.com_object.AddGroupObjects(o_groups.com_object)

    def add_itf_specification_type_eng_cnx(self, i_type_eng_cnx: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddItfSpecificationTypeEngCnx(CatInterferenceSpecificationTypeEngCnx
                | iTypeEngCnx)
                |     Adds the type of engineering connection specification to take into
                |     account.
                |     The following values can be added one by one:
                | 
                |         catInterferenceSpecificationTypeEngCnxCheckNoClash to take into account
                |         engineering connection specifications of type "Check No
                |         Clash"
                |         catInterferenceSpecificationTypeEngCnxCheckContact to take into account
                |         engineering connection specifications of type "Check
                |         Contact"
                |         catInterferenceSpecificationTypeEngCnxCheckClearance to take into
                |         account engineering connection specifications of type "Check
                |         Clearance"
                |         catInterferenceSpecificationTypeEngCnxNoCheck to take into account
                |         engineering connection specifications of type
                |         "NoCheck"
                |         catInterferenceSpecificationTypeEngCnxCheckNone to not use engineering
                |         connection specification
                | 
                |     If the value catInterferenceSpecificationTypeEngCnxNoCheck is the only
                |     value used, standard specification must also be used.
                |     In this case, the value of CatInterferenceSpecificationType (see
                |     InterferenceSpecificationType ) must be:
                | 
                |         catInterferenceSpecificationTypeClash
                |         or catInterferenceSpecificationTypeClearance
                |         or catInterferenceSpecificationTypeClashWithoutContact
                | 
                | 
                |     Remove the catInterferenceSpecificationTypeEngCnxCheckNone value (see
                |     RemoveItfSpecificationTypeEngCnx ) activates the first four
                |     values.
                | 
                |     Add value catInterferenceSpecificationTypeEngCnxCheckNone means that no
                |     engineering connection specification will be used. In this case, as a
                |     specification (standard specification or engineering connection specification
                |     or knowledge rules specification) must always be active, one of the others
                |     specifications (standard specification or knowledge rules specification) has to
                |     be added before.
                | 
                |     By default, Interference Simulation is created with the type:
                |     catInterferenceSpecificationTypeEngCnxCheckNone
                | 
                |     Example:
                | 
                |            This example allows to take into account the engineering connection
                |            of type "Check No Clash" in the InterferenceSimulation iSimu
                |            .
                |            
                | 
                |            Dim ItfSpecTypeEngCnx As
                |            CatInterferenceSpecificationTypeEngCnx
                |            ItfSpecTypeEngCnx = catInterferenceSpecificationTypeEngCnxCheckNoClash
                |            iSimu.AddItfSpecificationTypeEngCnx 
                |            ItfSpecTypeEngCnx

        :param int i_type_eng_cnx:
        :return: None
        """
        return self.com_object.AddItfSpecificationTypeEngCnx(i_type_eng_cnx)

    def execute(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Execute()
                |     Executes the Simulation and compute the Interferences
                |     Results.
                |     Role: Execute the Simulation and compute the Interferences
                |     Results.
                |     see InterferenceResults
                | 
                |     Example:
                | 
                |            This example launches computation of the InterferenceSimulation
                |            iSimu .
                |            
                | 
                |            iSimu.Execute

        :return: None
        """
        return self.com_object.Execute()

    def get_group_objects(self, i_index: int, o_groups: InterferenceGroupObjects) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetGroupObjects(long iIndex,InterferenceGroupObjects
                | oGroups)
                |     Retrieves a Group
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the group to retrieve from the
                |             simulation.
                |             As a numerics, this index is the rank of the group in the
                |             simulation.
                |             The index of the first group is 1, and the index of the last
                |             occurrence is the number of groups (see GetNumberOfGroupObjects method).
                |             
                | 
                |     Returns:
                |         The retrieved group
                |     Example:
                | 
                |            This example gets the first group Group_1 of the
                |            InterferenceSimulation iSimu .
                |            
                | 
                |            Dim NbGroup As Integer
                |            Dim Group_1 As InterferenceGroupObjects
                |            NbGroup = iSimu.GetNumberOfGroupObjects
                |            If NbGroup > 0 Then
                |               iSimu.GetGroupObjects 1, Group_1
                |               ...
                |            End If

        :param int i_index:
        :param InterferenceGroupObjects o_groups:
        :return: None
        """
        return self.com_object.GetGroupObjects(i_index, o_groups.com_object)

    def get_number_of_group_objects(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfGroupObjects() As long
                |     Gets the number of groups from the simulation
                | 
                |     Returns:
                |         The number of groups
                |     Example:
                | 
                |            This example gets the number of groups NbGroup of the
                |            InterferenceSimulation iSimu .
                |            
                | 
                |            Dim NbGroup As Integer
                |            NbGroup = iSimu.GetNumberOfGroupObjects

        :return: int
        """
        return self.com_object.GetNumberOfGroupObjects()

    def get_rule_set_name(self, o_rule_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetRuleSetName(CATBSTR oRuleSetName)
                |     Gets name of the RuleSet containing the knowledge rules of computation of
                |     the interference simulation.
                |     An empty string returned means that no RuleSet is taken into
                |     account.
                | 
                |     Example:
                | 
                |            This example retrieves the name of the RuleSet used in the
                |            InterferenceSimulation iSimu .
                |            
                | 
                |            Dim RuleSetName  As String
                |            iSimu.GetRuleSetName  RuleSetName

        :param str o_rule_set_name:
        :return: None
        """
        return self.com_object.GetRuleSetName(o_rule_set_name)

    def is_active_compute_quantifier(self, i_quantifier_mode: int, o_is_active: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsActiveComputeQuantifier(CatInterferenceComputeQuantifier
                | iQuantifierMode,boolean oIsActive)
                |     Checks if the desired computation of a quantifier is
                |     active.
                | 
                |     Example:
                | 
                |            This example verifies if the computation of the quantifier of
                |            minimum distance is activated for the InterferenceSimulation iSimu
                |            .
                |            
                | 
                |            Dim InterferenceQuantifier As
                |            CatInterferenceComputeQuantifier
                |            InterferenceQuantifier = catInterferenceComputeQuantifierMinimumDistance
                |            Dim bool1 As Boolean
                |            iSimu.IsActiveComputeQuantifier  InterferenceQuantifier,
                |            bool1
                |            If bool1 = TRUE Then
                |               ...
                |            End If

        :param int i_quantifier_mode:
        :param bool o_is_active:
        :return: None
        """
        return self.com_object.IsActiveComputeQuantifier(i_quantifier_mode, o_is_active)

    def is_active_itf_specification_type_eng_cnx(self, i_type_eng_cnx: int, o_is_active: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsActiveItfSpecificationTypeEngCnx(CatInterferenceSpecificationTypeEngCnx
                | iTypeEngCnx,boolean oIsActive)
                |     Determines if one specific type of engineering connection specification is
                |     used.
                | 
                |     Example:
                | 
                |            This example verifies if the engineering connection of type "Check
                |            Contact" is taken into account in the InterferenceSimulation iSimu
                |            .
                |            
                | 
                |            Dim ItfSpecTypeEngCnx As
                |            CatInterferenceSpecificationTypeEngCnx
                |            Dim bool1 As Boolean
                |            ItfSpecTypeEngCnx = catInterferenceSpecificationTypeEngCnxCheckContact
                |            iSimu.IsActiveItfSpecificationTypeEngCnx  ItfSpecTypeEngCnx,
                |            bool1
                |            If bool1 = TRUE Then
                |               MsgBox " Engineering connection of type Check Contact: activated
                |               "
                |            End If

        :param int i_type_eng_cnx:
        :param bool o_is_active:
        :return: None
        """
        return self.com_object.IsActiveItfSpecificationTypeEngCnx(i_type_eng_cnx, o_is_active)

    def is_compute_quantifier_available(self, i_quantifier_mode: int, o_is_available: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub IsComputeQuantifierAvailable(CatInterferenceComputeQuantifier
                | iQuantifierMode,boolean oIsAvailable)
                |     Checks if the desired computation of a quantifier is
                |     available.
                |     Computation of vector of penetration has only effect when the result is a
                |     clash and is always available.
                |     Computation of minimum distance between parts has only effect when the
                |     result is a clearance. It is only available if one of the following
                |     specifications is active:
                | 
                |         standard computation with a computation of clearance (see parameter:
                |         catInterferenceSpecificationTypeClearance of CatInterferenceSpecificationType
                |         )
                |         engineering connections of type "Check Clearance" are taken into
                |         account (see parameter: catInterferenceSpecificationTypeEngCnxCheckClearance of
                |         CatInterferenceSpecificationTypeEngCnx )
                |         knowledges rules are taken into account (see method: PutRuleSetByName
                |         )
                | 
                | 
                |     Example:
                | 
                |            This example verifies if the computation of the quantifier of
                |            minimum distance is allowed for the InterferenceSimulation iSimu
                |            .
                |            
                | 
                |            Dim InterferenceQuantifier As
                |            CatInterferenceComputeQuantifier
                |            InterferenceQuantifier = catInterferenceComputeQuantifierMinimumDistance
                |            Dim bool1 As Boolean
                |            iSimu.IsComputeQuantifierAvailable  InterferenceQuantifier,
                |            bool1
                |            If bool1 = TRUE Then
                |               ...
                |            End If

        :param int i_quantifier_mode:
        :param bool o_is_available:
        :return: None
        """
        return self.com_object.IsComputeQuantifierAvailable(i_quantifier_mode, o_is_available)

    def put_rule_set_by_name(self, i_rule_set_name: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PutRuleSetByName(CATBSTR iRuleSetName)
                |     Adds a RuleSet containing the knowledge rules of computation to the
                |     interference simulation.
                |     In this case, knowledge rules specification will be taken into account
                |     during computation.
                |     Note that a Search will be launch to retrieve the RuleSet by its name. So,
                |     the name given as argument to this method must be specific enough so that the
                |     search result finds only one RuleSet.
                | 
                |     Example:
                | 
                |            This example sets the RuleSet beginning with the string "RuleSet_01"
                |            to the InterferenceSimulation iSimu .
                |            
                | 
                |            Dim RuleSetName  As String
                |            RuleSetName = "RuleSet_01*"
                |            iSimu.PutRuleSetByName  RuleSetName

        :param str i_rule_set_name:
        :return: None
        """
        return self.com_object.PutRuleSetByName(i_rule_set_name)

    def remove_compute_quantifier(self, i_quantifier_mode: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveComputeQuantifier(CatInterferenceComputeQuantifier
                | iQuantifierMode)
                |     Removes the computation of a quantifier.
                | 
                |     Example:
                | 
                |            This example removes the computation of the quantifier of minimum
                |            distance to the InterferenceSimulation iSimu .
                |            
                | 
                |            Dim InterferenceQuantifier As
                |            CatInterferenceComputeQuantifier
                |            InterferenceQuantifier = catInterferenceComputeQuantifierMinimumDistance
                |            iSimu.RemoveComputeQuantifier
                |            InterferenceQuantifier

        :param int i_quantifier_mode:
        :return: None
        """
        return self.com_object.RemoveComputeQuantifier(i_quantifier_mode)

    def remove_group_objects(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveGroupObjects(long iIndex)
                |     Removes a Group (if possible)
                |     This method removes a group only if this is possible depending of the value
                |     of the parameter CatInterferenceGroupComputationType2 .
                |     If the value of InterferenceGroupComputationType2 is:
                | 
                |         catInterferenceGroupComputationTypeAllAgainstAllInGroup : group can be removed if there is more than one group.
                |         catInterferenceGroupComputationTypeGroupAgainstGroup : group can be removed if there are more than two groups.
                |         catInterferenceGroupComputationTypeGroupAgainstContext : no group can be removed.
                |         catInterferenceGroupComputationTypeAllAgainstAllInContext : no group can be removed.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the group to remove from the
                |             simulation.
                |             As a numerics, this index is the rank of the group in the
                |             simulation.
                |             The index of the first group is 1, and the index of the last
                |             occurrence is the number of groups (see GetNumberOfGroupObjects
                |             method).
                | 
                |     Example:
                | 
                |            This example removes the last group of the InterferenceSimulation
                |            iSimu .
                |            We suppose that the InterferenceSimulation has a
                |            GroupComputationType2 equal to 
                |            catInterferenceGroupComputationTypeGroupAgainstGroup and that a new
                |            group has already been added.
                |            
                | 
                |            Dim NbGroup As Integer
                |            Dim Group_1 As InterferenceGroupObjects
                |            NbGroup = iSimu.GetNumberOfGroupObjects
                |            If NbGroup > 2 Then
                |               iSimu.RemoveGroupObjects NbGroup
                |               ...
                |            End If

        :param int i_index:
        :return: None
        """
        return self.com_object.RemoveGroupObjects(i_index)

    def remove_itf_specification_type_eng_cnx(self, i_type_eng_cnx: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveItfSpecificationTypeEngCnx(CatInterferenceSpecificationTypeEngCnx
                | iTypeEngCnx)
                |     Removes one type of engineering connection specification.
                |     Removes the value catInterferenceSpecificationTypeEngCnxCheckNone will take
                |     into account all the other values:
                | 
                |         catInterferenceSpecificationTypeEngCnxCheckNoClash
                |         catInterferenceSpecificationTypeEngCnxCheckContact
                |         catInterferenceSpecificationTypeEngCnxCheckClearance
                |         catInterferenceSpecificationTypeEngCnxNoCheck
                | 
                | 
                |     Example:
                | 
                |            This example removes the taken into account of the engineering
                |            connection of type "Check Clearance" in the InterferenceSimulation iSimu
                |            .
                |            
                | 
                |            Dim ItfSpecTypeEngCnx As
                |            CatInterferenceSpecificationTypeEngCnx
                |            ItfSpecTypeEngCnx = catInterferenceSpecificationTypeEngCnxCheckClearance
                |            iSimu.RemoveItfSpecificationTypeEngCnx 
                |            ItfSpecTypeEngCnx

        :param int i_type_eng_cnx:
        :return: None
        """
        return self.com_object.RemoveItfSpecificationTypeEngCnx(i_type_eng_cnx)

    def remove_rule_set(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveRuleSet()
                |     Removes the RuleSet of the interference simulation.
                |     In this case, knowledge rules specification will not be taken into account
                |     during computation.
                | 
                |     A specification (standard specification or engineering connection
                |     specification or knowledge rules specification) must always be
                |     active.
                |     So, before removing the taking account of the knowledge rules
                |     (RemoveRuleSet), one of the others specifications (standard specification or
                |     engineering connection specification) must be active.
                | 
                |     Example:
                | 
                |            This example removes the RuleSet used in the InterferenceSimulation
                |            iSimu .
                |
                |            iSimu.RemoveRuleSet

        :return: None
        """
        return self.com_object.RemoveRuleSet()

    def __repr__(self):
        return f'InterferenceSimulation(name="{ self.name }")'
