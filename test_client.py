import requests
import datetime


def test_all():
    create_1st_cat = requests.post('http://127.0.0.1:8000/categories',
                                   params={"cat": "yoga"})
    assert create_1st_cat.ok

    id_1 = create_1st_cat.json()["id"]

    create_2st_cat = requests.post('http://127.0.0.1:8000/categories',
                                   params={"cat": "study"})
    assert create_2st_cat.ok

    id_2 = create_2st_cat.json()["id"]
    # print(id_1, id_2)

    all_categories = requests.get('http://127.0.0.1:8000/categories')
    # print(all_categories.json())

    create_1st_task = requests.post('http://127.0.0.1:8000/tasks',
                                    json={
                                        "text": "go to yoga class",
                                        "create_habit": True,
                                        "category": id_1,
                                        "start": datetime.datetime(
                                            2023, 5, 25, 15, 00).isoformat(),
                                        "end": '2023-05-25T16:30:00+00:00'
                                    })
    # print(create_1st_task.text, flush=True)

    assert create_1st_task.ok

    task1_id = create_1st_task.json()["id"]

    create_2st_task = requests.post('http://127.0.0.1:8000/tasks',
                                    json={
                                        "text": "preparation to IELTS",
                                        "create_habit": True,
                                        "category": id_2,
                                        "start": datetime.datetime(
                                            2023, 5, 25, 10, 00).isoformat(),
                                        "end": '2023-05-25T12:30:00+00:00'
                                    })
    # print(create_2st_task.text, flush=True)
    assert create_2st_task.ok

    cats = requests.get('http://127.0.0.1:8000/categories')
    assert cats.ok

    # print(tasks.text)

    finish_1st = requests.post(f'http://127.0.0.1:8000/tasks/{task1_id}/done',
                               json={
        "start": '2023-05-25T16:30:00+00:00',
        "end": '2023-05-25T18:30:00+00:00'
    })
    print(finish_1st.text, flush=True)
    assert finish_1st.ok

    tasks = requests.get('http://127.0.0.1:8000/tasks')
    assert tasks.ok

    print(cats.text)
    print(tasks.text)
