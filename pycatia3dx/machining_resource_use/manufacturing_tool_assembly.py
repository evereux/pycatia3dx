"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia3dx.system.any_object import AnyObject


class ManufacturingToolAssembly(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     ManufacturingToolAssembly
                | 
                | Interface dedicated to Tool Assembly objects management.
                | Role: This interface offers services to manage mainly the associated tool and
                | holder.
                | Common attributes are declared in CATMfgToolAssemblyConstant.
                | 
                | See also:
                |     CATBaseUnknown
                | See also:
                |     DELIMfgTool
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add_component(self, i_component: AnyObject) -> AnyObject:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func AddComponent(AnyObject iComponent) As AnyObject
                |     Adds a new component to tool assembly.
                | 
                |     Parameters:
                | 
                |         iComponent
                |             : PLM object to add 
                |         oInstance
                |             : return instance

        :param AnyObject i_component:
        :return: AnyObject
        """
        return AnyObject(self.com_object.AddComponent(i_component.com_object))

    def get_all_components(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetAllComponents() As CATSafeArrayVariant
                |     Returns the list of all components associated with the tool
                |     assembly.
                | 
                |     Parameters:
                | 
                |         oListofComponent
                |             List of PLM Object. First, all elements in list are removed.

        :return: tuple
        """
        return self.com_object.GetAllComponents()

    def get_all_stages(self, o_nb_stages: int, o_list_of_height: tuple, o_list_of_diam1: tuple, o_list_of_diam2: tuple,
                       is_local: bool) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub GetAllStages(long oNbStages,CATSafeArrayVariant
                | oListOfHeight,CATSafeArrayVariant oListOfDiam1,CATSafeArrayVariant
                | oListOfDiam2,boolean IsLocal)
                |     Returns Number of stages with the value of Gage between Tool and First
                |     Holder.
                | 
                |     Parameters:
                | 
                |         oNbStages
                |             : Number of stages 
                |         oListOfHeight:
                |             height definition 
                |         oListOfDiam1
                |             : diameter definition 
                |         oListOfDiam2
                |             : conical diameter definition

        :param int o_nb_stages:
        :param tuple o_list_of_height:
        :param tuple o_list_of_diam1:
        :param tuple o_list_of_diam2:
        :param bool is_local:
        :return: None
        """
        return self.com_object.GetAllStages(o_nb_stages, o_list_of_height, o_list_of_diam1, o_list_of_diam2, is_local)

    def get_editable_status(self, i_activity: AnyObject) -> bool:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetEditableStatus(AnyObject iActivity) As boolean
                |     Returns a boolean: if TRUE, it means that the Tool Assembly is editable for
                |     the given Activity if FALSE, the Tool Assembly can not be modified on this
                |     entity
                | 
                |     Parameters:
                | 
                |         iActivity
                |             The activity for which you want to know the edit capability of the
                |             tool assembly

        :param AnyObject i_activity:
        :return: bool
        """
        return self.com_object.GetEditableStatus(i_activity.com_object)

    def get_holders(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetHolders() As CATSafeArrayVariant
                |     Returns the list of holder associated with the tool
                |     assembly.
                | 
                |     Parameters:
                | 
                |         oListofHolder
                |             List of Holder. First, all elements in list are removed.

        :return: tuple
        """
        return self.com_object.GetHolders()

    def get_length_of_tool_assembly(self, islocal: bool, i_unit: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetLengthOfToolAssembly(boolean Islocal,long iUnit) As
                | double
                |     Returns the value of the total length of the tool
                |     assembly.
                | 
                |     Parameters:
                | 
                |         oToolAssemblyLength.
                |         Islocal:
                |             Local value save in Tool Configuration if is defined
                |             
                |         iUnit
                |             :

        :param bool islocal:
        :param int i_unit:
        :return: float
        """
        return self.com_object.GetLengthOfToolAssembly(islocal, i_unit)

    def get_list_holder_gage(
            self,
            o_listof_holder: tuple,
            o_list_holder_gage: tuple,
            islocal: bool,
            i_unit: int
    ) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub GetListHolderGage(CATSafeArrayVariant oListofHolder,CATSafeArrayVariant
                | oListHolderGage,boolean Islocal,long iUnit)
                |     Returns the list of holder associated with the tool assembly and the list
                |     of Gage
                |
                |     Parameters:
                |
                |         oListofHolder
                |             List of Holder. First, all elements in list are removed.
                |
                |         oListHolderGage
                |             List of Gage between each Holder. First, all elements in list are
                |             removed.
                |         Islocal:
                |             Local value save in Tool Configuration if is defined
                |
                |         iUnit
                |             :

        :param tuple o_listof_holder:
        :param tuple o_list_holder_gage:
        :param bool islocal:
        :param int i_unit:
        :return: None
        """
        return self.com_object.GetListHolderGage(o_listof_holder, o_list_holder_gage, islocal, i_unit)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'get_list_holder_gage'
        # vba_code = """
        # Public Function get_list_holder_gage(manufacturing_tool_assembly)
        #     Dim oListofHolder (2)
        #     manufacturing_tool_assembly.GetListHolderGage oListofHolder
        #     get_list_holder_gage = oListofHolder
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_tool_gage(self, islocal: bool, i_unit: int) -> float:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetToolGage(boolean Islocal,long iUnit) As double
                |     Returns the value of Gage between Tool and First Holder.
                | 
                |     Parameters:
                | 
                |         oToolGage.
                |         Islocal:
                |             Local value save in Tool Configuration if is defined
                |             
                |         iUnit
                |             :

        :param bool islocal:
        :param int i_unit:
        :return: float
        """
        return self.com_object.GetToolGage(islocal, i_unit)

    def get_tools(self) -> tuple:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Func GetTools() As CATSafeArrayVariant
                |     Returns the list of tool associated with the tool
                |     assembly.
                | 
                |     Parameters:
                | 
                |         oListofHolder
                |             List of Holders. First, all elements in list are removed.

        :return: tuple
        """
        return self.com_object.GetTools()

    def remove_all_components(self) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveAllComponents()
                |     Remove all the components of tool assembly.

        :return: None
        """
        return self.com_object.RemoveAllComponents()

    def remove_component(self, i_component: AnyObject) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub RemoveComponent(AnyObject iComponent)
                |     Removes a component of tool assembly.
                | 
                |     Parameters:
                | 
                |         iComponent:
                |             PLM object to remove

        :param AnyObject i_component:
        :return: None
        """
        return self.com_object.RemoveComponent(i_component.com_object)

    def set_list_holder_gage(self, i_list_holder_gage: tuple, islocal: bool, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2026-02-08 14:05:01.675948))
                | Sub SetListHolderGage(CATSafeArrayVariant iListHolderGage,boolean Islocal,long
                | iUnit)
                |     Sets the list of holder gage associated to the tool
                |     assembly
                |
                |     Parameters:
                |
                |         iListHolderGage
                |             List of Gage between each Holder. First, all elements in list are
                |             removed.
                |         Islocal:
                |             Local value save in Tool Configuration if is defined
                |
                |         iUnit
                |             :

        :param tuple i_list_holder_gage:
        :param bool islocal:
        :param int i_unit:
        :return: None
        """
        return self.com_object.SetListHolderGage(i_list_holder_gage, islocal, i_unit)
        # todo: check this method, does it require system service?
        # Autogenerated comment:
        # some methods require a system service call as the methods expects a vb array object
        # passed to it and there is no way to do this directly with python. In those cases the following code
        # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # vba_function_name = 'set_list_holder_gage'
        # vba_code = """
        # Public Function set_list_holder_gage(manufacturing_tool_assembly)
        #     Dim iListHolderGage (2)
        #     manufacturing_tool_assembly.SetListHolderGage iListHolderGage
        #     set_list_holder_gage = iListHolderGage
        # End Function
        # """

        # system_service = SystemService(self.application.SystemService)
        # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_tool_gage(self, o_tool_gage: float, islocal: bool, i_unit: int) -> None:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Sub SetToolGage(double oToolGage,boolean Islocal,long iUnit)
                |     Set the value of Gage between Tool and First Holder.
                | 
                |     Parameters:
                | 
                |         iToolGage
                |             : Gage between Tool and First Holder 
                |         Islocal:
                |             Local value save in Tool Configuration if is defined
                |             
                |         iUnit
                |             :

        :param float o_tool_gage:
        :param bool islocal:
        :param int i_unit:
        :return: None
        """
        return self.com_object.SetToolGage(o_tool_gage, islocal, i_unit)

    def __repr__(self):
        return f'ManufacturingToolAssembly(name="{self.name}")'
