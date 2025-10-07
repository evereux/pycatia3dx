"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.opns_section.section import Section
from pycatia3dx.types.general import CATVariant


class SectionService(Service):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Service
                |                         SectionService
                | 
                | Interface representing CATIASectionService.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self) -> Section:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Add() As Section
                |     Create a section object which takes all products of the documents into
                |     account. This section is created in an existing review
                | 
                |     Example:
                | 
                |           
                | 
                |          Dim mySectionSrv As SectionService
                |          Set mySectionSrv = CurrentEditor.GetService("SectionService")
                |          Dim mySection as Section
                |          mySection = mySectionSrv.Add

        :return: Section
        """
        return Section(self.com_object.Add())

    def count(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Count() As long
                |     Count the number of section in the current review
                | 
                |     Example:
                | 
                |            Control the expected number of sections to display error
                |            message
                |            
                | 
                |              If MySrv.Count <>0 Then 
                |               MsgBox "Error number of sections not expected"
                |              End If

        :return: int
        """
        return self.com_object.Count()

    def item(self, i_index: CATVariant) -> Section:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func Item(CATVariant iIndex) As Section
                |     Returns a Section object using its index from the Sections list in current
                |     review
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Section to retrieve from the list of Sections. As
                |             a numerics, this index is the rank of the Section in the current review The
                |             index of the first Section is 1, and the index of the last Section is Count.
                |             
                | 
                |     Example:
                | 
                |             This example retrieves in ThisSection the first Section
                |             
                |             Section Of MyProduct from the SectionSrvSectionServices.
                |             
                |             
                | 
                |             Dim ThisSection As Section
                |             Set ThisSection = TheSections.Item(1)

        :param CATVariant i_index:
        :return: Section
        """
        return Section(self.com_object.Item(i_index))

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub Remove(CATVariant iIndex)
                |     Removes a Section object from the current review
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index of the Section to remove from the list of Sections. As a
                |             numerics, this index is the rank of the Section.in the current review The index
                |             of the first Section is 1, and the index of the last Section is Count.
                |             
                | 
                |     Example:
                | 
                |             The following example removes the first Section
                |
                |             MySrv.Remove(1)

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'SectionService(name="{ self.name }")'
