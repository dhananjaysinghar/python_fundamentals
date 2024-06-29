l5 = {"Raj":1000, "Nehru":2500, "Krupa":5000, "Karuna":7000, "Nidhi":1500}

l8 = list(
                filter(
                        lambda key: l5[key] >= 2000, l5
                    )
             
          )


print(l8)
