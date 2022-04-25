# from flask import current_app


# def test_prcoess_new_mr(app, client):
#     # Тест не рабочий, разобраться с тем достать переменную окружения
#     # Тест не должен отправлять запрос к апи на присвоение ревьюера
#     with app.app_context():
#         reviewer = current_app.config['REVIEWER_ID']
#         response = client.post(
#             '/new_mr',
#             headers={'X-Gitlab-Event': 'Merge Request Hook'},
#             json={'id': 14, 'project_id': 131110, 'reviewer_ids': [reviewer]},
#         )
#         # test fails since webhook doesn't return any response
#         # however the reviewer is assigned
#         assert response.status_code == 201
