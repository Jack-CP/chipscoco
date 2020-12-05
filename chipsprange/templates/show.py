
def show(goods, flag = 0):
    """
    :param goods: goods table, e.g:{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},1

        }, or [{"id": 1, "name": "洗发水", "price": 22}, ]
    :return:
    """
    tr = "+"+"-"*5+"+"+"-"*16+"+"+"-"*10+"+"+"-"*10+"+"
    heading = "|{:^5s}|{:^13s}|{:^8s}|{:^8s}|".format("id", "商品名", "售价","数量")

    print(tr+"\n"+heading+"\n"+tr)
    if flag == 0:
        for id_ in goods:
            print("|{0:^5s}|{1:{4}^8s}|{2:^10s}|{3:^10s}|".format(str(id_), goods[id_]["name"],
                                                     str(goods[id_]["price"]),str(goods[id_]["count"]),
                                                                  chr(12288)))
    else:
        for item in goods:
            print("|{0:^5s}|{1:{4}^8s}|{2:^10s}|{3:^10s}|".format(str(item["id"]), item["name"],
                                                         str(item["price"]),str(item["count"]),chr(12288)))
    print(tr)
