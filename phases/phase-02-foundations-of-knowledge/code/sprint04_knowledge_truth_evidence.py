prior = 0.01  # base rate
sens  = 0.90  # P(+|H)
fpr   = 0.05  # P(+|not H)
post = sens*prior / (
  sens*prior + fpr*(1-prior))
print(round(post, 3)) # 0.154
