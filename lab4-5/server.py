import json
import re

from aiohttp import web

# + PUT /labs?lab_name=lab1&deadline=21.08.2001 - добавить лабу
# + GET /labs - посмотреть лабы
# + GET /labs/lab1 - посмотреть лабу
# - PUT /labs/lab1?deadline=21.08.2001 - добавить в лабу
# + DELETE /labs/lab1 - удалить лабу

routes = web.RouteTableDef()
labs = dict()

# {
#     "lab_name": {
#         "deadline": ""
#     },
#     ...
# }


def check_deadline(deadline):
    if not re.fullmatch(r'\d{1,2}.\d{1,2}.\d{4}', deadline):
        return False
    return True


def add_lab(lab_name, deadline=None):
    reason = "OK"
    lab = {}

    if deadline is not None:
        isDataCorrect = check_deadline(deadline)
        if not isDataCorrect:
            reason = "Некорректная дата!"
        lab["deadline"] = deadline

    labs[lab_name] = lab
    return reason


def remove_lab(lab_name):
    labs.pop(lab_name)


def find_lab(lab_name):
    return labs.get(lab_name)


def set_deadline(lab_name, deadline):
    labs[lab_name]["deadline"] = deadline

#
#
#


@routes.put('/labs')
async def create_lab(request):
    lab_name = request.query['lab_name']
    print("Creating new lab with name: ", lab_name)

    lab = find_lab(lab_name)
    status = 200
    if lab is None:
        deadline = None
        if "deadline" in request.query:
            deadline = request.query['deadline']
        reason = add_lab(lab_name, deadline)
    else:
        status = 201
        reason = "Лабораторная работа с таким названием уже существует!"

    response_obj = {'status': 'success', 'link': f'http://localhost:8080/labs/{lab_name}', "labs": labs}
    return web.Response(text=json.dumps(response_obj), status=status, reason=reason)


@routes.get('/labs')
async def get_all_labs(request):
    response_obj = {'status': 'success', 'labs': labs}
    return web.Response(text=json.dumps(response_obj))


@routes.get('/labs/{lab_name}')
async def get_lab_info(request):
    try:
        lab_name = request.match_info.get('lab_name')
        lab = find_lab(lab_name)

        status = 200
        if lab is None:
            response_obj = {'status': 'failed'}
            status = 201
        else:
            response_obj = {'status': 'success', lab_name: lab, "labs": labs}

        return web.Response(text=json.dumps(response_obj), status=status)

    except Exception as e:
        response_obj = {'status': 'failed', 'reason': str(e)}
        return web.Response(text=json.dumps(response_obj), status=500)


@routes.get('/labs')
async def get_all_lab(request):
    status = 404
    reason = "На сервере нет лабораторных"
    labs_data = {}
    if len(labs) > 0:
        status = 200
        reason = "OK"
        for name, lab_data in labs.items():
            lab = {"deadline": lab_data["deadline"], "labs": labs}
            labs_data[name] = lab

    return web.Response(text=json.dumps(labs_data), status=status, reason=reason)


@routes.put('/labs/{lab_name}')
async def change_lab(request):
    lab_name = request.match_info["lab_name"]
    lab = find_lab(lab_name)

    reason = ""
    status = 200

    if lab is None:
        status = 400
        reason = "Такая лабораторная ещё не создана!"

    deadline = None
    if "deadline" in request.query:
        deadline = request.query['deadline']
    else:
        status = 400

    if status != 400:
        reason = change_lab_param(lab_name, deadline)

    text = {"labs": labs}

    return web.Response(text=text, status=status, reason=reason)


def change_lab_param(lab_name, deadline):
    if deadline is None:
        return "Отсутсвует параметр deadline!"

    labs[lab_name]["deadline"] = deadline

    return "OK"


@routes.delete('/labs/{lab_name}')
async def delete_lab(request):
    lab_name = request.match_info["lab_name"]

    status = 201
    reason = "Такой лаборатоной нет на сервере"

    if lab_name in labs:
        status = 200
        reason = "OK"
        labs.pop(lab_name)

    text = {"labs": labs}

    return web.Response(text=text, status=status, reason=reason)


app = web.Application()
app.router.add_routes(routes)
web.run_app(app)
