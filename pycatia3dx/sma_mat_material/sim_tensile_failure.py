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


class SimTensileFailure(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimTensileFailure
                | 
                | Represents the Tensile Failure object.
                | 
                | Example:
                |     Given a SimMaterialOption object of parent material option, you can create
                |     a SimTensileFailure suboption as following:
                | 
                |      Dim MyParentOption As SimMaterialOption
                |      ...
                |      Dim MyTensileFailure As SimTensileFailure
                |      Set MyTensileFailure = MyParentOption.CreateSubOption("SimTensileFailure")
                |      
                | 
                |     Given a SimMaterialOption object of parent material option, you can
                |     retrieve a SimTensileFailure suboption at index i as
                |     following:
                | 
                |      Dim MyParentOption As SimMaterialOption
                |      ...
                |      Dim SubOptions
                |      SubOptions = MyParentOption.GetSubOptions()
                |      Dim MyTensileFailure As SimTensileFailure
                |      Set MyTensileFailure = SubOptions(i)
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOption object MyParentOption of parent material option,
                |     you can create a SimTensileFailure suboption as following:
                | 
                |      ...
                |      MyTensileFailure = MyParentOption.CreateSubOption("SimTensileFailure")
                |      
                | 
                |     Given a SimMaterialOption object MyParentOption of parent material option,
                |     you can retrieve a SimTensileFailure suboption at index i as
                |     following:
                | 
                |      ...
                |      SubOptions = MyParentOption.GetSubOptions()
                |      MyTensileFailure = SubOptions[i]
                |      
                | 
                | See also:
                |     SimMaterialOption
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def deviatoric_stress_status(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DeviatoricStressStatus() As SimTensileFailureCriteria
                |     Retrieves or sets failure criteria for deviatoric stress.
                | 
                |     Parameters:
                | 
                |         oStatus[out]
                |             The failure criteria. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: int
        """

        return self.com_object.DeviatoricStressStatus

    @deviatoric_stress_status.setter
    def deviatoric_stress_status(self, value: int):
        """
        :param int value:
        """

        self.com_object.DeviatoricStressStatus = value

    @property
    def element_removal_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ElementRemovalFlag() As boolean
                |     Retrieves or sets the element removal flag.
                |     TRUE : Allow element removal when the failure criterion is met.
                |     FALSE : Allow Brittle/Ductile type failure for the deviatoric and hydrostatic parts of stresses.
                | 
                |     Returns:
                |         S_OK if successful.

        :return: bool
        """

        return self.com_object.ElementRemovalFlag

    @element_removal_flag.setter
    def element_removal_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ElementRemovalFlag = value

    @property
    def hydro_stress_status(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property HydroStressStatus() As SimTensileFailureCriteria
                |     Retrieves or sets failure criteria for hydrostatic stress.
                | 
                |     Parameters:
                | 
                |         oStatus[out]
                |             The failure criteria. 
                | 
                |     Returns:
                |         S_OK if successful.

        :return: int
        """

        return self.com_object.HydroStressStatus

    @hydro_stress_status.setter
    def hydro_stress_status(self, value: int):
        """
        :param int value:
        """

        self.com_object.HydroStressStatus = value

    @property
    def material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialTable() As SimMaterialTable (Read Only)
                |     Returns the Tensile Failure material table data.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTable)

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimTensileFailureMaterialTableColumn
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
        return f'SimTensileFailure(name="{ self.name }")'
