"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class SimCompositeGridElemRef(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     SimCompositeGridElemRef
                | 
                | Represents the Composite Grid Element Reference object.
                | Given a SimCompositeGridElemRefGroup object, you can retrieve a SimCompositeGridElemRef as below: .... Refer SMAIAMpaCompositeGridElemRefGroup.idl to create/retrieve a SimCompositeGridElemRefGroup. .... Dim myCompositeRefElem As SimCompositeGridElemRef Set myCompositeRefElem = myCompositeRefElemGroup.AddNewElemRef or Dim listElems listElems = myCompositeRefElemGroup.GetElementRefs ...Loop for listSize = UBound(listElems) - LBound(listElems) + 1 if needed.. myCompositeRefElemGroup = listElems(0)
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def get_geometry(self) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetGeometry() As CATBaseDispatch
                |     Retreives a reference geometry of this element.
                | 
                |     Returns:
                |         Geometry of the reference element Eg are line, plane etc.

        :return: AnyObject
        """
        return self.com_object.GetGeometry()

    def set_geometry(self, i_geometry: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetGeometry(CATBaseDispatch iGeometry)
                |     Sets a reference geometry to this element.
                | 
                |     Parameters:
                | 
                |         oGeometry
                |             [in] Geometry for the reference element Eg are line, plane etc.

        :param AnyObject i_geometry:
        :return: None
        """
        return self.com_object.SetGeometry(i_geometry.com_object)

    def __repr__(self):
        return f'SimCompositeGridElemRef(name="{ self.name }")'
