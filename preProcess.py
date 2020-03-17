import random
import readJSON


class SentenceGenerator:
    def __init__(self, food):
        self.words = readJSON.read_json()
        self.sentences = {}
        self.food = food

    def add_periods(self):
        for key, val in self.sentences.items():
            self.sentences[key] = [v + "。" for v in val]

    def generator(self):
        self.sentences["开头"] = [self.food + i for i in self.words['begin']]
        self.sentences["容易"] = [i+"学会" for i in self.words['time']]
        self.sentences["方法-1"] = ["我家{}从不".format(self.food)+i+"着吃" for i in self.words['method']]
        self.sentences["方法-2"] = [self.food + "不用" + i for i in self.words['method']]
        self.sentences["方法-3"] = ["别再" + i + "着吃了" for i in self.words['method']]
        self.sentences["方法-4"] = ["不放一点" + i for i in self.words['condiment']]
        self.sentences["称赞"] = ["吃了" + i + "了，这种做法还是第一次见到" for i in self.words['longtime']]
        self.sentences["称赞-2"] = ["比" + i + "好吃" + random.sample(self.words['times'], 1)[0] for i in self.words['place']]
        self.sentences["称赞-3"] = [i + "都吃不到" for i in self.words['place']]
        self.sentences["称赞-4"] = ["能让你多吃{}碗".format(random.randint(2, 10)) + i for i in self.words['course']]
        self.sentences["量大-1"] = ["一次做一" + i for i in self.words['quantity']]
        self.sentences["量大-2"] = ["一大" + i + "不够吃" for i in self.words['quantity']]
        self.sentences["持久-1"] = ["我们家连着吃了" + i for i in self.words['longtime']]
        self.sentences["持久-2"] = [i + "吃不腻" for i in self.words['longtime']]
        self.sentences["认可-1"] = [i + "点名要吃" for i in self.words['family']]
        self.sentences["认可-2"] = ["自从学会这样做，" + i + "隔三差五想吃，吃一次就忘不了" for i in self.words['family']]
        self.sentences["认可-3"] = [i + "的最爱" for i in self.words['family']]
        self.sentences["认可-4"] = ["隔壁" + i + "天天来蹭饭" for i in self.words['neighbour']]
        self.sentences["认可-5"] = ["隔壁的" + i + "都馋哭了" for i in self.words['neighbour']]
        self.sentences["认可-6"] = ["招待" + i + "特别有面子" for i in self.words['leader']]

    def main(self):
        self.generator()
        self.add_periods()

        self.sentences["方法"] = []
        self.sentences["称赞"] = []
        for key, val in list(self.sentences.items()):
            k = key.split("-")
            if len(k) > 1 and k[0] in ["称赞", "量大", "持久", "认可"]:
                self.sentences["称赞"].append(self.sentences[key])
                del self.sentences[key]
            elif len(k) > 1 and k[0] == "方法":
                self.sentences["方法"].append(self.sentences[key])
                del self.sentences[key]

        return self.sentences


if __name__ == "__main__":
    sentenceGenerator = SentenceGenerator("土豆")
    print(sentenceGenerator.main())
