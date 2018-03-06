class Co_owner:
    # define a co-owner
    NUMBER_CO_OWNER = 1

    def __init__(self, name, quota_share1, quota_share2):
        
        print("Copropriaitre Numéro ", Co_owner.NUMBER_CO_OWNER)
        self.name = name
        self.quota_share1 = quota_share1
        self.quota_share2 = quota_share2

        Co_owner.NUMBER_CO_OWNER += 1


# error management
def error_manager() :
    return print("Vous devez entrer un nombre --> Recommencer")

# initialization of co-owner
while Co_owner.NUMBER_CO_OWNER <= 8:
    
    print("")
    name_owner = input("Donnez un nom au coproprietaire ")
    print("")

    try :

        owner_quota = int(input("quote-part principale "))
        print("")

    except ValueError :        
        print("")
        error_manager()
        print("")
        continue

    else :
        
        try :

            owner_quota2 = int(input("quote_part secondaire "))
            print("")

        except ValueError :
            print("")
            error_manager()
            print("")
            continue

        else :
            
            owner = Co_owner(name_owner, owner_quota, owner_quota2 )
            print("")
            print("{} a une quote-part principale de {} et une secondaire de {}".format(owner.name, owner.quota_share1, owner.quota_share2))
