"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem
from pycatia3dx.sma_mpa_base.sim_table import SimTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn


class SimMappedFieldData(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimMappedFieldData
                | 
                | Represents the Mapped Field Data object.
    
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
                |     Returns the axis system.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def boundary_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property BoundaryTolerance() As double
                |     Returns or sets the boundary tolerance. If tolerance type is set to
                |     Relative: Quantity: Real, units: none If tolerance type is set to Absolute:
                |     Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.BoundaryTolerance

    @boundary_tolerance.setter
    def boundary_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.BoundaryTolerance = value

    @property
    def data_source_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DataSourceType() As SimMappedFieldDataDataSourceType
                |     Returns or sets the data source type.

        :return: int
        """

        return self.com_object.DataSourceType

    @data_source_type.setter
    def data_source_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DataSourceType = value

    @property
    def negative_normal_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NegativeNormalDistance() As double
                |     Returns or sets the negative normal distance. If tolerance type is set to
                |     Relative: Quantity: Real, units: none If tolerance type is set to Absolute:
                |     Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.NegativeNormalDistance

    @negative_normal_distance.setter
    def negative_normal_distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.NegativeNormalDistance = value

    @property
    def neighborhood_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property NeighborhoodTolerance() As double
                |     Returns or sets the neighborhood tolerance. If tolerance type is set to
                |     Relative: Quantity: Real, units: none If tolerance type is set to Absolute:
                |     Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.NeighborhoodTolerance

    @neighborhood_tolerance.setter
    def neighborhood_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.NeighborhoodTolerance = value

    @property
    def positive_normal_distance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositiveNormalDistance() As double
                |     Returns or sets the positive normal distance. If tolerance type is set to
                |     Relative: Quantity: Real, units: none If tolerance type is set to Absolute:
                |     Quantity: LENGTH, units: m

        :return: float
        """

        return self.com_object.PositiveNormalDistance

    @positive_normal_distance.setter
    def positive_normal_distance(self, value: float):
        """
        :param float value:
        """

        self.com_object.PositiveNormalDistance = value

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the field data table.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    @property
    def tolerance_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ToleranceType() As SimMappedFieldDataToleranceType
                |     Returns or sets the tolerance type.

        :return: int
        """

        return self.com_object.ToleranceType

    @tolerance_type.setter
    def tolerance_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ToleranceType = value

    @property
    def unmapped_value(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property UnmappedValue() As double
                |     Returns or sets the field value outside the mapped region.

        :return: float
        """

        return self.com_object.UnmappedValue

    @unmapped_value.setter
    def unmapped_value(self, value: float):
        """
        :param float value:
        """

        self.com_object.UnmappedValue = value

    @property
    def vpm_document(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property VPMDocument() As CATBaseDispatch
                |     Returns or sets the VPM document.

        :return: AnyObject
        """

        return AnyObject(self.com_object.VPMDocument)

    @vpm_document.setter
    def vpm_document(self, value: AnyObject):
        """
        :param AnyObject value:
        """

        self.com_object.VPMDocument = value

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimMappedFieldDataTableColumn iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the field data table. Only applicable when
                |     the Data Source Type is set to Table.
                | 
                |     Parameters:
                | 
                |         iTableColumnName[in]
                |             The table column name. 
                | 
                |     Returns:
                |         The table column. 

        :param int i_table_column_name:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetTableColumn(i_table_column_name))

    def __repr__(self):
        return f'SimMappedFieldData(name="{ self.name }")'
