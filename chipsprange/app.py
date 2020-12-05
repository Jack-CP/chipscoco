# 实现一个简单的商城购物系统
from bll import handles
from dal import shopping_goods_data


def shopping():


    prompt = "您好，欢迎使用薯条橙子在线购物系统chipscoco，输入<>中对应的指令来使用购物系统:\n" \
             "<1>:查看所有商品\n<2>:对商品按售价进行排序(asc表示升序，desc表示降序)\n" \
             "<3>:添加商品到购物车\n<4>:查看购物车\n<5>:删除购物车指定商品\n<6>:下单结账\n<0>:退出系统"

    commands = {1: handles.show_all_goods, 2: handles.sort_goods, 3: handles.add_goods, 4: handles.show_shopping_cart,
                5: handles.remove_goods, 6: handles.shopping_cart_paybill }
    # commands 是数字编号+函数的内存地址

    while True:
        print(prompt)
        command = int(input("输入指令:__\b\b"))
        if command in commands:
            commands[command](shopping_goods_data.CHIPSCOCO)
            # 因为把 shopping_goods_data 作为模块分出去以后，这里再调用chipscoco就要
            # 加上模块名了
        elif command == 0:
            break
        else:
            print("您输入了非法的指令")
        input("按下键盘任意键，继续使用系统......")


if __name__ == "__main__":
    shopping()
