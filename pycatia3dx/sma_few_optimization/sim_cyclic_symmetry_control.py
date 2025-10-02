"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.todo_sma_mpa_base.sim_axis import SimAxis
from pycatia3dx.todo_sma_mpa_base.sim_axis_system import SimAxisSystem


class SimCyclicSymmetryControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCyclicSymmetryControl
                | 
                | Represents the cyclic symmetry control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCyclicSymmetryControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCyclicSymmetryControl As SimCyclicSymmetryControl
                |      Set MyCyclicSymmetryControl = MyFeatures.Add("SimCyclicSymmetryControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimCyclicSymmetryControl named "Cyclic Symmetry Control.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCyclicSymmetryControl As SimCyclicSymmetryControl
                |      Set MyCyclicSymmetryControl = MyFeatures.Item("Cyclic Symmetry Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCyclicSymmetryControl as following:
                | 
                |      ...
                |      MyCyclicSymmetryControll = MyFeatures.Add("SimCyclicSymmetryControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimCyclicSymmetryControl named "Cyclic Symmetry Control.1" as
                |     following:
                | 
                |      ...
                |      MyCyclicSymmetryControll = MyFeatures.Item("Cyclic Symmetry Control.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
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
                |     Returns the local axis system used for Cyclic Symmetry Control.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def line(self) -> SimAxis:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Line() As SimAxis (Read Only)
                |     Returns the axis of symmetry used for cyclic symmetry control.

        :return: SimAxis
        """

        return SimAxis(self.com_object.Line)

    @property
    def specify_symmetry_plane_flag(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecifySymmetryPlaneFlag() As boolean
                |     Returns or sets the use of symmetry plane flag.
                |     FALSE : No symmetry plane is used ,
                |     TRUE : Symmetry plane is used.

        :return: bool
        """

        return self.com_object.SpecifySymmetryPlaneFlag

    @specify_symmetry_plane_flag.setter
    def specify_symmetry_plane_flag(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.SpecifySymmetryPlaneFlag = value

    @property
    def start_point(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property StartPoint() As CATBaseDispatch (Read Only)
                |     Returns the start point.

        :return: AnyObject
        """

        return AnyObject(self.com_object.StartPoint)

    def set_num_segments(self, i_num_segements: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetNumSegments(long iNumSegements)
                |     Sets the num of segements.
                | 
                |     Parameters:
                | 
                |         iVal
                |             [in] Number of segments value. Quantity: REAL, units: None

        :param int i_num_segements:
        :return: None
        """
        return self.com_object.SetNumSegments(i_num_segements)

    def __repr__(self):
        return f'SimCyclicSymmetryControl(name="{ self.name }")'
