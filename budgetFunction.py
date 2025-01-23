def budgetFunction(budget):
     if budget < 100:
         return "Local day trips."
     elif budget < 500:
        return "Nearby cities."
     else:
        return "International travel!"