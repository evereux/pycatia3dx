"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject


class SimLineFastener(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimLineFastener
                | 
                | Represents the Line Fastener object.
                | 
                | Example:
                |     Given a SimMCXProperties object, you can create a SimLineFastener as
                |     following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyLineFastener As SimLineFastener
                |      Set MyLineFastener = MyMCXProperties.Add("SimLineFastener")
                |      
                | 
                |     Given a SimMCXProperties object, you can retrieve a SimLineFastener named
                |     "Line Fastener.1" as following:
                | 
                |      Dim MyMCXProperties As SimMCXProperties
                |      ...
                |      Dim MyLineFastener As SimLineFastener
                |      Set MyLineFastener = MyMCXProperties.Item("Line Fastener.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMCXProperties object myMCXProperties, you can create a
                |     SimLineFastener as following:
                | 
                |      ...
                |      myLineFastener = myMCXProperties.Add("SimLineFastener")
                |      
                | 
                |     Given a SimMCXProperties object myMCXProperties, you can retrieve a
                |     SimLineFastener named "Line Fastener.1" as following:
                | 
                |      ...
                |      myLineFastener = myMCXProperties.Item("Line Fastener.1")
                |      
                | 
                | See also:
                |     SimMCXProperties
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def axis_system(self) -> SimAxisSystem:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AxisSystem() As SimAxisSystem (Read Only)
                |     Returns the axis system used for point coordinates.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def construct_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ConstructType() As SimLineFastenerConstructType
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
    def fastener_placement_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FastenerPlacementMethod() As
                | SimLineFastenerPlacementFastenerPlacementMethod
                |     Returns or sets the fastener placement method.

        :return: int
        """

        return self.com_object.FastenerPlacementMethod

    @fastener_placement_method.setter
    def fastener_placement_method(self, value: int):
        """
        :param int value:
        """

        self.com_object.FastenerPlacementMethod = value

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
    def maximum_angle(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaximumAngle() As double
                |     Maximum angle between the fastener and the face normal of the connected
                |     face. Quantity: ANGLE, units: Degrees.

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
                |     Distance between the fastener placement points\lines and the farthest
                |     connected face. The faces at distance more than this limit will not be
                |     considered for the fastener. Quantity: LENGTH, units: m.

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
    def mesh_compatibility(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MeshCompatibility() As
                | SimLineFastenerMeshCompatibility
                |     Returns or sets the mesh compatibility type.

        :return: int
        """

        return self.com_object.MeshCompatibility

    @mesh_compatibility.setter
    def mesh_compatibility(self, value: int):
        """
        :param int value:
        """

        self.com_object.MeshCompatibility = value

    @property
    def number_of_point_coordinates(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfPointCoordinates() As long
                |     Returns or sets the number of points through coordinates.

        :return: int
        """

        return self.com_object.NumberOfPointCoordinates

    @number_of_point_coordinates.setter
    def number_of_point_coordinates(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfPointCoordinates = value

    @property
    def points_coordinates(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointsCoordinates() As CATSafeArrayVariant
                |     Returns or sets a list of points coordinate (x1, y1, z1, x2, y2, z2, ...).

        :return: tuple
        """

        return self.com_object.PointsCoordinates

    @points_coordinates.setter
    def points_coordinates(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.PointsCoordinates = value

    @property
    def spacing(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Spacing() As double
                |     This parameter specifies the distance between connector mesh elements along
                |     placement. Quantity: LENGTH, units: m.

        :return: float
        """

        return self.com_object.Spacing

    @spacing.setter
    def spacing(self, value: float):
        """
        :param float value:
        """

        self.com_object.Spacing = value

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
    def width(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Width() As double
                |     Thickness of the single shell element for Shell construct. Quantity:
                |     LENGTH, units: m. The diagonal size of the single hexahedral element for
                |     SolidHex construct. Quantity: LENGTH, units: m. 

        :return: float
        """

        return self.com_object.Width

    @width.setter
    def width(self, value: float):
        """
        :param float value:
        """

        self.com_object.Width = value

    def __repr__(self):
        return f'SimLineFastener(name="{ self.name }")'
