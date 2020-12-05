import math

WEB_PAGES1 = """hit girl，正义联盟中的成员，在联盟中排行第五，她是一个内心善良又极富正义感的战斗天使。
"""


WEB_PAGES2 = """正义联盟中的hit girl, 从小就爱乐于助人，匡扶正义。人人都喜欢hit girl。
"""


WEB_PAGES3 = """科洛·莫瑞兹出生于1997年2月10日，她8岁便开始涉足影坛。
科洛年纪虽小，作品却不少，她的从影生涯始于2003年。。
"""


def calc_max_length(dictionary):
    """

    :param dictionary: an object of set, indicates all of the keywords. e.g
    :return: the max length of keyword
    """
    max_length = 1
    for _ in dictionary:
        if len(_) > max_length:
            max_length = len(_)
    return max_length


def cut(text,dictionary, max_split_width):
    """

    :param text: a text to be cut,e.g:"科洛·莫瑞兹出生于1997年2月10日，她8岁便开始涉足影坛。
科洛年纪虽小，作品却不少，她的从影生涯始于2003年。。"
    :param dictionary: an object of set, indicates all of the keywords. e.g.: {"正义", "hit girl"}
    :param max_split_width:
    :return:
    """


    keywords = {}
    words_size = 0
    while text:
        # 这里的range函数是生成一个倒排序列，例如6,5,4,3,2,1
        for index in range(max_split_width, 0, -1):
            # 对文本按最大宽度进行切片
            keyword = text[:index]
            # 如果切片分出来的词语在词典集合中，就保存到列表words变量中，并且退出for循环
            # 在集合中进行快速查找
            if keyword in dictionary:
                words_size += 1
                keywords[keyword] = 1 if keyword not in keywords else keywords[keyword] + 1
                text = text[index]
                break
        else:
            text = text[1:]
    return keywords, words_size


def build_inverse_index_table(web_pages, dictionary):
    """

    :param web_pages: an object of list, e.g.:["", ""]
    :param dictionary: an object of set, indicates all of the keywords. e.g.: {"正义", "hit girl"}
    :return: an object of dict, e.g.:{
     "正义" : [{"tf":xxx, "idf":xxx, "tfidf": xxx, "content": ""}]
    }
    """

    inverse_index_table = {}
    web_pages_size = len(web_pages)
    max_split_width = calc_max_length(dictionary)
    """
      在for循环中逐一遍历列表中的网页，内置函数enumerate可以返回列表的索引和值
    假设列表为['a','b','c'] 
    那么在for循环中通过enumerate函数遍历出的为如下索引值对:
    索引0，值'a',索引1，值'b'，索引2，值'c'，其它的同理
    """

    for index, web_pages in enumerate(web_pages):
        terms, terms_size = cut(web_pages, dictionary, max_split_width)
        for term in terms:
            # 计算term的 tf 值
            tf = round(terms[term] / terms_size, 4)
            page = {"content":web_page, "tf": tf}
            if term not in inverse_index_table:
                inverse_index_table[term] = [page]
                continue

                # 如果term 已存在于倒排表中，那么当前的term 肯定是其他网页的term
                # 其他网页的term 被添加进列表中，方便后续计算tf-idf
                inverse_index_table[term].append(page)


    for _, pages in inverse_index_table.items():
        terms_in_docs_length = len(pages)

        for page in pages:
            # 计算 term的 idf和 tf-idf 值
            page["idf"] = round(math.log10(web_pages_size / ters_in_docs_length), 4)
            page["tfidf"] = page["tf"] * page["idf"]

    return inverse_index_table


def search():
    # 定义词典，用来保存分词的词语，读者也可以自行扩充其他的词语
    dictionary = {"科洛·莫瑞兹", "hit girl", "正义"}
    max_split_width = calc_max_length(dictionary)

    web_pages = [WEB_PAGES1, WEB_PAGES2, WEB_PAGES3]
    inverse_index_table = build_inverse_index_table(web_pages, dictionary)
    prompt = "您好，欢迎使用薯条橙子在线搜索引擎chipscoco"
    print(prompt)

    while True:
        query = input("薯条一下："+"_"*10+"\b"*10)
        keywords, _ = cut(query, dictionary, max_split_width)
        for keyword in keywords:
            pages = inverse_index_table.get(keyword, [])
            if pages:
                pages = sorted(pages, key = lambda page: page["tfidf"], reverse= True)
                print("chipscoco为您找到相关结果约{}个".format(len(pages)))
                for page in pages:
                    print("{}...\n".format(page["content"][:30])+"_")






if __name__ == '__main__':
