"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2020 on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.light_source import LightSource
from pycatia3dx.system.collection import Collection


class LightSources(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     LightSources
                | 
                | A collection of all the LightSource objects.
                | This collection is currently managed by a Viewer3D object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> LightSource:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Add() As LightSource
                |     Adds a new light source to the LightSources collection. 
                | 
                | Example:
                |     The following adds a light source to the collection attached to the active
                |     viewer. This viewer must be a @see Viewer3D object.
                | 
                |      Dim MyViewer As Viewer
                |      Set MyViewer = CATIA.ActiveWindow.ActiveViewer
                |      Dim MyLightSource As LightSource
                |      Set MyLightSource = MyViewer.LightSources.Add

        :return: LightSource
        """
        return LightSource(self.com_object.Add())

    def item(self, i_index: int) -> LightSource:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(long iIndex) As LightSource
                |     Returns a light source from its index in the LightSources
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the light source to retrieve in the collection of
                |             light sources. Compared with other collections, you cannot use the name of the
                |             light source as argument. 
                | 
                |     Returns:
                |         The retrieved light source 
                | 
                | Example:
                |     The following example returns in MyLightSource the sixth light source in
                |     the collection.
                | 
                |      Dim MyLightSource As LightSource
                |      Set MyLightSource = LightSources.Item(6)

        :param int i_index:
        :return: LightSource
        """
        return LightSource(self.com_object.Item(i_index))

    def remove(self, i_index: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Sub Remove(long iIndex)
                |     Removes a light source from the LightSources collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the light source to remove. Compared with other
                |             collections, you cannot use the name of the light source as argument.
                |             
                | 
                |     Example:
                |         The following example removes the second light source in the collection
                |         attached to the active viewer. This viewer must be a Viewer3D
                |         object.
                | 
                |          Dim MyViewer As Viewer
                |          Set MyViewer = CATIA.ActiveWindow.ActiveViewer
                |          MyViewer.LightSources.Remove(2)

        :param int i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'LightSources(name="{self.name}")'
