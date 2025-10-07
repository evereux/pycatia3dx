"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_structural_mode.sim_beam_section import SimBeamSection
from pycatia3dx.sma_mpa_structural_mode.sim_connector_section import SimConnectorSection
from pycatia3dx.sma_mpa_structural_mode.sim_point_fastener_placement import SimPointFastenerPlacement


class SimPointFastener(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPointFastener
                | 
                | Represents the Point Fastener object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimPointFastener as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyPointFastener As SimPointFastener
                |      Set MyPointFastener = MyMCXProperties.Add("SimPointFastener")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimPointFastener named
                |     "Point Fastener.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyPointFastener As SimPointFastener
                |      Set MyPointFastener = MyMCXProperties.Item("Point Fastener.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimPointFastener as following:
                | 
                |      ...
                |      myPointFastener = myMCXProperties.Add("SimPointFastener")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimPointFastener named "Point Fastener.1" as following:
                | 
                |      ...
                |      myPointFastener = myMCXProperties.Item("Point Fastener.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def adjust_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdjustTolerance() As double
                |     This parameter is used to move the spot locations if the projection at a
                |     spot fails. Quantity: LENGTH, units: m.

        :return: float
        """

        return self.com_object.AdjustTolerance

    @adjust_tolerance.setter
    def adjust_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.AdjustTolerance = value

    @property
    def beam_section(self) -> SimBeamSection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BeamSection() As SimBeamSection (Read Only)
                |     Returns the connector beam section.

        :return: SimBeamSection
        """

        return SimBeamSection(self.com_object.BeamSection)

    @property
    def connector_section(self) -> SimConnectorSection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConnectorSection() As SimConnectorSection (Read Only)
                |     Returns the connector section.

        :return: SimConnectorSection
        """

        return SimConnectorSection(self.com_object.ConnectorSection)

    @property
    def construct_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConstructType() As SimPointFastenerConstructType
                |     Returns or sets the construct type.

        :return: int
        """

        return self.com_object.ConstructType

    @construct_type.setter
    def construct_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ConstructType = value

    @property
    def coupling_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CouplingType() As SimCouplingCouplingType
                |     Returns or sets the coupling type.

        :return: int
        """

        return self.com_object.CouplingType

    @coupling_type.setter
    def coupling_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.CouplingType = value

    @property
    def fastener_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FastenerDiameter() As double
                |     * The influence diameter for points on the supports for all constructs
                |     other than the SolidHex. Quantity: LENGTH, units: m. The diagonal size of the
                |     single hexahedral element for SolidHex construct. Quantity: LENGTH, units: m.

        :return: float
        """

        return self.com_object.FastenerDiameter

    @fastener_diameter.setter
    def fastener_diameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.FastenerDiameter = value

    @property
    def height(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Height() As double
                |     This parameter is used to fill the gap between connecting faces. Quantity:
                |     LENGTH, units: m.

        :return: float
        """

        return self.com_object.Height

    @height.setter
    def height(self, value: float):
        """
        :param float value:
        """

        self.com_object.Height = value

    @property
    def maximum_adjacent_face_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumAdjacentFaceAngle() As double
                |     This parameter is used to specify the maximum angle before a face will be
                |     excluded from the coupling surface. Quantity: ANGLE, units: degrees

        :return: float
        """

        return self.com_object.MaximumAdjacentFaceAngle

    @maximum_adjacent_face_angle.setter
    def maximum_adjacent_face_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumAdjacentFaceAngle = value

    @property
    def maximum_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumAngle() As double
                |     Maximum angle between a fastener and the face normal of the connected face.
                |     Quantity: ANGLE, units: Degrees.

        :return: float
        """

        return self.com_object.MaximumAngle

    @maximum_angle.setter
    def maximum_angle(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumAngle = value

    @property
    def maximum_projection_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumProjectionDistance() As double
                |     Distance between the fastener placement points\\lines and the farthest
                |     connected face. The faces at distance more than this limit will not be
                |     considered for a fastener. Quantity: LENGTH, units: m.

        :return: float
        """

        return self.com_object.MaximumProjectionDistance

    @maximum_projection_distance.setter
    def maximum_projection_distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.MaximumProjectionDistance = value

    @property
    def point_fastener_placement(self) -> SimPointFastenerPlacement:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointFastenerPlacement() As SimPointFastenerPlacement (Read
                | Only)
                |     Returns the points table.

        :return: SimPointFastenerPlacement
        """

        return SimPointFastenerPlacement(self.com_object.PointFastenerPlacement)

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
    def spring_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpringType() As SimSpringType
                |     Returns or sets the type of the SMAMpaSpringType. 

        :return: int
        """

        return self.com_object.SpringType

    @spring_type.setter
    def spring_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.SpringType = value

    def __repr__(self):
        return f'SimPointFastener(name="{ self.name }")'
