"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.system.any_object import AnyObject


class SimDynClashServices(Service):

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
                |                         SIMDynClashServices
                | 
                | Represents the simulation dynamic clash.
                | The dynamic clash is used to compute clash when objects are moving. Make sure
                | to call to UpdateClashAgent after modification.
                | Example:
                | 
                |      Dim MyDynClash As SIMDynClashServices
                |      
                |      'service retrieval'
                |      Set MyDynClash = CATIA.ActiveEditor.GetService("SIMDynClashServices")
                | 
                | 
                | See also:
                |     SIMDynClashResult
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def clash_analysis_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClashAnalysisMode() As boolean
                |     Indicates if the current dynamic clash is active or not.
                | 
                |     Example:
                | 
                |      Dim bClashAnalysisMode As Boolean
                |      bClashAnalysisMode = MyDynClash.ClashAnalysisMode

        :return: bool
        """

        return self.com_object.ClashAnalysisMode

    @clash_analysis_mode.setter
    def clash_analysis_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ClashAnalysisMode = value

    @property
    def clash_status(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClashStatus() As boolean (Read Only)
                |     Indicates if there is any clash to report.
                | 
                |     Example:
                | 
                |      Dim bClashStatus As Boolean
                |      bClashStatus = MyDynClash.ClashStatus

        :return: bool
        """

        return self.com_object.ClashStatus

    @property
    def clearance_analysis_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ClearanceAnalysisMode() As boolean
                |     Indicates if the current dynamic clash is active or not.
                | 
                |     Example:
                | 
                |      Dim bClearanceAnalysisMode As Boolean
                |      bClearanceAnalysisMode = MyDynClearance.ClearanceAnalysisMode

        :return: bool
        """

        return self.com_object.ClearanceAnalysisMode

    @clearance_analysis_mode.setter
    def clearance_analysis_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ClearanceAnalysisMode = value

    @property
    def contact_analysis_mode(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property ContactAnalysisMode() As boolean
                |     Indicates if the current dynamic clash is active or not.
                | 
                |     Example:
                | 
                |      Dim bContactAnalysisMode As Boolean
                |      bContactAnalysisMode = MyDynContact.ContactAnalysisMode

        :return: bool
        """

        return self.com_object.ContactAnalysisMode

    @contact_analysis_mode.setter
    def contact_analysis_mode(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.ContactAnalysisMode = value

    @property
    def penetration_reporting(self) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property PenetrationReporting() As boolean
                |     Indicates if the current dynamic clash is active or not.
                | 
                |     Example:
                | 
                |      Dim bPenetrationReporting As Boolean
                |      bPenetrationReporting = MyDynClash.PenetrationReporting

        :return: bool
        """

        return self.com_object.PenetrationReporting

    @penetration_reporting.setter
    def penetration_reporting(self, value: bool):
        """
        :param bool value:
        """

        self.com_object.PenetrationReporting = value

    def add_exclusion_object(self, i_object: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddExclusionObject(AnyObject iObject) As long
                |     Add an element to the list. The returned value will indicate
                |     if:
                | 
                |         0: if the object is invalid
                |         N: the object location.
                | 
                |     If the object is already in the list, the API will succeed and
                |     return
                | 
                |     Example:
                | 
                |      Dim MyObject
                |      'please perform object object valuation'
                |      Dim iLocation As Integer
                |      iLocation = MyDynClearance.AddExclusionObject(MyObject)

        :param AnyObject i_object:
        :return: int
        """
        return self.com_object.AddExclusionObject(i_object.com_object)

    def get_exclusion_list(self, o_list: tuple) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetExclusionList(CATSafeArrayVariant oList) As long
                |     Gets the list and size of the elements that needs to be
                |     excluded.
                | 
                |     Example:
                | 
                |      Dim MyExclusionList() As CATVariant
                |      Dim iListSize As Integer
                |      iListSize = MyDynClearance.GetExclusionList(MyExclusionList)

        :param tuple o_list:
        :return: int
        """
        return self.com_object.GetExclusionList(o_list)

    def locate_exclusion_object(self, i_object: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func LocateExclusionObject(AnyObject iObject) As long
                |     Locate an element in the list. The returned value will indicate
                |     if:
                | 
                |         0: if the object is invalid or missing
                |         N: the object location.
                | 
                |     Example:
                | 
                |      Dim MyObject
                |      'please perform object object valuation'
                |      Dim iLocation As Integer
                |      iLocation = MyDynClearance.LocateExclusionObject(MyObject)

        :param AnyObject i_object:
        :return: int
        """
        return self.com_object.LocateExclusionObject(i_object.com_object)

    def remove_exclusion_object(self, i_object: AnyObject) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RemoveExclusionObject(AnyObject iObject) As long
                |     Remove an element from the list. The returned value will indicate
                |     if:
                | 
                |         0: if the object is invalid or missing
                |         N: the object location before removal.
                | 
                |     Example:
                | 
                |      Dim MyObject
                |      'please perform object object valuation'
                |      Dim iLocation As Integer
                |      iLocation = MyDynClearance.RemoveExclusionObject(MyObject)

        :param AnyObject i_object:
        :return: int
        """
        return self.com_object.RemoveExclusionObject(i_object.com_object)

    def retrieve_results(self, o_list: tuple) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func RetrieveResults(CATSafeArrayVariant oList) As long
                |     Retrieve the results of the current clashes as a list of
                |     SIMDynClashResult.
                | 
                |     Example:
                | 
                |      Dim MyExclusionList() As CATVariant
                |      Dim iListSize As Integer
                |      iListSize = MyDynClearance.RetrieveResults(MyExclusionList)
                | 
                |     See also:
                |         SIMDynClashResult

        :param tuple o_list:
        :return: int
        """
        return self.com_object.RetrieveResults(o_list)

    def update_clash_agent(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub UpdateClashAgent()
                |     Make sure to call this API after any changes to update the
                |     service.
                | 
                |     Example:
                | 
                |      MyDynClearance.UpdateClashAgent

        :return: None
        """
        return self.com_object.UpdateClashAgent()

    def __repr__(self):
        return f'SimDynClashServices(name="{ self.name }")'
