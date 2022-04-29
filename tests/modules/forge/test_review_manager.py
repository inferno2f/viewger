import pytest
from pytest_mock import MockerFixture

from app.modules.forge.review_manager import ReviewManager


@pytest.mark.parametrize("mr_id, reviewer_id", zip(range(1, 11), range(10, 0, -1)))
def test_assign_reviewer(app, mocker: MockerFixture, mr_id, reviewer_id):
    project_mock = mocker.MagicMock()
    get_projects_mock = mocker.MagicMock(return_value=project_mock)
    project_mrs_manager_mock = mocker.MagicMock()
    mr_mock = mocker.MagicMock()
    get_mr_mock = mocker.MagicMock(return_value=mr_mock)
    mr_manager_mock = mocker.MagicMock()
    update_mr_mock = mocker.MagicMock()
    mr_get_id_mock = mocker.MagicMock(return_value=mr_id)
    mocker.patch('app.gitlab_client.projects.get', new=get_projects_mock)
    mocker.patch.object(project_mock, 'mergerequests', new=project_mrs_manager_mock)
    mocker.patch.object(project_mrs_manager_mock, 'get', new=get_mr_mock)
    mocker.patch.object(mr_mock, 'get_id', new=mr_get_id_mock)
    mocker.patch.object(mr_mock, 'manager', new=mr_manager_mock)
    mocker.patch.object(mr_manager_mock, 'update', new=update_mr_mock)

    rm = ReviewManager()
    rm.assign_reviewer(None, mr_id, reviewer_id)

    update_mr_mock.assert_called_once_with(mr_id, {'reviewer_ids': [reviewer_id]})


@pytest.mark.parametrize("reviewer_id", range(10))
def test_select_reviewer_for_mr(create_configured_app, reviewer_id):
    app = create_configured_app({'REVIEWER_ID': reviewer_id})
    rm = ReviewManager()

    with app.app_context():
        assert rm.select_reviewer_for_mr() == app.config['REVIEWER_ID']
