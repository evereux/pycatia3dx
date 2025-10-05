"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimMassPerArea(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMassPerArea
                | 
                | Represents the Mass Per Area object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimMassPerArea as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyMassPerArea As SimMassPerArea
                |      Set MyMassPerArea = MyAbstractions.Add("SimMassPerArea")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimMassPerArea named
                |     "Mass Per Area.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyMassPerArea As SimMassPerArea
                |      Set MyMassPerArea = MyAbstractions.Item("Mass Per Area.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimMassPerArea as following:
                | 
                |      ...
                |      myMassPerArea = myAbstractions.Add("SimMassPerArea")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimMassPerArea named "Mass Per Area.1" as following:
                | 
                |      ...
                |      myMassPerArea = myAbstractions.Item("Mass Per Area.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def contribution_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ContributionType() As
                | SimNonstructuralMassApplicationMethod
                |     Returns or sets the nonstructural mass contribution type.

        :return: int
        """

        return self.com_object.ContributionType

    @contribution_type.setter
    def contribution_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ContributionType = value

    @property
    def magnitude(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Magnitude() As double
                |     Returns or sets the mass magnitude used for the nonstructural
                |     mass.
                |     If the contribution type is TotalMass then the unit is : Quantity: MASS, units: Kg.
                |     Else the unit depends of the feature's type :
                | 
                |         MassPerVolume : Quantity: DENSITY, units: Kg_m3
                |         MassPerArea : Quantity: SURFACICMASS, units: Kg_m2
                |         MassPerLength : Quantity: LINEMASS, units: Kg_m

        :return: float
        """

        return self.com_object.Magnitude

    @magnitude.setter
    def magnitude(self, value: float):
        """
        :param float value:
        """

        self.com_object.Magnitude = value

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

    @property
    def total_mass_distribution_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TotalMassDistributionMethod() As
                | SimNonstructuralMassTotalMassDistributionMethod
                |     Returns or sets the mass distribution used for the selected type of
                |     nonstructural mass. 

        :return: int
        """

        return self.com_object.TotalMassDistributionMethod

    @total_mass_distribution_method.setter
    def total_mass_distribution_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.TotalMassDistributionMethod = value

    def __repr__(self):
        return f'SimMassPerArea(name="{ self.name }")'
