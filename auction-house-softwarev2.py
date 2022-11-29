auction_items = [[6926, "Mono Lisa","portrait made by leanardo davinci", 1030312, 0], [1828, "girl with pearl earring","made by davinci" ,  5012300, 0], [9598, "the starry night","made by davinci", 7480120, 0], [1553, "saint john the baptist","made by someone very talnted" ,6038467, 0], [4808, "The last supper", "someone died", 723404, 0],
                [4799, "La Vierge aux rochers", "very cool painting",  2384782, 0], [9657, "The Vitruvian Man", "intresting painting", 2783480, 0], [8877, "leanardo davinci self portrait", "seld portrait of leanardo davinci",  8923748, 0], [1544, "the screaming man","a man that is screaming", 9237493, 0], [7416, "salvator mundi", "Some guy",450000000, 0]]


contsearching = True


while contsearching == True:
   for i in range(10):
       print(*auction_items[i], sep=(", "))
   print()
   item_id = int(input("Please input the item number of the item you would like to view: "))
   print()

   for item in auction_items:
       if item_id == item[0]:
           print("ID: " + str(item[0]) + "\nname: " + str(item[1]) + "\ndescription: " + str(item[2])+ "\nprice: " + str(item[3]) + "\nAmount of bids: " + str(item[4]))
           print()
           ifbid = input("would you like to bid? (y/n) ")
           if ifbid.lower() == "y":
               bidamount = int(input("Please enter bid amount, must be more than " + str(item[3]) + ": "))
               if bidamount > item[3]:
                   item[3] = bidamount
                   item[4] += 1
               else:
                   print("thats not enough money")
   asktocontinue = input("would you like to continue searching? (y/n) ")
   print()
   if asktocontinue.lower() == "n":
       contsearching = False
