
# price =2000
# discount=0

# if price > 1500:
#     discount =price*15/100
    # print ("Total price",price-discount)
# else :
#     discount = price*5/100
    
# print("total price is",price-discount)

price =2000;
discount=0

if price>1500:
    discount=price*15/100

elif price<1000 :
    discount=price*10/100

else :
    discount=price*5/100

print("Total price",price-discount)

marks = 200

if marks >= 100:
    print("invalid marks")
elif 100 <= marks <=80 :
    print("distinction")
elif 60 <= marks <= 80:
    print("First")
elif 50 <= marks <= 60:
    print('Second')
elif 30 <= marks <= 50:
    print("Third")
else:
    print("Failed")
