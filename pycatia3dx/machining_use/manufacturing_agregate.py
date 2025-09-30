"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingAgregate(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingAgregate
                | 
                | Interface to manage manufacturing aggregate.
                | 
                | The aggregate contains many elements that can be sorted according to their
                | types.
                | The type of the elements is the name of an interface that all these elements
                | implement.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_element(self, i_position: int) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetElement(long iPosition) As AnyObject
                |     Returns the element of a given type and for a given position in the
                |     aggregate.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             The position of the element in the agregate 
                | 
                |     Returns:
                |         The element of the given type and the given position in the aggregate

        :param int i_position:
        :return: AnyObject
        """
        return AnyObject(self.com_object.GetElement(i_position))

    def get_number_of_elements(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetNumberOfElements() As long
                |     Returns the count of elements of a given type in the
                |     aggregate.
                | 
                |     Returns:
                |         The number of elements of the given type

        :return: int
        """
        return self.com_object.GetNumberOfElements()

    def __repr__(self):
        return f'ManufacturingAgregate(name="{ self.name }")'
