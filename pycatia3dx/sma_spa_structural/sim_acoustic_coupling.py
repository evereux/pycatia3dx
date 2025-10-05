"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimAcousticCoupling(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimAcousticCoupling
                | 
                | Represents the Acoustic Coupling object.
                | 
                | Example:
                |     Given a SimAbstractions object, you can create a SimAcousticCoupling as
                |     following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyAcousticCoupling As SimAcousticCoupling
                |      Set MyAcousticCoupling = MyAbstractions.Add("SimAcousticCoupling")
                |      
                | 
                |     Given a SimAbstractions object, you can retrieve a SimAcousticCoupling
                |     named "Acoustic Coupling.1" as following:
                | 
                |      Dim MyAbstractions As SimAbstractions
                |      ...
                |      Dim MyAcousticCoupling As SimAcousticCoupling
                |      Set MyAcousticCoupling = MyAbstractions.Item("Acoustic Coupling.1")
                |      
                | 
                | Example in Python:
                |     Given a SimAbstractions object myAbstractions, you can create a
                |     SimAcousticCoupling as following:
                | 
                |      ...
                |      myAcousticCoupling = myAbstractions.Add("SimAcousticCoupling")
                |      
                | 
                |     Given a SimAbstractions object myAbstractions, you can retrieve a
                |     SimAcousticCoupling named "Acoustic Coupling.1" as
                |     following:
                | 
                |      ...
                |      myAcousticCoupling = myAbstractions.Item("Acoustic Coupling.1")
                |      
                | 
                | See also:
                |     SimAbstractions
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def adjust_secondary_surface_initial_position_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdjustSecondarySurfaceInitialPositionFlag() As
                | boolean
                |     Retrieves a flag that determines whether the adjustment of the initial
                |     position of the secondary surface is enabled or not.
                |     TRUE: all tied nodes are moved in the initial
                |     configuration.
                | 
                |     FALSE: prevents all tied nodes on the secondary surface from moving onto
                |     the main surface.

        :return: bool
        """

        return self.com_object.AdjustSecondarySurfaceInitialPositionFlag

    @adjust_secondary_surface_initial_position_flag.setter
    def adjust_secondary_surface_initial_position_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdjustSecondarySurfaceInitialPositionFlag = value

    @property
    def adjust_slave_surface_initial_position_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property AdjustSlaveSurfaceInitialPositionFlag() As boolean
                |     Deprecated R424

        :return: bool
        """

        return self.com_object.AdjustSlaveSurfaceInitialPositionFlag

    @adjust_slave_surface_initial_position_flag.setter
    def adjust_slave_surface_initial_position_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.AdjustSlaveSurfaceInitialPositionFlag = value

    @property
    def formulation_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FormulationType() As
                | SimAcousticCouplingFormulationType
                |     Returns or sets the formulation type.

        :return: int
        """

        return self.com_object.FormulationType

    @formulation_type.setter
    def formulation_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.FormulationType = value

    @property
    def main_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MainSurface() As CATBaseDispatch (Read Only)
                |     Returns the main surface.

        :return: AnyObject
        """

        return AnyObject(self.com_object.MainSurface)

    @property
    def main_surface_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MainSurfaceType() As
                | SimAcousticCouplingMainSurfaceType
                |     Returns or sets the main surface type.

        :return: int
        """

        return self.com_object.MainSurfaceType

    @main_surface_type.setter
    def main_surface_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.MainSurfaceType = value

    @property
    def master_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MasterSurface() As CATBaseDispatch (Read Only)
                |     Deprecated R424

        :return: AnyObject
        """

        return AnyObject(self.com_object.MasterSurface)

    @property
    def master_surface_type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property MasterSurfaceType() As
                | SimAcousticCouplingMasterSurfaceType
                |     Deprecated R424

        :return: int
        """

        return self.com_object.MasterSurfaceType

    @master_surface_type.setter
    def master_surface_type(self, value: int):
        """
        :param int value:
        """

        self.com_object.MasterSurfaceType = value

    @property
    def position_tolerance(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionTolerance() As double
                |     Returns or sets the position tolerance. Quantity: LENGTH, units: m.

        :return: float
        """

        return self.com_object.PositionTolerance

    @position_tolerance.setter
    def position_tolerance(self, value: float):
        """
        :param float value:
        """

        self.com_object.PositionTolerance = value

    @property
    def position_tolerance_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PositionToleranceFlag() As boolean
                |     Returns or sets the flag that determines if the position tolerance is
                |     applied.
                | 
                |     TRUE: the position tolerance is applied.
                | 
                |     FALSE: the position tolertance is not applied.

        :return: bool
        """

        return self.com_object.PositionToleranceFlag

    @position_tolerance_flag.setter
    def position_tolerance_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PositionToleranceFlag = value

    @property
    def secondary_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SecondarySurface() As CATBaseDispatch (Read Only)
                |     Returns the secondary surface.

        :return: AnyObject
        """

        return AnyObject(self.com_object.SecondarySurface)

    @property
    def slave_surface(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SlaveSurface() As CATBaseDispatch (Read Only)
                |     Deprecated R424

        :return: AnyObject
        """

        return AnyObject(self.com_object.SlaveSurface)

    def swap_main_and_secondary(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SwapMainAndSecondary()
                |     Swaps the main and secondary surfaces.

        :return: None
        """
        return self.com_object.SwapMainAndSecondary()

    def swap_master_and_slave(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SwapMasterAndSlave()
                |     Deprecated R424 

        :return: None
        """
        return self.com_object.SwapMasterAndSlave()

    def __repr__(self):
        return f'SimAcousticCoupling(name="{ self.name }")'
