class Ranker:
    def _init_ (self):
        pass

    def add_ranking(self, category, rankings):
        new_dict = {category: rankings}
        file1 = open("rankings.txt","a")
        file1.write(str(new_dict) + "\n")

