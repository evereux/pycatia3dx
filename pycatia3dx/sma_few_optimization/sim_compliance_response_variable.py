"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable


class SimComplianceResponseVariable(SimNonParametricResponseVariable):

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
                |                             SimComplianceResponseVariable
                | 
                | Represents the compliance response variable object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimComplianceResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyComplianceResponseVariable As
                |      SimComplianceResponseVariable
                |      Set MyComplianceResponseVariable = MyFeatures.Add("SimComplianceResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimComplianceResponseVariable named "Compliance Response Variable.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyComplianceResponseVariable As
                |      SimComplianceResponseVariable
                |      Set MyComplianceResponseVariable = MyFeatures.Item("Compliance Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimComplianceResponseVariable as following:
                | 
                |      ...
                |      MyComplianceResponseVariable = MyFeatures.Add("SimComplianceResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimComplianceResponseVariable named "Compliance Response Variable.1" as
                |     following:
                | 
                |      ...
                |      MyComplianceResponseVariable = MyFeatures.Item("Compliance Response Variable.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def load_case(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LoadCase() As CATBaseDispatch (Read Only)
                |     Returns the Linear Loadcase.

        :return: AnyObject
        """

        return AnyObject(self.com_object.LoadCase)

    def __repr__(self):
        return f'SimComplianceResponseVariable(name="{ self.name }")'
