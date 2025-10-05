"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.application import Application
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.cat_base_dispatch import CATBaseDispatch


class SimPointFastenerPlacement(CATBaseDispatch):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 SimPointFastenerPlacement
                | 
                | Represents the Point Fastener Placement object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def application(self) -> Application:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Application() As Application (Read Only)

        :return: Application
        """

        return Application(self.com_object.Application)

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
    def clearance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Clearance() As double
                |     Returns or sets the clearance. Quantity: LENGTH, units: m.

        :return: float
        """

        return self.com_object.Clearance

    @clearance.setter
    def clearance(self, value: float):
        """
        :param float value:
        """

        self.com_object.Clearance = value

    @property
    def distribution_option_on_lines(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DistributionOptionOnLines() As
                | SimPointFastenerPlacementDistributionOptionOnLine
                |     Returns or sets the distribution option.

        :return: int
        """

        return self.com_object.DistributionOptionOnLines

    @distribution_option_on_lines.setter
    def distribution_option_on_lines(self, value: int):
        """
        :param int value:
        """

        self.com_object.DistributionOptionOnLines = value

    @property
    def fastener_placement_method(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FastenerPlacementMethod() As
                | SimPointFastenerPlacementFastenerPlacementMethod
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
    def name(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Name() As CATBSTR

        :return: str
        """

        return self.com_object.Name

    @name.setter
    def name(self, value: str):
        """
        :param str value:
        """

        self.com_object.Name = value

    @property
    def number_of_fasteners_along_lines(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NumberOfFastenersAlongLines() As long
                |     Returns or sets the number of fasteners.

        :return: int
        """

        return self.com_object.NumberOfFastenersAlongLines

    @number_of_fasteners_along_lines.setter
    def number_of_fasteners_along_lines(self, value: int):
        """
        :param int value:
        """

        self.com_object.NumberOfFastenersAlongLines = value

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
    def parent(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Parent() As CATBaseDispatch (Read Only)

        :return: AnyObject
        """

        return AnyObject(self.com_object.Parent)

    @property
    def point_spacing_along_lines(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PointSpacingAlongLines() As double
                |     Returns or sets the spacing between points on line. Quantity: LENGTH,
                |     units: m.

        :return: float
        """

        return self.com_object.PointSpacingAlongLines

    @point_spacing_along_lines.setter
    def point_spacing_along_lines(self, value: float):
        """
        :param float value:
        """

        self.com_object.PointSpacingAlongLines = value

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

    def get_item(self, id_name: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetItem(CATBSTR IDName) As CATBaseDispatch

        :param str id_name:
        :return: AnyObject
        """
        return self.com_object.GetItem(id_name)

    def __repr__(self):
        return f'SimPointFastenerPlacement(name="{ self.name }")'
