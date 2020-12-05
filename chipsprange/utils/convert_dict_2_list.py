def convert_dict_2_list(data):
    """
    :param data: a dict of  goods,  e.g:{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        },
    :return: a list of goods , e.g:[{"id": 1, "name": "洗发水", "price": 22}]
    """

    goods = []
    for _ in data:
        goods.append({"id": _, "name": data[_]["name"], "price": data[_]["price"],"count":data[_]["count"]})

    return goods
