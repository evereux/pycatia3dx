"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class SimRebarLayers(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     SimRebarLayers
                | 
                | Represents the Rebar Layers collection.
                | 
                | Example:
                |     Given a SimShellSection object you can retrieve a SimRebarLayers collection
                |     as following:
                | 
                |      Dim MyShellSection As SimShellSection
                |      ...
                |      Dim MyRebarLayers As SimRebarLayers
                |      Set MyRebarLayers = MyShellSection.AllRebarLayers
                |      
                | 
                | Example in Python:
                |     Given a SimShellSection object you can retrieve a SimRebarLayers collection
                |     as following:
                | 
                |      ...
                |      myRebarLayers = myShellSection.AllRebarLayers
                |      
                | 
                | See also:
                |     SimShellSection
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As CATBaseDispatch
                |     Creates a Rebar Layer object and returns it.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom for which the Rebar Layer will be created.
                |             
                |         ospConnectorDamping[out]
                |             The created Rebar Layer. 
                | 
                |     Returns:
                |         The SimConnectorDamping object

        :return: AnyObject
        """
        return self.com_object.Add()

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Rebar Layer from the collection of Rebar Layers.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Rebar Layer. 
                | 
                |     Returns:
                |         The SimConnectorElasticity object

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes the specified Rebar Layer.
                | 
                |     Parameters:
                | 
                |         iDegreeOfFreedom[in]
                |             The degree of freedom for which the Rebar Layer will be removed.

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def remove_all(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAll()
                |     Removes all Rebar Layers. 

        :return: None
        """
        return self.com_object.RemoveAll()

    def __repr__(self):
        return f'SimRebarLayers(name="{ self.name }")'
