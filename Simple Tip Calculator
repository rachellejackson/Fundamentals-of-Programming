def simpleTip():
    """
    Allows a user to input the cost of a meal and calculates an appropriate 
    tip for their server. Excellent - 20%, average - 15%, and poor - 10%)

    Inputs:
        cost (float): the cost of the meal

    Outputs:
        Prints statements for the original cost of the meal and the dollar amounts of tips for each
        service level followed by their respective dollar amount totals.
    """
    meal_cost = float(input("Enter the cost of the meal: $"))

    excellent_service_tip = meal_cost * 0.20
    av_service_tip = meal_cost * 0.15
    poor_service_tip = meal_cost * 0.10

    excellent_service_total = meal_cost + excellent_service_tip
    av_service_total = meal_cost + av_service_tip
    poor_service_total = meal_cost + poor_service_tip

    print("Cost of meal: $", "%.2f" % meal_cost)
    print("Excellent Service tip: $", "%.2f" % excellent_service_tip, "total: $", "%.2f"\
       % excellent_service_total)
    print("Average Service tip: $", "%.2f" % av_service_tip, "total: $", "%.2f" % av_service_total)
    print("Poor Service tip: $", "%.2f" % poor_service_tip, "total: $", "%.2f" % poor_service_total)
