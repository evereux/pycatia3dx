"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class DrawingThread(AnyObject):

    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     DrawingThread
                | 
                | Represents a drawing thread in a drawing view.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def type(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Type() As CatThreadType
                |     Returns or sets a CatThreadType (threaded or taped) on a thread. Be
                |     careful, this method is only available on threads which are linked to 2D circle
                |     geometry 
                | 
                | Example:
                |     The following example sets the type Taped in MyThread
                | 
                |       If MyThread.IsLinkedTo()=cat2DCircle Then
                |          MyThread.Type = catTaped
                |        End If

        :return: int
        """

        return self.com_object.Type

    @type.setter
    def type(self, value: int):
        """
        :param int value:
        """

        self.com_object.Type = value

    def is_linked_to(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func IsLinkedTo() As CatThreadLinkedTo
                |     Specifies which kind of objects the thread is linked to.
                | 
                |     Returns:
                |         oLinkedType The type of thread link 
                | 
                | Example:
                |     The following example retrieves the CatThreadLinkedTo in MyThread This view
                |     belongs to the drawing view collection of the drawing
                |     sheet
                | 
                |      ThreadLinkType = MyThread.IsLinkedTo

        :return: int
        """
        return self.com_object.IsLinkedTo()

    def __repr__(self):
        return f'DrawingThread(name="{ self.name }")'
