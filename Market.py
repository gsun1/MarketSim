#import Asset

class Market():
    def __init__(self):
        pass

    '''
    equilibrium(self,buyers,seller)
    @params:
    buyers - a list of the valuations of buyers
    sellers - a list of the valuations of sellers
    @returns:
    A tuple (p,c) where p is the market price and c
    is the number of participants. In particular, if
    the buyers and sellers are sorted in terms of their
    valuations, the first c buyers and sellers will transact
    '''
    def equilibrium(self,buyers,sellers):
        assert(buyers == sorted(buyers,reverse=True))
        assert(sellers == sorted(sellers,reverse=True))
        max_trans = min(len(buyers),len(sellers))
        count = 0
        for i in range(max_trans):
            if buyers[i] < sellers[i]:
                if i == 0:
                    return None
                else:
                    return (buyers[i-1] + sellers[i-1])//2,count
            count += 1
        return (buyers[max_trans-1] + sellers[max_trans-1])/2,count

