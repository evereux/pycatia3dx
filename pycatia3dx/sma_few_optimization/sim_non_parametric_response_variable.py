"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.sma_few_optimization.sim_design_improvement_response_variable import \
    SimDesignImprovementResponseVariable


class SimNonParametricResponseVariable(SimDesignImprovementResponseVariable):

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
                |                         SimNonParametricResponseVariable
                | 
                | Represents the Non-Parametric Response Variable.
                | Base class for Non-Parametric Response Variable.
                | 
                | Example:
                |     Given a SimNonParametricFeatures object, you can retrieve a
                |     SimNonParametricResponseVariable named "ResponseVariable.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyResponseVariable As
                |      SimNonParametricResponseVariable
                |      Set MyResponseVariable = MyFeatures.Item("ResponseVariable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures collection, you can retrieve a
                |     SimNonParametricResponseVariable object as following:
                | 
                |      ...
                |      MyResponseVariable  = MyFeatures.Item("Response Variable.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def __repr__(self):
        return f'SimNonParametricResponseVariable(name="{ self.name }")'
