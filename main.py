class Co_owner:
    # define a co-owner
    NUMBER_CO_OWNER = 1

    def __init__(self, name, quota_share1=1371, quota_share2=712):
        
        print("Coproprietaire N° ", Co_owner.NUMBER_CO_OWNER)
        
        self.name = name
        self.quota_share1 = quota_share1
        self.quota_share2 = quota_share2

        Co_owner.NUMBER_CO_OWNER += 1


# initialization of co-owner
while Co_owner.NUMBER_CO_OWNER < 8:
    
    name_owner = input("Donnez un nom au coproprietaire ")        
    
    owner = Co_owner(name_owner)

    print("{} a une quote-part principale de {} et une secondaire de {}".format(owner.name, owner.quota_share1, owner.quota_share2))
