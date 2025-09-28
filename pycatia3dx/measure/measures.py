"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.measure.measure import Measure
from pycatia3dx.system.any_object import AnyObject
from pycatia3dx.system.collection import Collection
from pycatia3dx.types.general import CATVariant


class Measures(Collection):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     Measures
                | 
                | A collection of Measures.
                | 
                | The method VALReview.GetFactory ("Measures") on the VALReview retrieves this
                | collection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_text: str) -> Measure:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Add(CATBSTR iText) As Measure
                |     Adds a Measure to the collection.
                | 
                |     Parameters:
                | 
                |         iText
                |             The Measure type string 
                | 
                |     Returns:
                |         The created Measure 
                |     Example:
                | 
                |          This example creates a new Measure in the cMeasures
                |          collection.
                |          
                | 
                |          Dim cMeasures As Measures 
                |          Set cMeasures = TheVALReview.GetFactory("Measures")
                |          Dim oNewMeasure As Measure
                |          Set oNewMeasure = cMeasures.Add("Measure")

        :param str i_text:
        :return: Measure
        """
        return Measure(self.com_object.Add(i_text))

    def item(self, i_index: CATVariant) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Item(CATVariant iIndex) As CATBaseDispatch
                |     Returns a Measure using its index from the Measures
                |     collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Measure to retrieve from the
                |             collection of Measures. As a numerics, this index is the rank of the Measure in
                |             the collection. The index of the first Measure in the collection is 1, and the
                |             index of the last Measure is Count. As a string, it is the name you assigned to
                |             the Measure. 
                | 
                |     Returns:
                |         The retrieved Measure 
                |     Example:
                | 
                |          This example retrieves in oMeasure1 the third
                |          Measure,
                |          and in oMeasure2 the Measure named
                |          Measure3 from the cMeasures collection. 
                |          
                | 
                |          Dim oMeasure1 As Measure
                |          Set oMeasure1 = cMeasures.Item(3)
                |          Dim oMeasure2 As Measure
                |          Set oMeasure2 = cMeasures.Item("Measure3")

        :param CATVariant i_index:
        :return: AnyObject
        """
        return self.com_object.Item(i_index)

    def remove(self, i_index: CATVariant) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Sub Remove(CATVariant iIndex)
                |     Removes a Measure from the Measures collection.
                | 
                |     Parameters:
                | 
                |         iIndex
                |             The index or the name of the Measure to retrieve from the
                |             collection of Measures. As a numerics, this index is the rank of the Measure in
                |             the collection. The index of the first Measure in the collection is 1, and the
                |             index of the last Measure is Count. As a string, it is the name you assigned to
                |             the Measure. 
                | 
                |     Example:
                | 
                |          The following example removes the second Measure and the Measure
                |          named
                |          Measure2 from the cMeasures collection.
                |          
                | 
                |          cMeasures.Remove(2)
                |          cMeasures.Remove("Measure2")

        :param CATVariant i_index:
        :return: None
        """
        return self.com_object.Remove(i_index)

    def __repr__(self):
        return f'Measures(name="{ self.name }")'
