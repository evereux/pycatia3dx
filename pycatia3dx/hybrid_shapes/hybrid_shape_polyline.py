"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-27 14:29:47.477239

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.knowledge_interfaces.length import Length
from pycatia3dx.mmr_automation_interfaces.hybrid_shape import HybridShape
from pycatia3dx.mode.reference import Reference


class HybridShapePolyline(HybridShape):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     CATMmrAutomationInterfaces.HybridShape
                |                         HybridShapePolyline
                | 
                | Represents the hybrid shape polyline curve object.
                | Role: To access or set the data of the hybrid shape polyline object. This data
                | includes:
                | 
                |     Elements
                |     Radius
                |     Closure
                | 
                | Use the HybridShapeFactory object to create a HybridShapePolyline
                | object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def closure(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property Closure() As boolean
                |     Returns or sets the flag to decide closure of the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         Closure
                |             (For get_Closure) Returns or sets the closure
                |             property
                | 
                |             Example:
                |                 This example retrieves the closure property of the polyline of
                |                 the HybShpPolyline hybrid shape polyline.
                | 
                |                  Dim HybShpPolClosure As  boolean
                |                  HybShpPolClosure = HybShpPolyline.Closure

        :return: bool
        """

        return self.com_object.Closure

    @closure.setter
    def closure(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.Closure = value

    @property
    def number_of_elements(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Property NumberOfElements() As long (Read Only)
                |     Returns the number of elements of the polyline.
                | 
                |     Parameters:
                | 
                |         NumberOfElements
                |             Number of elements in the polyline.
                | 
                |             Example:
                |                 This example retrieves the number of elements in the polyline
                |                 of the HybShpPolyline hybrid shape polyline.
                | 
                |                  Dim HybShpPolNoOfEle As  long
                |                  HybShpPolNoOfEle = HybShpPolyline.NumberOfElements

        :return: int
        """

        return self.com_object.NumberOfElements

    def get_element(self, i_position: int, o_element: Reference, o_radius: Length) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub GetElement(long iPosition,Reference oElement,Length
                | oRadius)
                |     Returns the element of the polyline.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position at which the element is to be retrieved. 
                |         oElement
                |             Reference to the element. 
                |         ioRadius
                |             Length to the radius.
                | 
                |             Example:
                |                 This example retrieves the element and radius of the polyline
                |                 at specified position of the HybShpPolyline hybrid shape
                |                 polyline.
                | 
                |                  Dim HybShpPolylineElement As Reference
                |                  Dim HybShpPolylineRadius As Reference
                |                  HybShpPolyline.GetElement 1,
                |                  HybShpPolylineElement,HybShpPolylineRadius

        :param int i_position:
        :param Reference o_element:
        :param Length o_radius:
        :return: None
        """
        return self.com_object.GetElement(i_position, o_element.com_object, o_radius.com_object)

    def insert_element(self, i_point: Reference, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub InsertElement(Reference iPoint,long iPosition)
                |     Inserts the element at a specified position in the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             Reference of the point object to be inserted. 
                |         iPosition
                |             Position at which the element should be inserted.
                | 
                |             Example:
                |                 This example inserts the element in the polyline of the
                |                 HybShpPolyline hybrid shape polyline.
                | 
                |                  HybShpPolyline.InsertElement PointReference,1

        :param Reference i_point:
        :param int i_position:
        :return: None
        """
        return self.com_object.InsertElement(i_point.com_object, i_position)

    def remove_element(self, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub RemoveElement(long iPosition)
                |     Removes the element at a specified position in the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position from which the element should be should be
                |             removed.
                | 
                |             Example:
                |                 This example removes the element in the polyline of the
                |                 HybShpPolyline hybrid shape polyline.
                | 
                |                  HybShpPolyline.RemoveElement 1

        :param int i_position:
        :return: None
        """
        return self.com_object.RemoveElement(i_position)

    def replace_element(self, i_point: Reference, i_position: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub ReplaceElement(Reference iPoint,long iPosition)
                |     Replaces the element at a specified position in the
                |     polyline.
                | 
                |     Parameters:
                | 
                |         iPoint
                |             Reference of the point object that will replace the old element.
                |             
                |         iPosition
                |             Position at which the element should be inserted.
                | 
                |             Example:
                |                 This example replaces the element in the polyline of the
                |                 HybShpPolyline hybrid shape polyline.
                | 
                |                  HybShpPolyline.ReplaceElement PointReference, 1

        :param Reference i_point:
        :param int i_position:
        :return: None
        """
        return self.com_object.ReplaceElement(i_point.com_object, i_position)

    def set_radius(self, i_position: int, i_radius: float) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-27 14:29:47.477239)
                | Sub SetRadius(long iPosition,double iRadius)
                |     Sets the radius at specified position of the polyline.
                | 
                |     Parameters:
                | 
                |         iPosition
                |             Position at which radius should be set 
                |         iRadius
                |             Value of the radius to be set.
                | 
                |             Example:
                |                 This example sets the radius at the specific position of the
                |                 polyline of the HybShpPolyline hybrid shape
                |                 polyline.
                | 
                |                  HybShpPolyline.SetRadius 1, 10

        :param int i_position:
        :param float i_radius:
        :return: None
        """
        return self.com_object.SetRadius(i_position, i_radius)

    def __repr__(self):
        return f'HybridShapePolyline(name="{ self.name }")'
