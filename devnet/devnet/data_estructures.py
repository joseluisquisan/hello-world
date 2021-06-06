def legalAges():
    lifeEvent = {
          "drivingAge": 16,
          "votingAge": 18,
          "drinkingAge": 21,
          "retirementAge": 65
      }

    print("The legal driving age is " + str(lifeEvent["drivingAge"]) + ".")
    print("The legal voting age is " + str(lifeEvent["votingAge"]) + ".")
    print("The legal drinking age is " + str(lifeEvent["drinkingAge"]) + ".")
    print("The legal retirement age is " + str(lifeEvent["retirementAge"]) + ".")

    
legalAges()