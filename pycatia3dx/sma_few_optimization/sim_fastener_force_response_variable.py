"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_few_optimization.sim_non_parametric_response_variable import SimNonParametricResponseVariable


class SimFastenerForceResponseVariable(SimNonParametricResponseVariable):

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
                |                             SimFastenerForceResponseVariable
                | 
                | Represents the fastener force response variable object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFastenerForceResponseVariable as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyFastenerForcesResponseVariable As
                |      SimFastenerForceResponseVariable
                |      Set MyFastenerForcesResponseVariable = MyFeatures.Add("SimFastenerForceResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimFastenerForceResponseVariable named "Fastener Force Response Variable.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyFastenerForcesResponseVariable As
                |      SimFastenerForceResponseVariable
                |      Set MyFastenerForcesResponseVariable = MyFeatures.Item("Fastener Force Response Variable.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimFastenerForceResponseVariable as following:
                | 
                |      ...
                |      MyFastenerForcesResponseVariable = MyFeatures.Add("SimFastenerForceResponseVariable")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimFastenerForceResponseVariable named "Fastener Force Response Variable.1" as
                |     following:
                | 
                |      ...
                |      MyFastenerForcesResponseVariable = MyFeatures.Item("Fastener Force  Response Variable.1")
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

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As SimFastenerForceType
                |     Returns or sets the type of fastener force design response.

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def __repr__(self):
        return f'SimFastenerForceResponseVariable(name="{ self.name }")'
