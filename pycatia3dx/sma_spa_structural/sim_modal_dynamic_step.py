"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_mpa_foundation.sim_step import SimStep


class SimModalDynamicStep(SimStep):

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
                |                         SimModalDynamicStep
                | 
                | Represents the Modal Dynamic Step object.
                | 
                | Example:
                |     Given a SimSteps object, you can create a SimModalDynamicStep as
                |     following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyModalDynamicStep As SimModalDynamicStep
                |      Set MyModalDynamicStep = MySteps.Add("SimModalDynamicStep")
                |      
                | 
                |     Given a SimSteps object, you can retrieve a SimModalDynamicStep named
                |     "Modal Dynamic Step.1" as following:
                | 
                |      Dim MySteps As SimSteps
                |      ...
                |      Dim MyModalDynamicStep As SimModalDynamicStep
                |      Set MyModalDynamicStep = MySteps.Item("Modal Dynamic Step.1")
                |      
                | 
                | Example in Python:
                |     Given a SimSteps object mySteps, you can create a SimModalDynamicStep as
                |     following:
                | 
                |      ...
                |      myModalDynamicStep = mySteps.Add("SimModalDynamicStep")
                |      
                | 
                |     Given a SimSteps object mySteps, you can retrieve a SimModalDynamicStep
                |     named "Modal Dynamic Step.1" as following:
                | 
                |      ...
                |      myModalDynamicStep = mySteps.Item("Modal Dynamic Step.1")
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
    def time_increment(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TimeIncrement() As double
                |     Returns or sets the time increment value. Quantity: TIME, units: s.

        :return: float
        """

        return self.com_object.TimeIncrement

    @time_increment.setter
    def time_increment(self, value: float):
        """
        :param float value:
        """

        self.com_object.TimeIncrement = value

    @property
    def total_time(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property TotalTime() As double
                |     Returns or sets the total time value. Quantity: TIME, units: s.

        :return: float
        """

        return self.com_object.TotalTime

    @total_time.setter
    def total_time(self, value: float):
        """
        :param float value:
        """

        self.com_object.TotalTime = value

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

    def __repr__(self):
        return f'SimModalDynamicStep(name="{ self.name }")'
