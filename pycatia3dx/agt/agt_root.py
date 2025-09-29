"""
    Module initially auto generated using DSYAutomation files from CATIA 3DX R2025x on 2025-09-28 13:20:20.191090

    .. warning::
        The notes denoted "3DEXPERIENCE Automation Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia3dx.agt.agt_connectors import AGTConnectors
from pycatia3dx.agt.agt_draught_stops import AGTDraughtStops
from pycatia3dx.agt.agt_fire_bridges import AGTFireBridges
from pycatia3dx.agt.agt_insulations import AGTInsulations
from pycatia3dx.agt.agt_sills import AGTSills
from pycatia3dx.agt.coverings import Coverings
from pycatia3dx.agt.walls import Walls
from pycatia3dx.system.any_object import AnyObject


class AGTRoot(AnyObject):
    """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)

                | SystemTS.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     AGTRoot
                | 
                | Object to AGTRoot.
                | To retrieve collection from part object.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.com_object = com_object

    @property
    def connectors(self) -> AGTConnectors:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Connectors() As AGTConnectors (Read Only)
                |     Returns the collection of Connector.
                | 
                |     Example:
                |         This example retrieves in Connector Collection from part
                |         object.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As AGTRoot
                |          Set MyRoot = MyRoot.GetItem("CATAGTRoot")
                |          Dim ConnectorCollection As AGTConnectors
                |          Set ConnectorCollection = MyRoot.Connectors

        :return: AGTConnectors
        """

        return AGTConnectors(self.com_object.Connectors)

    @property
    def coverings(self) -> Coverings:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Coverings() As Coverings (Read Only)
                |     Returns the collection of Covering.
                | 
                |     Example:
                |         This example retrieves in Covering Collection from part
                |         object.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As AGTRoot
                |          Set MyRoot = MyRoot.GetItem("CATAGTRoot")
                |          Dim CoveringCollection As Coverings
                |          Set CoveringCollection = MyRoot.Coverings

        :return: Coverings
        """

        return Coverings(self.com_object.Coverings)

    @property
    def draught_stops(self) -> AGTDraughtStops:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property DraughtStops() As AGTDraughtStops (Read Only)
                |     Returns the collection of DraughtStop.
                | 
                |     Example:
                |         This example retrieves in DraughtStop Collection from part
                |         object.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As AGTRoot
                |          Set MyRoot = MyRoot.GetItem("CATAGTRoot")
                |          Dim DraughtStopsCollection As AGTDraughtStops
                |          Set DraughtStopsCollection = MyRoot.DraughtStops

        :return: AGTDraughtStops
        """

        return AGTDraughtStops(self.com_object.DraughtStops)

    @property
    def fire_bridges(self) -> AGTFireBridges:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property FireBridges() As AGTFireBridges (Read Only)
                |     Returns the collection of FireBridge.
                | 
                |     Example:
                |         This example retrieves in FireBridge Collection from part
                |         object.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As AGTRoot
                |          Set MyRoot = MyRoot.GetItem("CATAGTRoot")
                |          Dim FireBridgesCollection As AGTFireBridges
                |          Set FireBridgesCollection = MyRoot.FireBridges

        :return: AGTFireBridges
        """

        return AGTFireBridges(self.com_object.FireBridges)

    @property
    def insulations(self) -> AGTInsulations:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Insulations() As AGTInsulations (Read Only)
                |     Returns the collection of insulation.
                | 
                |     Example:
                |         This example retrieves in Insulation Collection from part
                |         object.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As AGTRoot
                |          Set MyRoot = MyRoot.GetItem("CATAGTRoot")
                |          Dim InsulationCollection As AGTInsulations
                |          Set InsulationCollection = MyRoot.Insulations

        :return: AGTInsulations
        """

        return AGTInsulations(self.com_object.Insulations)

    @property
    def sills(self) -> AGTSills:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Sills() As AGTSills (Read Only)
                |     Returns the collection of Sill.
                | 
                |     Example:
                |         This example retrieves in Sill Collection from part
                |         object.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As AGTRoot
                |          Set MyRoot = MyRoot.GetItem("CATAGTRoot")
                |          Dim SillCollection As AGTSills
                |          Set SillCollection = MyRoot.Sills

        :return: AGTSills
        """

        return AGTSills(self.com_object.Sills)

    @property
    def walls(self) -> Walls:
        """
        .. note::
            :class: toggle

            3DEXPERIENCE Automation Help (2025-09-28 13:20:20.191090)
                | Property Walls() As Walls (Read Only)
                |     Returns the collection of Wall.
                | 
                |     Example:
                |         This example retrieves in Wall Collection from part
                |         object.
                | 
                |          Dim myPart As CATIAPart
                |          Set myPart = CATIA.ActiveEditor.ActiveObject
                |          Dim MyRoot As AGTRoot
                |          Set MyRoot = MyRoot.GetItem("CATAGTRoot")
                |          Dim WallsCollection As AGTWalls
                |          Set WallsCollection = MyRoot.Walls
                |          
                | 
                | 
                | Copyright © 1999-2024, Dassault Systèmes. All rights reserved.

        :return: Walls
        """

        return Walls(self.com_object.Walls)

    def __repr__(self):
        return f'AgtRoot(name="{self.name}")'
