"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_few_optimization.enums import SimDesignResponseDirection
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable
from pycatia3dx.sma_mpa_base.sim_axis_system import SimAxisSystem


class SimCenterOfGravityResponseVariable(SimNonParametricResponseVariable):

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
                |                             SimCenterOfGravityResponseVariable
                | 
                | Represents the center of gravity response variable object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCenterOfGravityResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCenterOfGravityResponseVariable As
                |      SimCenterOfGravityResponseVariable
                |      Set MyCenterOfGravityResponseVariable = MyFeatures.Add("SimCenterOfGravityResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimCenterOfGravityResponseVariable named "Center of Gravity Response
                |     Variable.1" as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyCenterOfGravityResponseVariable As
                |      SimCenterOfGravityResponseVariable
                |      Set MyCenterOfGravityResponseVariable = MyFeatures.Item("Center of Gravity Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimCenterOfGravityResponseVariable as following:
                | 
                |      ...
                |      MyCenterOfGravityResponseVariable = MyFeatures.Add("SimCenterOfGravityResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimCenterOfGravityResponseVariable named "Center of Gravity Response
                |     Variable.1" as following:
                | 
                |      ...
                |      MyCenterOfGravityResponseVariable = MyFeatures.Item("Center of Gravity Response Variable.1")
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
                |     Returns the axis system used for the Center of Gravity design response.

        :return: SimAxisSystem
        """

        return SimAxisSystem(self.com_object.AxisSystem)

    @property
    def direction(self) -> SimDesignResponseDirection:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Direction() As SimDesignResponseDirection
                |     Returns or sets the direction of Center of Gravity design response.

        :return: SimDesignResponseDirection
        """

        return SimDesignResponseDirection(self.com_object.Direction)

    @direction.setter
    def direction(self, value: SimDesignResponseDirection):
        """
        :param SimDesignResponseDirection value:
        """

        self.com_object.Direction = value

    def __repr__(self):
        return f'SimCenterOfGravityResponseVariable(name="{ self.name }")'
