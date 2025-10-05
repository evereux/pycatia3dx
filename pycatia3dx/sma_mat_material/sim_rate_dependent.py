"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_mat_material.sim_material_table import SimMaterialTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn


class SimRateDependent(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimRateDependent
                | 
                | Represents the Rate Dependent object.
                | 
                | Example:
                |     Given a SimMaterialOption object of parent material option, you can create
                |     a SimRateDependent suboption as following:
                | 
                |      Dim MyParentOption As SimMaterialOption
                |      ...
                |      Dim MyRateDependent As SimRateDependent
                |      Set MyRateDependent = MyParentOption.CreateSubOption("SimRateDependent")
                |      
                | 
                |     Given a SimMaterialOption object of parent material option, you can
                |     retrieve a SimRateDependent suboption at index i as
                |     following:
                | 
                |      Dim MyParentOption As SimMaterialOption
                |      ...
                |      Dim SubOptions
                |      SubOptions = MyParentOption.GetSubOptions()
                |      Dim MyRateDependent As SimRateDependent
                |      Set MyRateDependent = SubOptions(i)
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOption object MyParentOption of parent material option,
                |     you can create a SimRateDependent suboption as following:
                | 
                |      ...
                |      MyRateDependent = MyParentOption.CreateSubOption("SimRateDependent")
                |      
                | 
                |     Given a SimMaterialOption object MyParentOption of parent material option,
                |     you can retrieve a SimRateDependent suboption at index i as
                |     following:
                | 
                |      ...
                |      SubOptions = MyParentOption.GetSubOptions()
                |      MyRateDependent = SubOptions[i]
                |      
                | 
                | See also:
                |     SimMaterialOption
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def hardening_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HardeningType() As SimRateDependentHardeningType
                |     Retrieves or sets the hardening type of the material
                |     option.
                | 
                |     Returns:
                |         S_OK if successful.

        :return: int
        """

        return self.com_object.HardeningType

    @hardening_type.setter
    def hardening_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.HardeningType = value

    @property
    def johnson_cook_c(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JohnsonCookC() As double
                |     Retrieves or sets the Johnson-Cook parameter C.
                | 
                |     Returns:
                |         S_OK if successful.

        :return: float
        """

        return self.com_object.JohnsonCookC

    @johnson_cook_c.setter
    def johnson_cook_c(self, value: float):
        """
        :param float value:
        """

        self.com_object.JohnsonCookC = value

    @property
    def johnson_cook_epsilon(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property JohnsonCookEpsilon() As double
                |     Retrieves or sets the Johnson-Cook parameter Epsilon.
                | 
                |     Returns:
                |         S_OK if successful.

        :return: float
        """

        return self.com_object.JohnsonCookEpsilon

    @johnson_cook_epsilon.setter
    def johnson_cook_epsilon(self, value: float):
        """
        :param float value:
        """

        self.com_object.JohnsonCookEpsilon = value

    @property
    def material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialTable() As SimMaterialTable (Read Only)
                |     Returns the Rate Dependent material table data.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTable)

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimRateDependentMaterialTableColumn
                | iMaterialTableColumn) As SimTableColumn
                |     Retrieves the column object for the specified table
                |     column.
                | 
                |     Parameters:
                | 
                |         iMaterialTableColumn[in]
                |             The specified table column. 
                | 
                |     Returns:
                |         The table column object. This value will be NULL_var in case the
                |         specified column is not found in the table. 

        :param int i_material_table_column:
        :return: SimTableColumn
        """
        return SimTableColumn(self.com_object.GetMaterialTableColumn(i_material_table_column))

    def __repr__(self):
        return f'SimRateDependent(name="{ self.name }")'
