class Co_owner:
    # define a co-owner
    NUMBER_CO_OWNER = 1

    def __init__(self, name, quota_share1, quota_share2):
        
        print("Copropriaitre Numéro ", Co_owner.NUMBER_CO_OWNER)
        self.name = name
        self.quota_share1 = quota_share1
        self.quota_share2 = quota_share2

        Co_owner.NUMBER_CO_OWNER += 1


# initialization of co-owner
p1 = Co_owner("MARC", 1375, 720)
print("{} a une quote-part principale de {} et une secondaire de {}".format(p1.name, p1.quota_share1, p1.quota_share2))
p2 = Co_owner("LILIAN", 125, 117)
print("{} a une quote-part principale de {} et une secondaire de {}".format(p2.name, p2.quota_share1, p2.quota_share2))
