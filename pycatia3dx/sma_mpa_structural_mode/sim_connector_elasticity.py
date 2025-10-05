"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_table import SimTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn
from pycatia3dx.system.any_object import AnyObject


class SimConnectorElasticity(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimConnectorElasticity
                | 
                | Represents the Connector Elasticity object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def direction(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Direction() As SimDof (Read Only)
                |     Returns the DOF on which the elasticity connector is defined.

        :return: int
        """

        return self.com_object.Direction

    @property
    def elasticity_order(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElasticityOrder() As
                | SimConnectorElasticityElasticityOrder
                |     Returns or sets the elasticity order.

        :return: int
        """

        return self.com_object.ElasticityOrder

    @elasticity_order.setter
    def elasticity_order(self, value: int):
        """
        :param int value:
        """

        self.com_object.ElasticityOrder = value

    @property
    def stiffness(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Stiffness() As double
                |     Returns or sets the stiffness. Quantity: FORCE, units: kg_s2

        :return: float
        """

        return self.com_object.Stiffness

    @stiffness.setter
    def stiffness(self, value: float):
        """
        :param float value:
        """

        self.com_object.Stiffness = value

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the table that determines the elasticity behavior.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimConnectorElasticityTableColumn iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the table that determines the elasticity
                |     behavior.
                | 
                |     Parameters:
                | 
                |         iTableColumnName
                |             [in] The table column name. 
                | 
                |     Returns:
                |         The table column. 

        :param int i_table_column_name:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetTableColumn(i_table_column_name))

    def __repr__(self):
        return f'SimConnectorElasticity(name="{ self.name }")'
