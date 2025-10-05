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


class SimFrequencyBasedDamping(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimFrequencyBasedDamping
                | 
                | Represents the Frequency Based Damping object.
                | 
                | Example:
                |     This example demonstrates how to retrieve the SimFrequencyBasedDamping
                |     object from a SimRandomVibrationStep. The same pattern applies to all supported
                |     steps.
                | 
                |      Dim MyRandomVibrationStep As SimRandomVibrationStep
                |      ...
                |      Dim MyFrequencyBasedDamping As SimFrequencyBasedDamping
                |      Set MyFrequencyBasedDamping = MyRandomVibrationStep.FrequencyBasedDamping
                |      
                | 
                | Example in Python:
                | 
                |      MyFrequencyBasedDamping = MyRandomVibrationStep.FrequencyBasedDamping
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def damping_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DampingType() As SimFrequencyBasedDampingDampingType
                |     Returns or sets the damping type.

        :return: SimFrequencyBasedDampingDampingType
        """

        return self.com_object.DampingType

    @damping_type.setter
    def damping_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.DampingType = value

    @property
    def modes_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ModesType() As SimFrequencyBasedDampingModesType
                |     Returns or sets the modes type.

        :return: SimFrequencyBasedDampingModesType
        """

        return self.com_object.ModesType

    @modes_type.setter
    def modes_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ModesType = value

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the table that determines the damping behavior.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimFrequencyBasedDampingTableColumn iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the table that determines the damping
                |     behavior.
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
        return f'SimFrequencyBasedDamping(name="{ self.name }")'
