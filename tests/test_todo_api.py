from helpers.funcs import new_task_payload, create_task, get_task, update_task, list_tasks, delete_task

# def test_can_call_endpoint():
#     response = requests.get(ENDPOINT)
#     assert response.status_code == 200, "Status code is not 200" 

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200, "Status code is not 200"

    data = create_task_response.json()
    task_id = data['task']['task_id']
    get_task_response = get_task(task_id)
    
    assert get_task_response.status_code == 200, "get task response status code is not 200"
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == payload["content"]
    assert get_task_data['user_id'] == payload["user_id"] 



def test_can_update_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    task_id = create_task_response.json()['task']['task_id']
    # update a task 
    new_payload = {
        'user_id': payload['user_id'],
        'task_id': task_id,
        'content': 'my updated content',
        'is_done': True,
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200 
    # get and validate the changes 
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data['content'] == new_payload['content']
    assert get_task_data['is_done'] == new_payload['is_done']
    

def test_can_list_tasks():
    n = 10
    payload = new_task_payload()
    for _ in range(n):
        create_task_response = create_task(payload)
        assert create_task_response.status_code == 200
    user_id = payload['user_id']
    list_tasks_response = list_tasks(user_id)
    assert list_tasks_response.status_code == 200
    data = list_tasks_response.json()
    tasks = data['tasks']
    assert len(tasks) == n
    # print(data)


def test_can_delete_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()['task']['task_id']
    
    # delete a task
    delete_task_response = delete_task(task_id)
    assert delete_task_response.status_code == 200 

    # get the task and check that it is not found
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 404
    # print(get_task_response.status_code)
    # pass