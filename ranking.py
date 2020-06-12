import ast

class Ranker:
    def _init_ (self):
        pass

    def add_ranking(self, category, rankings):
        new_dict = {category: rankings}
        file1 = open("rankings.txt","a")
        file1.write(str(new_dict) + "\n")

    def two_sort(self, list1, list2):
        for i in range(0, len(list1)):
            for passnum in range(i):
                if list1[i] < list1[passnum]:
                    temp = list1[i]
                    list1[i] = list1[passnum]
                    list1[passnum] = temp

                    temp1 = list2[i]
                    list2[i] = list2[passnum]
                    list2[passnum] = temp1
        return list1,list2

    def convert_to_rankings(self, dictionary):
        iterator = 0
        for i in dictionary:
            dictionary[i] = iterator + 1
            iterator += 1
        return dictionary

    def two_sort_ascending(self, list1, list2):
        for i in range(0, len(list1)):
            for passnum in range(i):
                if list1[i] > list1[passnum]:
                    temp = list1[i]
                    list1[i] = list1[passnum]
                    list1[passnum] = temp

                    temp1 = list2[i]
                    list2[i] = list2[passnum]
                    list2[passnum] = temp1
        return list1,list2

    def get_final_rankings(self):
        list1 = []
        with open('rankings.txt') as fp:
            line = fp.readline()
            while line:
                list1.append(ast.literal_eval(line))
                line = fp.readline()

        return list1

