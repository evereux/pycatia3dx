"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.interfaces.service import Service
from pycatia3dx.plm_modeller_base.plm_entity import PLMEntity


class PLMRefreshService(Service):
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
                |                         PLMRefreshService
                | 
                | Interface representing service to manage Refresh operation.
                | Example of how to retrieve such an object using
                | Application.GetSessionService:
                | 
                |    // Retrieve the Refresh Service
                |    Dim oRefreshService as PLMRefreshService
                |    Set oRefreshService = CATIA.GetSessionService("PLMRefreshService")
                | 
                |    // for global refresh
                |    oRefreshService.PerformRefresh
                | 
                |    // for selective refresh
                |    oRefreshService.AddObjectToRefresh iEntity1        // iEntity1 : is object to be refreshed and it must be PLMComponent
                |    oRefreshService.AddObjectToRefresh iEntity2        // iEntity2 : 2nd object to be refreshed => and so on... to add more objects 
                |    Dim oConcurrentEngineeringStatus() As Variant      // output status of
                |    objects in the same sequence of addition using
                |    AddObjectToRefresh
                |    oRefreshService.getConcurrentEngineeringStatus oConcurrentEngineeringStatus 
                |    // retrieve concurrency status (must be called)
                |    oRefreshService.PerformRefresh
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_object_to_refresh(self, i_plm_entity: PLMEntity) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub AddObjectToRefresh(PLMEntity iPLMEntity)
                |     Adds object to be analysed for selective refresh operation (object must be
                |     PLMComponent) No need to call this method for Global refresh
                |     operation
                | 
                |     Parameters:
                | 
                |         iPLMEntity
                |             input PLMComponent to be analysed for selective refresh operation.
                |             this method can be called several times to add more than one object for refresh
                |             before calling getConcurrentEngineeringStatus. 
                | 
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                | 
                |         S_OK
                |             if addition succeeded.
                |         E_INVALIDARG
                |             if input object is NULL
                |         E_FAIL
                |             if addition failed .

        :param PLMEntity i_plm_entity:
        :return: None
        """
        return self.com_object.AddObjectToRefresh(i_plm_entity.com_object)

    def perform_refresh(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub PerformRefresh()
                |     Refreshes your model by loading the modifications that have been performed
                |     and saved by another user since you have opened the model.
                | 
                |         It will perform Global Refresh by default.
                |         For using selective refresh getConcurrentEngineeringStatus must be
                |         called earlier to proceed with PerformRefresh
                | 
                |             Returns:
                |                 An HRESULT value.
                |                 Legal values:
                | 
                |                 S_OK
                |                     Refresh successful.
                |                 E_INVALIDARG
                |                     At least one object to be refreshed is UI
                |                     active
                |                 E_FAIL
                |                     Refresh failed due to some internal error
                |                     occurred.

        :return: None
        """
        return self.com_object.PerformRefresh()

    def get_concurrent_engineering_status(self, o_concurrent_engineering_status: tuple) -> int:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub getConcurrentEngineeringStatus(CATSafeArrayVariant
                | oConcurrentEngineeringStatus)
                |     Gets ConcurrentEngineeringStatus status of objects that are added using
                |     AddObjectToRefresh method No need to call this method for Global refresh
                |     operation Call to the server is performed: consequently the performances of the
                |     method are dependent on this
                |
                |     Parameters:
                |
                |         oConcurrentEngineeringStatus
                |             The list of object concurrent access status at the time of
                |             call.
                |
                |             UnchangedInDatabase
                |                 There is no change in the database for given
                |                 object.
                |             ModifiedInDatabaseAndNotInSession
                |                 Given object is modified in the database.
                |             ModifiedInDatabaseAndInSession
                |                 There are conflicting changes made to the object in the
                |                 database and in session.
                |             DeletedInDatabase
                |                 Given object is removed from the database.
                |             ExistInDatabaseAndNotInSession
                |                 Given object exists in database but not loaded in
                |                 session.
                |
                |     Returns:
                |         An HRESULT value.
                |         Legal values:
                |
                |         S_OK
                |             If the concurrent access status is retrieved
                |             correctly.
                |         E_INVALIDARG
                |             The input list contains non-PLMComponent/UI active
                |             objects.
                |         E_FAIL
                |             If concurrent access status retrieval fails.

        :param tuple o_concurrent_engineering_status:
        :return: int
        """
        return self.com_object.getConcurrentEngineeringStatus(o_concurrent_engineering_status)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_concurrent_engineering_status'
        # vba_code = """
        # Public Function get_concurrent_engineering_status(plm_refresh_service)
        #     Dim oConcurrentEngineeringStatus (2)
        #     plm_refresh_service.getConcurrentEngineeringStatus oConcurrentEngineeringStatus
        #     get_concurrent_engineering_status = oConcurrentEngineeringStatus
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'PLMRefreshService(name="{self.name}")'
