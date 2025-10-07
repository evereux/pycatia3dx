"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.todo_part.defeaturing_filters import DefeaturingFilters
from pycatia3dx.todo_part.dress_up_shape import DressUpShape


class Defeaturing(DressUpShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.Shape
                |                         CATPartIDLItf.DressUpShape
                |                             Defeaturing
                | 
                | Represents the defeaturing.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def filters(self) -> DefeaturingFilters:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Filters() As DefeaturingFilters (Read Only)
                |     Returns the filter collection of the Defeaturing. The returned object is
                |     the filter collection associated to this Defeaturing object. All changes
                |     applied to the returned collection will be automatically applied to the
                |     Defeaturing object. As a consequence there is no need to affect the collection
                |     to the defeaturing after the change to update the
                |     property.
                | 
                |     Returns:
                |         oFilters The filter collection (see DefeaturingFilters for list of
                |         possible actions)
                | 
                |         Example:
                |             The following example returns in myDefeaturingFiltersCollection the
                |             filter collection of the Defeaturing
                |             firstDefeaturing:
                | 
                |              Set myDefeaturingFiltersCollection = firstDefeaturing.Filters

        :return: DefeaturingFilters
        """

        return DefeaturingFilters(self.com_object.Filters)

    def __repr__(self):
        return f'Defeaturing(name="{ self.name }")'
