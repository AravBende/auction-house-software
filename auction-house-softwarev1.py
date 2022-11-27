auction_items = [[6926, "Mono Lisa", 1030312, 0], [1828, "girl with pearl earring", 5012300, 0], [9598, "the starry night", 7480120, 0], [1553, "saint john the baptist", 6038467, 0], [4808, "The last supper", 723404, 0],
                 [4799, "La Vierge aux rochers", 2384782, 0], [9657, "The Vitruvian Man", 2783480, 0], [8877, "leanardo davinci self portrait", 8923748, 0], [1544, "the screaming man", 9237493, 0], [7416, "salvator mundi", 450000000, 0]]


contsearching = True


while contsearching == True:
    for i in range(10):
        print(*auction_items[i], sep=(", "))
    print()
    item_id = int(input("Please input the item number of the item you would like to view: "))
    print()

    for item in auction_items:
        if item_id == item[0]:
            print("ID: " + str(item[0]) + "\nDescription: " + str(item[1]) + "\nprice: " + str(item[2]) + "\nAmount of bids: " + str(item[3]))
            print()
            ifbid = input("would you like to bid? (y/n) ")
            if ifbid.lower() == "y":
                item[3] += 1
                bidamount = int(input("Please enter bid amount, must be more then " + str(item[2]) + ": "))
                if bidamount > item[3]:
                    item[3] = bidamount
                else:
                    print("thats not enough money")
    asktocontinue = input("would you like to continue searching? (y/n) ")
    print()
    if asktocontinue.lower() == "n":
        contsearching = False
