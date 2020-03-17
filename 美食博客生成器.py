import random
import preProcess


def 洗牌遍历(废话):
    池 = [j for i in 废话 for j in random.sample(i, 3)]
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素


def main():
    theme = input("请输入主题：")
    generator = preProcess.SentenceGenerator(theme)
    sentences = generator.main()
    方法 = sentences["方法"]  # 食物的制作方式
    称赞 = sentences["称赞"]  # 夸奖食物做得好
    下一句说明 = 洗牌遍历(方法)
    下一句称赞 = 洗牌遍历(称赞)

    tmp = random.sample(sentences["开头"], 1)[0]
    size = 400  # 文章长度
    cnt = 0  # 段落长度
    while len(tmp) < size:
        骰子 = random.randint(1, 6)  # 掷骰子决定下一句说什么
        阈值 = len(tmp)/size  # 控制说明出现的位置
        if 骰子 < 2*(1-阈值):
            tmp += next(下一句说明)
        elif 骰子 < 6:
            tmp += next(下一句称赞)
        elif tmp[-1] != "\n":
            tmp += "\n\n"
            cnt = 0

        # 避免段落太长
        if cnt > 9:
            tmp += "\n\n"

    return tmp


if __name__ == "__main__":
    print(main())
