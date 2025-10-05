"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_base.sim_table import SimTable
from pycatia3dx.sma_mpa_base.sim_table_column import SimTableColumn
from pycatia3dx.sma_mpa_foundation.sim_linear_load_cases import SimLinearLoadCases
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep


class SimHarmonicResponseStep(SimStep):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SMAMpaFoundationIDLItf.SimStep
                |                         SimHarmonicResponseStep
                | 
                | Represents the Harmonic Response Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimHarmonicResponseStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyHarmonicResponseStep As SimHarmonicResponseStep
                |      Set MyHarmonicResponseStep = MySteps.Add("SimHarmonicResponseStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimHarmonicResponseStep named
                |     "Harmonic Response Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyHarmonicResponseStep As SimHarmonicResponseStep
                |      Set MyHarmonicResponseStep = MySteps.Item("Harmonic Response Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimHarmonicResponseStep
                |     as following:
                | 
                |      ...
                |      myHarmonicResponseStep = mySteps.Add("SimHarmonicResponseStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimHarmonicResponseStep
                |     named "Harmonic Response Step.1" as following:
                | 
                |      ...
                |      myHarmonicResponseStep = mySteps.Item("Harmonic Response Step.1")
                |      
                | 
                | See also:
                |     SimSteps
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def activated(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Activated() As boolean
                |     Returns or sets the activation status.

        :return: bool
        """

        return self.com_object.Activated

    @activated.setter
    def activated(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Activated = value

    @property
    def interval_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property IntervalType() As SimHarmonicResponseStepIntervalType
                |     Returns or sets the interval type.

        :return: SimHarmonicResponseStepIntervalType
        """

        return self.com_object.IntervalType

    @interval_type.setter
    def interval_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.IntervalType = value

    @property
    def linear_load_cases(self) -> SimLinearLoadCases:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LinearLoadCases() As SimLinearLoadCases (Read Only)
                |     Returns the list of all linear load cases.

        :return: SimLinearLoadCases
        """

        return SimLinearLoadCases(self.com_object.LinearLoadCases)

    @property
    def projection_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ProjectionType() As
                | SimHarmonicResponseStepProjectionType
                |     Returns or sets the projection type.

        :return: SimHarmonicResponseStepProjectionType
        """

        return self.com_object.ProjectionType

    @projection_type.setter
    def projection_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ProjectionType = value

    @property
    def scale(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Scale() As SimHarmonicResponseStepScaleType
                |     Deprecated R425 Use ScaleType property.

        :return: SimHarmonicResponseStepScaleType
        """

        return self.com_object.Scale

    @scale.setter
    def scale(self, value: int):
        """
        :param int value:
        """

        self.com_object.Scale = value

    @property
    def scale_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ScaleType() As SimHarmonicResponseStepScaleType
                |     Returns or sets the scale type.

        :return: SimHarmonicResponseStepScaleType
        """

        return self.com_object.ScaleType

    @scale_type.setter
    def scale_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.ScaleType = value

    @property
    def structural_material_damping_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StructuralMaterialDampingFlag() As boolean
                |     Returns or sets the flag that determines if the structural material damping
                |     option is used.
                |     TRUE : the structural material damping option is used.
                |     FALSE : the structural material damping option is not used.

        :return: bool
        """

        return self.com_object.StructuralMaterialDampingFlag

    @structural_material_damping_flag.setter
    def structural_material_damping_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.StructuralMaterialDampingFlag = value

    @property
    def table(self) -> SimTable:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Table() As SimTable (Read Only)
                |     Returns the table that determines the hamornic response step behavior.

        :return: SimTable
        """

        return SimTable(self.com_object.Table)

    @property
    def viscous_material_damping_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ViscousMaterialDampingFlag() As boolean
                |     Returns or sets the flag that determines if the viscous material damping
                |     option is used.
                |     TRUE : the viscous material damping option is used.
                |     FALSE : the viscous material damping option is not used.

        :return: bool
        """

        return self.com_object.ViscousMaterialDampingFlag

    @viscous_material_damping_flag.setter
    def viscous_material_damping_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ViscousMaterialDampingFlag = value

    def get_table_column(self, i_table_column_name: int) -> SimTableColumn:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTableColumn(SimHarmonicResponseStepTableColumn iTableColumnName) As
                | SimTableColumn
                |     Retrieves a specific column of the table that determines the hamornic
                |     response step behavior.
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
        return f'SimHarmonicResponseStep(name="{ self.name }")'
