"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.knowledge_interfaces.str_param import StrParam
from pycatia3dx.mode.reference import Reference
from pycatia3dx.part.dress_up_shape import DressUpShape


class Thread(DressUpShape):

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
                |                             Thread
                | 
                | Represents the Thread feature.
                | It threads or taps cylindrical surface .
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def depth(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Depth() As double
                |     Returns the thread/tap depth.
                | 
                |     Returns:
                |         oDepth Value of the thread/tap depth
                | 
                |         Example:
                |             The following example returns in Depth the depth of thread
                |             firstthread:
                | 
                |              Set Depth = firstthread.Depth

        :return: float
        """

        return self.com_object.Depth

    @depth.setter
    def depth(self, value: float):
        """
        :param float value:
        """

        self.com_object.Depth = value

    @property
    def diameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Diameter() As double
                |     Returns the thread/tap diameter.
                | 
                |     Returns:
                |         oDiameter Value of the thread/tap diameter
                | 
                |         Example:
                |             The following example returns in ThreadDiameter the diameter of
                |             thread firstthread:
                | 
                |              Set ThreadDiameter = firstthread.Diameter

        :return: float
        """

        return self.com_object.Diameter

    @diameter.setter
    def diameter(self, value: float):
        """
        :param float value:
        """

        self.com_object.Diameter = value

    @property
    def lateral_face_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LateralFaceElement() As Reference
                |     Returns or sets the lateral face (must be cylindrical) .
                |     To set the property, you can use the following Boundary object: Face.

        :return: Reference
        """

        return Reference(self.com_object.LateralFaceElement)

    @lateral_face_element.setter
    def lateral_face_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.LateralFaceElement = value

    @property
    def limit_face_element(self) -> Reference:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property LimitFaceElement() As Reference
                |     Returns or sets the limit face (must be planar ) .
                |     To set the property, you can use the following Boundary object: PlanarFace.

        :return: Reference
        """

        return Reference(self.com_object.LimitFaceElement)

    @limit_face_element.setter
    def limit_face_element(self, value: Reference):
        """
        :param Reference value:
        """

        self.com_object.LimitFaceElement = value

    @property
    def pitch(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Pitch() As double
                |     Returns the thread/tap pitch.
                | 
                |     Returns:
                |         oPitch Value of the thread/tap pitch
                | 
                |         Example:
                |             The following example returns in ThreadPitch the thread pitch of
                |             thread firstthread:
                | 
                |              Set ThreadPitch = firstthread.ThreadPitch

        :return: float
        """

        return self.com_object.Pitch

    @pitch.setter
    def pitch(self, value: float):
        """
        :param float value:
        """

        self.com_object.Pitch = value

    @property
    def side(self) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Side() As CatThreadSide
                |     Returns the thread or tap side.
                | 
                |     Returns:
                |         oThreadSide The thread/tap side (see CatThreadSide for list of possible
                |         sides)
                | 
                |         Example:
                |             The following example returns in ThreadSide the thread/tap side of
                |             thread firstthread:
                | 
                |              Set ThreadSide = firstthreadoThreadSide

        :return: CatThreadSide
        """

        return self.com_object.Side

    @side.setter
    def side(self, value: int):
        """
        :param int value:
        """

        self.com_object.Side = value

    @property
    def support_depth(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportDepth() As double (Read Only)
                |     Returns the depth of thread/tap support.
                | 
                |     Returns:
                |         oSupportDepth Value of the depth of thread/tap support
                | 
                |         Example:
                |             The following example returns in SupportDepth the support depth of
                |             thread firstthread:
                | 
                |              Set SupportDepth = firstthread.SupportDepth

        :return: float
        """

        return self.com_object.SupportDepth

    @property
    def support_diameter(self) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property SupportDiameter() As double (Read Only)
                |     Returns the diameter of thread/tap support.
                | 
                |     Returns:
                |         oSupportDiameter Value of the diameter of thread/tap
                |         support
                | 
                |         Example:
                |             The following example returns in SupportDiameter the support
                |             diameter of thread firstthread:
                | 
                |              Set SupportDiameter = firstthread.SupportDiameter

        :return: float
        """

        return self.com_object.SupportDiameter

    @property
    def thread_description(self) -> StrParam:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ThreadDescription() As StrParam (Read Only)
                |     Returns the thread/tap description parameter. This call is valid only when
                |     a standard/user design table created
                | 
                |     Returns:
                |         oThreadDescParam A Parameter object controlling the thread/tap
                |         description (see StrParam for more information)
                | 
                |         Example:
                |             The following example returns in threadDescription the thread
                |             description (M12 etc) of thread firstthread:
                | 
                |              Set threadDescription = firstthread.ThreadDescription

        :return: StrParam
        """

        return StrParam(self.com_object.ThreadDescription)

    def create_standard_thread_design_table(self, i_standard_type: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateStandardThreadDesignTable(CatThreadStandard
                | iStandardType)
                |     Creates a Standard Thread design table .
                | 
                |     Parameters:
                | 
                |         iStandardType
                |             Standard type for thread (see CatThreadStandard for list of
                |             possible types)
                | 
                |             Example:
                |                 The following example creates a standard table for
                |                 MetricThinPitch for thread firstthread:
                | 
                |                  firstthread.CreateStandardThreadDesignTable
                |                  catMetricThinPitch

        :param int i_standard_type:
        :return: None
        """
        return self.com_object.CreateStandardThreadDesignTable(i_standard_type)

    def create_user_standard_design_table(self, i_standard_name: str, i_path: str) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub CreateUserStandardDesignTable(CATBSTR iStandardName,CATBSTR
                | iPath)
                |     Creates a UserStandard Thread design table .
                | 
                |     Parameters:
                | 
                |         iStandardName
                |             Name of the UserStandard thread. iStandardName should be empty if
                |             filepath is to be defined. 
                |         iPath
                |             Path of the UserStandard file. iPath is empty if the filepath is
                |             already defined through CATReffilesPath.
                | 
                |             Example1:
                |                 The following example creates a standard table for UserStandard
                |                 for thread firstThread. The file path is already defined thru
                |                 CATReffilesPath:
                | 
                |                  firstThread.CreateUserStandardDesignTable
                |                  "UserStandard",""
                | 
                |             Example2:
                |                 The following example creates a standard table for UserStandard
                |                 for thread firstThread when file path is not defined thru
                |                 CATReffilesPath:
                | 
                |                  firstThread.CreateUserStandardDesignTable
                |                  "","E:\\user\\standard\\UserStandard.txt"

        :param str i_standard_name:
        :param str i_path:
        :return: None
        """
        return self.com_object.CreateUserStandardDesignTable(i_standard_name, i_path)

    def reverse_direction(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub ReverseDirection()
                |     Swap the direction of the thread or the tap.

        :return: None
        """
        return self.com_object.ReverseDirection()

    def set_explicit_polarity(self, i_thread_polarity: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetExplicitPolarity(CatThreadPolarity iThreadPolarity)
                |     Sets the thread polarity explicit. Thread polarity is no more evaluated
                |     implicitly on basis of support face polarity
                | 
                |     Parameters:
                | 
                |         iThreadPolarity
                |             Standard type for thread (see CatThreadPolarity for list of
                |             possible types)
                | 
                |             Example:
                |                 The following example sets the thread polarity to Tap
                |                 explicitly thread firstthread:
                | 
                |                  firstthread.SetExplicitPolarity catTap

        :param int i_thread_polarity:
        :return: None
        """
        return self.com_object.SetExplicitPolarity(i_thread_polarity)

    def __repr__(self):
        return f'Thread(name="{ self.name }")'
