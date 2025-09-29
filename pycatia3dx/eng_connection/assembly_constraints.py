"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.eng_connection.assembly_constraint import AssemblyConstraint
from pycatia3dx.system.collection import Collection


class AssemblyConstraints(Collection):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.Collection
                |                     AssemblyConstraints
                | 
                | Interface representing the collection of Assembly Constraint in an Engineering
                | Connection.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    def add(self, i_type: int, i_geometries: tuple) -> AssemblyConstraint:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090))
                | Func Add(CatAssemblyConstraintType iType,CATSafeArrayVariant iGeometries) As
                | AssemblyConstraint
                |     Adds an Assembly Constraint in the Engineering Connection.
                | 
                |     Parameters:
                | 
                |         iCstDef
                |             [in] The type of the Assembly Constraint. 
                |         iListOfGeometry
                |             [in] The list of geometry pointed by the constraint. The geometry
                |             is identified by a String :
                | 
                |             Here is the different formats accepted:
                |             "ProductInstance1.1/ProductInstance2.1" for Pointing an instance
                |             (Fix or FixInstanceInstance).
                |             "ProductInstance1.1/ProductInstance2.1/PublicationName" for
                |             pointing a PUBLICATION.
                |             "ProductInstance1.1/ProductInstance2.1/RepInstance1/GeometryName"
                |             for pointing a geometry.
                |             "RepInstance1.1/GeometryName" for "On rep"
                |             pointing.
                | 
                | 
                |             Each geometry must correspond, one to one, to a MCX's impacted. It
                |             means that the Impacted's Path of First Instances must be included in the
                |             geometry's Path of First Instances. 
                | 
                |     Returns:
                | 
                |         an Assembly Constraint
                |             if the operation is successful. 
                |         Nothing
                |             if the operation is failed. 
                | 
                |         A VB Error is raised if the creation failed.
                | 
                |     Func Item(CATVariant iIndex) As AssemblyConstraint
                |         Returns an Assembly Contraint.
                | 
                |         Parameters:
                | 
                |             I
                |                 [in] The index or name of the Assembly Contraint.
                |                 
                |             the index in the collection
                |                 if it is an Integer. 
                |             the name of the Assembly Contraint
                |                 if it is a String. 
                | 
                |     Sub Remove(AssemblyConstraint iEngConnection)
                |         Removes an Assembly Constraint defined in the Engineering
                |         Connection.
                | 
                |         Parameters:
                | 
                |             iAssConstraint
                |                 [in] Assembly Constraint to remove. 
                |             the index in the collection
                |                 if it is an Integer. 
                |             the name of the constraint
                |                 if it is a String. 
                |             the constraint to remove
                |                 if it is an AssemblyConstraint.

        :param int i_type:
        :param tuple i_geometries:
        :return: AssemblyConstraint
        """
        return AssemblyConstraint(self.com_object.Add(i_type, i_geometries))

    def __repr__(self):
        return f'AssemblyConstraints(name="{self.name}")'
