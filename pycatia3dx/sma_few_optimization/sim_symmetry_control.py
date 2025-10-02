"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimSymmetryControl(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimSymmetryControl
                | 
                | Represents the symmetry control object.
                | 
                | Example:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimSymmetryControl as following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MySymmetryControl As SimSymmetryControl
                |      Set MySymmetryControl = MyFeatures.Add("SimSymmetryControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object, you can retrieve a
                |     SimSymmetryControl named " Symmetry Control.1" as
                |     following:
                | 
                |      Dim MyFeatures As SimDesignImprovementFeatures
                |      ...
                |      Dim MySymmetryControl As SimSymmetryControl
                |      Set MySymmetryControl = MyFeatures.Item("Symmetry Control.1")
                |      
                | 
                | Example in Python:
                |     Given a SimDesignImprovementFeatures object, you can create a
                |     SimSymmetryControl as following:
                | 
                |      ...
                |      MySymmetryControl = MyFeatures.Add("SimSymmetryControl")
                |      
                | 
                |     Given a SimDesignImprovementFeatures object MyFeatures, you can retrieve a
                |     SimSymmetryControl named "Symmetry Control.1" as
                |     following:
                | 
                |      ...
                |      MySymmetryControl = MyFeatures.Item("Symmetry Control.1")
                |      
                | 
                | See also:
                |     SimDesignImprovementFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def plane(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Plane() As CATBaseDispatch (Read Only)
                |     Returns the plane associated to the Symmetry Control.

        :return: AnyObject
        """

        return AnyObject(self.com_object.Plane)

    def __repr__(self):
        return f'SimSymmetryControl(name="{ self.name }")'
