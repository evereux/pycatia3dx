"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable
from pycatia3dx.todo_sma_mpa_base.sim_axis_system import SimAxisSystem


class SimMomentOfInertiaResponseVariable(SimNonParametricResponseVariable):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    SMAFeaOptimizationIDLItf.SimDesignImprovementResponseVariable
                |                        SMAFeaOptimizationIDLItf.SimNonParametricResponseVariable
                |                             SimMomentOfInertiaResponseVariable
                | 
                | Represents the moment of inertia response variable object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimMomentOfInertiaResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyMomentOfInertiaResponseVariable As
                |      SimMomentOfInertiaResponseVariable
                |      Set MyMomentOfInertiaResponseVariable = MyFeatures.Add("SimMomentOfInertiaResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimMomentOfInertiaResponseVariable named "Moment Of Inertia Response
                |     Variable.1" as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyMomentOfInertiaResponseVariable As
                |      SimMomentOfInertiaResponseVariable
                |      Set MyMomentOfInertiaResponseVariable = MyFeatures.Item("Moment Of Inertia Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimMomentOfInertiaResponseVariable as following:
                | 
                |      ...
                |      MyMomentOfInertiaResponseVariable = MyFeatures.Add("SimMomentOfInertiaResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimMomentOfInertiaResponseVariable named "Moment Of Inertia Response
                |     Variable.1" as following:
                | 
                |      ...
                |      MyMomentOfInertiaResponseVariable = MyFeatures.Item("Moment Of Inertia Response Variable.1")
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
                |     Returns the axis system used for the displacement design response.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def component(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Component() As SimMomentOfInertiaComponent
                |     Returns or sets the component of Moment of Inertia Design Response.

        :return: int
        """

        return self.com_object.Component

    @component.setter
    def component(self, value: int):
        """
        :param int value:
        """

        self.com_object.Component = value

    def __repr__(self):
        return f'SimMomentOfInertiaResponseVariable(name="{ self.name }")'
