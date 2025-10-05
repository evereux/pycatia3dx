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


class SimEos(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimEOS
                | 
                | Represents the EOS object.
                | 
                | Example:
                |     Given a SimMaterialOptions object, you can create a SimEOS as
                |     following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyEOS As SimEOS
                |      Set MyEOS = MyMaterialOptions.Add("SimEOS")
                |      
                | 
                |     Given a SimMaterialOptions object, you can retrieve a SimEOS named "EOS.1"
                |     as following:
                | 
                |      Dim MyMaterialOptions As SimMaterialOptions
                |      ...
                |      Dim MyEOS As SimEOS
                |      Set MyEOS = MyMaterialOptions.Item("EOS.1")
                |      
                | 
                | Example in Python:
                |     Given a SimMaterialOptions object myMaterialOptions, you can create a
                |     SimEOS as following:
                | 
                |      ...
                |      myEOS = myMaterialOptions.Add("SimEOS")
                |      
                | 
                |     Given a SimMaterialOptions object myMaterialOptions, you can retrieve a
                |     SimEOS named "EOS.1" as following:
                | 
                |      ...
                |      myEOS = myMaterialOptions.Item("EOS.1")
                |      
                | 
                | See also:
                |     SimMaterialOptions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def compressible_flow_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property CompressibleFlowFlag() As boolean
                |     Returns or sets the flag that determines if flow is compressible or
                |     not.
                | 
                |     TRUE: Flow is compressible.
                | 
                |     FALSE: Flow is in-compressible.

        :return: bool
        """

        return self.com_object.CompressibleFlowFlag

    @compressible_flow_flag.setter
    def compressible_flow_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.CompressibleFlowFlag = value

    @property
    def eos_data(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EOSData() As CATSafeArrayVariant
                |     Get or set data of the material option of type Ideal Gas, JWL and US-Up.
                |     The list of parameters.
                | 
                |     For Ideal Gas Gas constant, Ambient pressure, if Compressible flag is
                |     off.
                | 
                |     For JWL Detonation wave speed, A, B, Omega, R1, R2, Detonation energy
                |     density, Pre-detonation bulk modulus
                | 
                |     For Us-Up C0, S, Gamma0

        :return: tuple
        """

        return self.com_object.EOSData

    @eos_data.setter
    def eos_data(self, value: tuple):
        """
        :param tuple value:
        """

        self.com_object.EOSData = value

    @property
    def eos_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property EOSType() As SimEOSEOSType
                |     EOS type.

        :return: int
        """

        return self.com_object.EOSType

    @eos_type.setter
    def eos_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.EOSType = value

    @property
    def material_table(self) -> SimMaterialTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MaterialTable() As SimMaterialTable (Read Only)
                |     Returns the material table.

        :return: SimMaterialTable
        """

        return SimMaterialTable(self.com_object.MaterialTable)

    def get_material_table_column(self, i_material_table_column: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetMaterialTableColumn(SimEOSMaterialTableColumn iMaterialTableColumn) As
                | SimTableColumn
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
        return f'SimEos(name="{ self.name }")'
