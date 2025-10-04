"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimPortRegion(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimPortRegion
                | 
                | Represents the Port Region object.
                | 
                | Example:
                |     Given a SimFeatures object, you can create a SimPortRegion as
                |     following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyPortRegion As SimPortRegion
                |      Set MyPortRegion = MyFeatures.Add("SimPortRegion")
                |      
                | 
                |     Given a SimFeatures object, you can retrieve a SimPortRegion named "Port
                |     Region.1" as following:
                | 
                |      Dim MyFeatures As SimFeatures
                |      ...
                |      Dim MyPortRegion As SimPortRegion
                |      Set MyPortRegion = MyFeatures.Item("Port Region.1")
                |      
                | 
                | Example in Python:
                |     Given a SimFeatures object myFeatures, you can create a SimPortRegion as
                |     following:
                | 
                |      ...
                |      myPortRegion = myFeatures.Add("SimPortRegion")
                |      
                | 
                |     Given a SimFeatures object myFeatures, you can retrieve a SimPortRegion
                |     named "Port Region.1" as following:
                | 
                |      ...
                |      myPortRegion = myFeatures.Item("Port Region.1")
                |      
                | 
                | See also:
                |     SimFeatures
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def spec_tree_category(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SpecTreeCategory() As CATBSTR (Read Only)
                |     Returns a string representing the specification tree category of the
                |     feature. See SimFeatures.GetSpecTreeCategory for usage. 

        :return: str
        """

        return self.com_object.SpecTreeCategory

    def __repr__(self):
        return f'SimPortRegion(name="{ self.name }")'
