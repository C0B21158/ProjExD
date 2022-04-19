import random

def shutudai():
    qa = random.choice(list(qa_dict.items()))
    print(qa[0])
    return qa[1]


def kaitou(a_list):
    kai = input("答えを入力してください：")
    print("入力をした答えは：",kai)
    if kai in a_list:
        print("正解だお")
    else:
        print("不正解です")

if __name__ == "__main__":
    qa_dict = {
        "サザエの旦那の名前は？":["マスオ", "ますお"],
        "カツオの妹の名前は？":["ワカメ","わかめ"],
        "タラオはカツオから見てどんな関係？":["おい","甥","甥っ子","おいっこ"]
    }

    
    a_list = shutudai()
    kaitou(a_list)

