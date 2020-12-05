from templates import show
from utils import convert_dict_2_list
from dal import shopping_goods_data


def show_all_goods(chipscoco):
    """
       :param chipscoco: a dict object indicates online shopping system chipscoco,
       e.g:{
        "goods":{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        },
        "shopping_cart":{"洗发水": 22}
       }
       :return:
    """
    print("以下是商城中的所有商品:")
    show.show(chipscoco["goods"])


def sort_goods(chipscoco):
    """
       :param chipscoco: a dict object indicates online shopping system chipscoco,
       e.g:{
        "goods":{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        },
        "shopping_cart":{"洗发水": 22, }
       }
       :return:
    """
    goods = convert_dict_2_list.convert_dict_2_list(chipscoco["goods"])
    data_size = len(goods)
    command = input("您好，输入指令<asc>对商品按售价进行升序排序，"
                    "输入指令<desc>对商品按售价进行降序排序:____\b\b\b\b")
    if command.lower() == "asc":
        for index_outer in range(data_size-1):
            for index_inner in range(data_size-1-index_outer):
                if goods[index_inner]["price"] > goods[index_inner+1]["price"]:
                    goods[index_inner], goods[index_inner+1] =\
                        goods[index_inner+1], goods[index_inner]

        show.show(goods, flag=1)
    elif command.lower() == "desc":
        for index_outer in range(data_size-1):
            for index_inner in range(data_size-1-index_outer):
                if goods[index_inner]["price"] < goods[index_inner+1]["price"]:
                    goods[index_inner], goods[index_inner+1] =\
                        goods[index_inner+1],goods[index_inner]
        show.show(goods,flag=1)

    else:
        print("您输入的指令有误！")


def add_goods(chipscoco):
    """
       :param chipscoco: a dict object indicates online shopping system chipscoco,
       e.g:{
        "goods":{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        },
        "shopping_cart":{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        }
       :return:
    """
    id_ = int(input("请输入商品id:__\b\b"))
    # 添加重复商品
    # count = 0
    if id_ in chipscoco["goods"] and id_ not in chipscoco["shopping_cart"]:
        chipscoco["shopping_cart"][id_] = {"name": chipscoco["goods"][id_]["name"],
                                           "price":  chipscoco["goods"][id_]["price"],
                                           "count":  chipscoco["goods"][id_]["count"]}
        print("您好，已将商品{}加入购物车".format(chipscoco["goods"][id_]["name"]))
    elif id_ in chipscoco["shopping_cart"]:
        # count = count + 1
        # chipscoco["shopping_cart"]["count"] = chipscoco["shopping_cart"]["count"]+1
        # 因为忘了字典的格式，所以没有加上 [id_]
        chipscoco["shopping_cart"][id_]["count"] = chipscoco["shopping_cart"][id_]["count"]+1
        how_many = chipscoco["shopping_cart"][id_]["count"]
        print("您好，您已经第{}次加入{}商品".format(how_many,chipscoco["shopping_cart"][id_]["name"]))

    else:
        print("您输入的商品编号有误！")


def remove_goods(chipscoco):
    """

    :param chipscoco:
    :return: 删除购物车指定商品
    """
    id_ = int(input("您真的要删除购物车已添加的商品id吗：__\b\b"))
    # print(chipscoco)
    if id_ in chipscoco["shopping_cart"]:

        # id_ = chipscoco["shopping_cart"].pop("id_")
        # chipscoco["shopping_cart"].pop("id_") 把变量 id_ 写成字符串"id_"了。
        chipscoco["shopping_cart"].pop(id_)
        print("您已删除购物车里添加的商品")
    else:
        print("您输入的商品有误")


def show_shopping_cart(chipscoco):
    """
       :param chipscoco: a dict object indicates online shopping system chipscoco,
       e.g:{
        "goods":{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        },
        "shopping_cart":{
            1: {"name": "洗发水", "price": 22},
            2: {"name": "牙膏", "price": 15},
        }
       :return:
    """
    if not chipscoco["shopping_cart"]:
        print("您的购物车为空!")
        # 上面两行表示购物车结账之后为空的情况
    else:
        print("这是您的购物清单:")
        show.show(chipscoco["shopping_cart"])


def shopping_cart_paybill(chipscoco):
    """

    :param chipscoco:
    :return:
    """
    # id_ = int(input("请输入商品id:__\b\b"))

    single_price = sum_price = 0
    # for id_ in chipscoco["shopping_cart"]:
    #     sum_price = sum_price + ["shopping_cart"][id_]["price"]
    #     print("您的购物总额为 {} 元".format(sum_price))
    # else:
    #     print("您的购物车空空如也！")
    numbers = list(chipscoco["shopping_cart"])
    for id_ in numbers:
    # 小梁的新思路：构建一个新列表，只包含键名 编号。然后在列表中循环。


        # if id_ in chipscoco["shopping_cart"]:
            single_price = chipscoco["shopping_cart"][id_]["price"] * chipscoco["shopping_cart"][id_]["count"]
            sum_price = sum_price + single_price
    chipscoco["shopping_cart"].clear()
    print("您的购物总额为 {} 元".format(sum_price))