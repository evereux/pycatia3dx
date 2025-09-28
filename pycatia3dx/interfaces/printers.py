"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-13 15:35:27.265802

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.interfaces.printer import Printer
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Printers(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Printers
                | 
                | A collection of all the Printer objects managed by the
                | application.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def item(self, i_index: CATVariant) -> Printer:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-13 15:35:27.265802)
                | Func Item(CATVariant iIndex) As Printer
                |     Returns a printer using its index or its device name from the Printers
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the printer to retrieve from the
                |             collection of printers. As a numerics, this index is the rank of the printer in
                |             the collection. The index of the first printer in the collection is 1, and the
                |             index of the last printer is Count. As a string, it is the DeviceName of the
                |             printer. 
                | 
                |     Returns:
                |         The retrieved printer 
                |     Example:
                |         This example returns in ThisPrinter the third printer in the
                |         collection, and in ThatPrinter the printer named
                |         LaserPrinter.
                | 
                |          Dim ThisPrinter As Printer
                |          Set ThisPrinter = CATIA.Printers.Item(3)
                |          Dim ThatPrinter As Printer
                |          Set ThatPrinter = CATIA.Printers.Item("LaserPrinter")

        :param CATVariant i_index:
        :return: Printer
        """
        return Printer(self.com_object.Item(i_index))

    def __repr__(self):
        return f'Printers(name="{self.name}")'
