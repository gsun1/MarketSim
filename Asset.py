from random import randint
#import matplotlib.pyplot as plt

num_info = 5
num_endowed = 100
tum_traders = 100
lifetime = 100


class Asset:
    def __init__(self):
        self.info_dist = []
        for i in range(num_info):  # initialize distributions of information
            self.info_dist.append(randint(1, 5))
        self.info = []
        self.time = 0

    def init_asset(self):
        self.time = lifetime
        self.info = []
        for i in range(num_endowed):
            tmp = []
            for j in range(num_info):
                tmp.append(randint(0, self.info_dist[j]))
            self.info.append(tmp)
        for _ in range(100):
            for i in range(num_endowed):
                for j in range(num_info):
                    self.info[i][j] = \
                        max(0, self.info[i][j] + randint(-self.info_dist[j] - 1, self.info_dist[j]))
        return self.info

    def isLastPeriod(self):
        return self.time == 0

    def update(self):
        self.time -= 1
        for i in range(num_endowed):
            for j in range(num_info):
                self.info[i][j] = \
                    max(0, self.info[i][j] + randint(-self.info_dist[j]-1, self.info_dist[j]))
        return self.info

    def getValue(self):
        return sum([sum(x) for x in self.info])


'''m = Market()
m.init_asset()
data = []
for i in range(100):
    m.update()
    data.append(m.getValue())

plt.plot(data)
plt.show()'''