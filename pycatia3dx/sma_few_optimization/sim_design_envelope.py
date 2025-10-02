"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.sma_few_optimization.sim_design_improvement_design_variable import \
    SimDesignImprovementDesignVariable


class SimDesignEnvelope(SimDesignImprovementDesignVariable):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                    SMAFeaOptimizationIDLItf.SimDesignImprovementDesignVariable
                |                         SimDesignEnvelope
                | 
                | Represents the Design Space object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimDesignEnvelope as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyDesignSpace As SimDesignEnvelope
                |      Set MyDesignSpace = MyFeatures.Add("SimDesignEnvelope")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimDesignEnvelope named "Design Space.1" as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MyDesignSpace As SimDesignEnvelope
                |      Set MyDesignSpace = MyFeatures.Item("Design Space.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimDesignEnvelope as following:
                | 
                |      ...
                |      MyDesignSpace = MyFeatures.Add("SimDesignEnvelope")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimDesignEnvelope named "Design Space.1" as following:
                | 
                |      ...
                |      MyDesignSpace = MyFeatures.Item("Design Space.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: str) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add(CATBSTR iType) As CATBaseDispatch
                |     Creates a Preserved Region or Local optimization Area feature object and
                |     returns it.
                | 
                |     Parameters:
                | 
                |         iType
                |             The Feature Type to be created. Possible values for iType
                |             are:
                | 
                |                 For Add:
                |                     SimLocalOptimizationArea : Creates a design local optimization area feature. It is of type SimLocalOptimizationArea.
                |                     SimPreservedRegion : Creates a preserved region feature. It is of type SimPreservedRegion.
                |                     iParent
                |                         The Optimization feature under which the new has to be
                |                         created 
                | 
                |     Returns:
                |         The created feature object.

        :param str i_type:
        :return: AnyObject
        """
        return self.com_object.Add(i_type)

    def __repr__(self):
        return f'SimDesignEnvelope(name="{ self.name }")'
