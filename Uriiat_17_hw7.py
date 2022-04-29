"""
To know rich customers
"""
def wealth(accounts):
   max_balue = 0
   ind_value = 0
   for i in range(len(accounts)):
      ind_value = sum(accounts[i])
      if ind_value > max_balue:
         max_balue = ind_value
   return max_balue

accounts = [[12,20,28],
[33,34,20],
[2,5,12],
[1,12,9]]
print(accounts)
print(wealth(accounts ))