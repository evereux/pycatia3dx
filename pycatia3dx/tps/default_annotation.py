"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DefaultAnnotation(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DefaultAnnotation
                | 
                | This interface is used to get information about default
                | annotation.
                | Ther is two kinds of default annotation : - with a manual selection - with a selection automatic
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def link_wi_geom_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LinkWiGeomType() As CATBSTR (Read Only)
                |     Get the type of link between the default annotation and the geometry.
                |     Return E_FAIL if the annotation is not a default one.
                | 
                |     Parameters:
                | 
                |         oLinkWiGeom
                |             Type of link.

        :return: str
        """

        return self.com_object.LinkWiGeomType

    @property
    def search_algo_type(self) -> str:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SearchAlgoType() As CATBSTR (Read Only)
                |     Get the type of search algo to find geometry on which the annotation apply
                |     to. Return E_FAIL if the annotation is not a default one.
                | 
                |     Parameters:
                | 
                |         oAlgo
                |             Type of algo.

        :return: str
        """

        return self.com_object.SearchAlgoType

    def is_in_automatic_search_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func IsInAutomaticSearchMode() As boolean
                |     Get the type of search algo Return E_FAIL if the annotation is not a
                |     default one.
                | 
                |     Parameters:
                | 
                |         oIsAutoMode
                |             oIsAutoMode = TRUE if Automatic mode 

        :return: bool
        """
        return self.com_object.IsInAutomaticSearchMode()

    def __repr__(self):
        return f'DefaultAnnotation(name="{ self.name }")'
