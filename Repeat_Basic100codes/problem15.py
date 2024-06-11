#Determine weather type

temperature = int(input("what is the current temperature"))
humidity = int(input("what is current humidity"))

if temperature >= 30 and humidity >= 90 :
    print("Hot and Humid")
elif temperature >=30 and humidity < 90: 
    print("Hot")
elif temperature <30 and humidity>= 90:
    print("Cold and Humid")
elif temperature < 30 and humidity < 90 :
    print("Cold")