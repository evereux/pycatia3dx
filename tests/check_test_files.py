import os
import sys

sys.path.insert(0, os.path.abspath("..\\pycatia3dx"))

from pycatia3dx import catia3dx
from pycatia3dx.plm_access.search_service import SearchService
from tests.create_test_parts import create_test_part_one
from tests.test_part_parameters import TEST_CATPART_ONE
from tests.test_part_parameters import TEST_CATPART_ONE_DESCRIPTION
from tests.test_part_parameters import TEST_CATDRAWING_ONE
from tests.test_part_parameters import TEST_CATDRAWING_ONE_DESCRIPTION
from tests.test_part_parameters import TEST_VPMREFERENCE_ONE
from tests.test_part_parameters import TEST_VPMREFERENCE_ONE_DESCRIPTION
from tests.create_test_drawings import create_test_drawing_one
from tests.conftest import check_open_documents

application = catia3dx()


def file_exists_or_latest(base_type: str, file_name: str, file_description: str):
    search_service: SearchService = application.get_session_service("Search")
    db_search = search_service.database_search
    db_search.base_type = base_type
    db_search.add_easy_criteria("V_Name", file_name)
    search_service.search()
    if len(db_search.results) == 0:
        return False
    else:
        result_first = db_search.results[0]
        if result_first.get_attribute_value('V_description') != file_description:
            raise OSError(
                f'Test file "{file_name}" is out of date. {result_first.get_attribute_value('V_description')} != {file_description} Please delete and re-run this script.')
        else:
            return True


def check_test_files():
    application.logger.info('Checking test files exist.')

    if not file_exists_or_latest('3DShape', TEST_CATPART_ONE, TEST_CATPART_ONE_DESCRIPTION):
        create_test_part_one(application)
    else:
        application.logger.info(f'Test file "{TEST_CATPART_ONE}" OK.')

    if not file_exists_or_latest('VPMReference', TEST_VPMREFERENCE_ONE, TEST_VPMREFERENCE_ONE_DESCRIPTION):
        application.logger.warning(
            f'Tests cannot continue. Please manually create the VPMReference "{TEST_VPMREFERENCE_ONE}" and attach the 3DShape "{TEST_CATPART_ONE}". '
            f'VPMReference can not be manually created due to licensing restrictions.')
        sys.exit()
    else:
        application.logger.info(f'Test file "{TEST_VPMREFERENCE_ONE}" OK.')

    # # Drawing
    if not file_exists_or_latest('Drawing', TEST_CATDRAWING_ONE, TEST_CATDRAWING_ONE_DESCRIPTION):
        create_test_drawing_one(application)
    else:
        application.logger.info(f'Test file "{TEST_CATDRAWING_ONE}" OK.')

    # finished
    application.logger.info('Test files created.')


if __name__ == '__main__':
    # run this script before running the test suite to create the reference files.
    check_open_documents()
    check_test_files()
