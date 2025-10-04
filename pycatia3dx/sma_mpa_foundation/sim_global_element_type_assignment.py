"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimGlobalElementTypeAssignment(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimGlobalElementTypeAssignment
                | 
                | Represents the Global Element Type Assignment object.
                | 
                | Example:
                |     This example demonstrates how to retrieve the
                |     SimGlobalElementTypeAssignment object from a SimAnalysisCase, retrieve the
                |     family, topologies, formulation, default and candidate
                |     formulations.
                | 
                |      Dim MyAnalysisCase As SimAnalysisCase
                |      ...
                |      Dim MyGlobalAssignment As SimGlobalElementTypeAssignment
                |      Set MyGlobalAssignment = MyAnalysisCase.GlobalElementTypeAssignment
                |      Dim MyFamily As String
                |      MyFamily = MyGlobalAssignment.Family
                |      Dim MyElementTopology As String
                |      MyElementTopology = MyGlobalAssignment.Topologies(1)
                |      Dim MyElementFormulation As String
                |      MyElementFormulation = MyGlobalAssignment.GetFormulation(MyElementTopology)
                |      Dim MyDefaultFormulation As String
                |      MyDefaultFormulation = MyGlobalAssignment.DefaultFormulation(MyElementTopology)
                |      Dim MyCandidates As Variant
                |      MyCandidates = MyGlobalAssignment.CandidateFormulations(MyElementTopology)
                |      
                | 
                | Example in Python:
                | 
                |      MyGlobalAssignment = MyAnalysisCase.GlobalElementTypeAssignment
                |      MyFamily = MyGlobalAssignment.Family
                |      MyElementTopology = MyGlobalAssignment.Topologies(1)
                |      MyElementFormulation = MyGlobalAssignment.GetFormulation(MyElementTopology)
                |      MyDefaultFormulation = MyGlobalAssignment.DefaultFormulation(MyElementTopology)
                |      MyCandidates = MyGlobalAssignment.CandidateFormulations(MyElementTopology)
                |      
                | 
                | See also:
                |     SimAnalysisCase
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def family(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Family() As CATBSTR
                |     Returns or sets the family of elements formulations. Valid
                |     values:
                | 
                |         Standard-3D-Stress/Displacement
                |         Standard-3D-Thermal
                |         Standard-3D-Piezoelectric
                |         Standard-3D-Thermal/Displacement
                |         Standard-3D-Thermal/Displacement/Electric
                |         Standard-3D-Thermal/Electric
                |         Standard-3D-Thermal/Electric/Electrochemical
                |        
Standard-3D-Thermal/Displacement/Electric/Electrochemical                |        
Standard-3D-Thermal/Displacement/Electric/Electrochemical/Pore                |         Standard-Axisymmetric-Stress/Displacement
                |         Standard-Axisymmetric-Thermal
                |         Standard-Axisymmetric-Piezoelectric
                |         Standard-Axisymmetric-Thermal/Displacement
                |         Standard-Axisymmetric-Thermal/Displacement/Electric
                |         Standard-Axisymmetric-Thermal/Electric
                |         Explicit-3D-Stress/Displacement
                |         Explicit-3D-Thermal/Displacement
                |         Explicit-Axisymmetric-Stress/Displacement
                |         Explicit-Axisymmetric-Thermal/Displacement
                | 
                |     Setting an invalid family will return an error.

        :return: str
        """

        return self.com_object.Family

    @family.setter
    def family(self, value: str):
        """
        :param str value:
        """

        self.com_object.Family = value

    @property
    def topologies(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Topologies() As CATSafeArrayVariant (Read Only)
                |     Returns the section and topology pairs in the model. Element topologies
                |     are:
                | 
                |         BAR - Linear bar element for trusses/beams
                |         BAR3 - Parabolic bar element for trusses/beams
                |         TR3 - Linear triangular element for shells
                |         TR6 - Parabolic triangular element for shells
                |         QD4 - Linear quadrilateral element for shells
                |         QD8 - Parabolic quadrilateral element for shells
                |         TE4 - Linear tetrahedral element for solids
                |         TE10 - Parabolic tetrahedral element for solids
                |         HE8 - Linear hexahedral element for solids
                |         HE20 - Parabolic hexahedral element for solids
                |         WE6 - Linear prismatic wedge element for solids
                |         WE15 - Parabolic prismatic wedge element for solids
                |         PY5 - Linear pyramid element for solids

        :return: tuple
        """

        return self.com_object.Topologies

    def candidate_formulations(self, i_topology: str) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func CandidateFormulations(CATBSTR iTopology) As
                | CATSafeArrayVariant
                |     Returns the candidate element formulations for the argument topology.

        :param str i_topology:
        :return: tuple
        """
        return self.com_object.CandidateFormulations(i_topology)

    def default_formulation(self, i_topology: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func DefaultFormulation(CATBSTR iTopology) As CATBSTR
                |     Returns the default solver element formulation for the argument topology.

        :param str i_topology:
        :return: str
        """
        return self.com_object.DefaultFormulation(i_topology)

    def get_formulation(self, i_topology: str) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetFormulation(CATBSTR iTopology) As CATBSTR
                |     Returns the solver element formulation for the argument topology.

        :param str i_topology:
        :return: str
        """
        return self.com_object.GetFormulation(i_topology)

    def set_formulation(self, i_topology: str, i_formulation: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetFormulation(CATBSTR iTopology,CATBSTR iFormulation)
                |     Sets the solver element formulation for the argument topology.

        :param str i_topology:
        :param str i_formulation:
        :return: None
        """
        return self.com_object.SetFormulation(i_topology, i_formulation)

    def __repr__(self):
        return f'SimGlobalElementTypeAssignment(name="{ self.name }")'
