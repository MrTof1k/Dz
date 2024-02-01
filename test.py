import requests


def get_size_parms(json_response, address_ll):
    org_point = address_ll
    print("Размеры [1] (0.06)")
    delta1 = input()
    print("Размеры [2] (0.006)")
    delta2 = input()

    map_params = {
        "ll": address_ll,
        "spn": ",".join([delta1, delta2]),
        "l": "map",
        "pt": "{},pm2dgl".format(org_point)
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    return response
