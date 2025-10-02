"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable


class SimAbsoluteMassResponseVariable(SimNonParametricResponseVariable):

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
                |                             SimAbsoluteMassResponseVariable
                | 
                | Represents the absolute mass response variable object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimAbsoluteMassResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyAbsoluteMassResponseVariable As
                |      SimAbsoluteMassResponseVariable
                |      Set MyAbsoluteMassResponseVariable = MyFeatures.Add("SimAbsoluteMassResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimAbsoluteMassResponseVariable named "Absolute Mass Response Variable.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyAbsoluteMassResponseVariable As
                |      SimAbsoluteMassResponseVariable
                |      Set MyAbsoluteMassResponseVariable = MyFeatures.Item("Absolute Mass Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimAbsoluteMassResponseVariable as following:
                | 
                |      ...
                |      MyAbsoluteMassResponseVariable = MyFeatures.Add("SimAbsoluteMassResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimAbsoluteMassResponseVariable named "Absolute Mass Response Variable.1" as
                |     following:
                | 
                |      ...
                |      MyAbsoluteMassResponseVariable = MyFeatures.Item("Absolute Mass Response Variable.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimAbsoluteMassResponseVariable(name="{ self.name }")'
