from typing import Union

from pycatia3dx.dnb_fitting.fitting_service import FittingService
from pycatia3dx.dnb_igp_olp_use.calib_least_squares_service import CalibLeastSquaresService
from pycatia3dx.dnb_igp_olp_use.olp_download_service import OLPDownloadService
from pycatia3dx.dnb_igp_olp_use.olp_teach_helper import OLPTeachHelper
from pycatia3dx.dnb_igp_olp_use.olp_translator_helper import OLPTranslatorHelper
from pycatia3dx.dnb_igp_olp_use.olp_upload_service import OLPUploadService
from pycatia3dx.drafting.drawing_gen_service import DrawingGenService
from pycatia3dx.electrical.elec_import_finalizer_service import ElecImportFinalizerService
from pycatia3dx.fc_board.fcb_service import FcbService
from pycatia3dx.interfaces.player_services import PlayerServices
from pycatia3dx.interfaces.service import Service
from pycatia3dx.interfaces.visu_services import VisuServices
from pycatia3dx.knowledge_interfaces.knowledge_services import KnowledgeServices
from pycatia3dx.material.matplm_service import MatplmService
from pycatia3dx.measure.measurable_service import MeasurableService
from pycatia3dx.measure.measure_service import MeasureService
from pycatia3dx.opns_inertial.inertia_box_service import InertiaBoxService
from pycatia3dx.opns_inertial.inertia_service import InertiaService
from pycatia3dx.opns_section.section_service import SectionService
from pycatia3dx.pcb_board.pcb_service import PcbService
from pycatia3dx.plm_access.plm_script_service import PLMScriptService
from pycatia3dx.plm_access.plm_search_service import PLMSearchService
from pycatia3dx.plm_access.search_service import SearchService
from pycatia3dx.plm_application_context.plm_app_context import PLMAppContext
from pycatia3dx.plm_application_context.plm_refresh_service import PLMRefreshService
from pycatia3dx.plm_application_context.pn_o_service import PnOService
from pycatia3dx.plm_document.plm_document_services import PLMDocumentServices
from pycatia3dx.plm_interference.interference_services import InterferenceServices
from pycatia3dx.plm_session_builder.plm_new_service import PLMNewService
from pycatia3dx.plm_session_builder.plm_open_service import PLMOpenService
from pycatia3dx.plm_session_builder.plm_propagate_service import PLMPropagateService
from pycatia3dx.plm_simulation_engine.sim_dyn_clash_services import SimDynClashServices
from pycatia3dx.plm_validation.val_validation_service import VALValidationService
from pycatia3dx.sim_plm.sim_plm_service import SimPLMService
from pycatia3dx.sim_plm.sim_simulation_service import SimSimulationService
from pycatia3dx.sim_rep.sim_link_services import SimLinkServices
from pycatia3dx.sim_rep.sim_publication_services import SimPublicationServices
from pycatia3dx.sim_rep.sim_rep_services import SimRepServices
from pycatia3dx.sma_mpa_foundation.sim_execution_service import SimExecutionService
from pycatia3dx.sma_mpa_foundation.sim_initialization_service import SimInitializationService
from pycatia3dx.space_reference_system.rfg_service import RfgService
from pycatia3dx.space_reference_system.srs_instantiate_service import SrsInstantiateService
from pycatia3dx.structure.str_service import StrService

AnyService = Union[
    CalibLeastSquaresService,
    DrawingGenService,
    ElecImportFinalizerService,
    FcbService,
    FittingService,
    InertiaBoxService,
    InertiaService,
    InterferenceServices,
    KnowledgeServices,
    MatplmService,
    MeasurableService,
    MeasureService,
    OLPDownloadService,
    OLPTeachHelper,
    OLPTranslatorHelper,
    OLPUploadService,
    PLMAppContext,
    PLMDocumentServices,
    PLMNewService,
    PLMOpenService,
    PLMPropagateService,
    PLMRefreshService,
    PLMScriptService,
    PLMSearchService,
    PcbService,
    PlayerServices,
    PnOService,
    RfgService,
    SearchService,
    SectionService,
    SimDynClashServices,
    SimExecutionService,
    SimInitializationService,
    SimLinkServices,
    SimPLMService,
    SimPublicationServices,
    SimRepServices,
    SimSimulationService,
    SrsInstantiateService,
    StrService,
    VALValidationService,
    VisuServices,
]

service_types = {
    'Service': {
        'type': Service
    },
    'CalibLeastSquaresService': {
        'type': CalibLeastSquaresService
    },
    'DrawingGenService': {
        'type': DrawingGenService
    },
    'ElecImportFinalizerService': {
        'type': ElecImportFinalizerService
    },
    'FittingService': {
        'type': FittingService
    },
    'FcbService': {
        'type': FcbService
    },
    'InertiaBoxService': {
        'type': InertiaBoxService
    },
    'InertiaService': {
        'type': InertiaService
    },
    'InterferenceServices': {
        'type': InterferenceServices
    },
    'KnowledgeServices': {
        'type': KnowledgeServices
    },
    'MatplmService': {
        'type': MatplmService
    },
    'MeasurableService': {
        'type': MeasurableService
    },
    'MeasureService': {
        'type': MeasureService
    },

    'OLPDownloadService': {
        'type': OLPDownloadService
    },

    'OLPTeachHelper': {
        'type': OLPTeachHelper
    },
    'OLPTranslatorHelper': {
        'type': OLPTranslatorHelper
    },
    'OLPUploadService': {
        'type': OLPUploadService
    },

    'PLMAppContext': {
        'type': PLMAppContext
    },
    'PLMDocumentServices': {
        'type': PLMDocumentServices
    },
    'PLMNewService': {
        'type': PLMNewService
    },
    'PLMOpenService': {
        'type': PLMOpenService
    },
    'PLMPropagateService': {
        'type': PLMPropagateService
    },
    'PLMRefreshService': {
        'type': PLMRefreshService
    },
    'PLMScriptService': {
        'type': PLMScriptService
    },
    'PLMSearchService': {
        'type': PLMSearchService
    },

    'PcbService': {
        'type': PcbService
    },
    'PlayerServices': {
        'type': PlayerServices
    },
    'PnOService': {
        'type': PnOService
    },

    'RfgService': {
        'type': RfgService
    },

    'SearchService': {
        'type': SearchService
    },
    'SectionService': {
        'type': SectionService
    },

    'SimDynClashServices': {
        'type': SimDynClashServices
    },
    'SimExecutionService': {
        'type': SimExecutionService
    },
    'SimInitializationService': {
        'type': SimInitializationService
    },
    'SimLinkServices': {
        'type': SimLinkServices
    },
    'SimPLMService': {
        'type': SimPLMService
    },
    'SimPublicationServices': {
        'type': SimPublicationServices
    },
    'SimRepServices': {
        'type': SimRepServices
    },
    'SimSimulationService': {
        'type': SimSimulationService
    },

    'SrsInstantiateService': {
        'type': SrsInstantiateService
    },
    'StrService': {
        'type': StrService
    },
    'VALValidationService': {
        'type': VALValidationService
    },
    'VisuServices': {
        'type': VisuServices
    },
}
