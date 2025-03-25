YEARS_INTEREST = 0.08
YEARS_INSTERT = 100000
YEARS_COUNT = 30

sum_value = 0
pow_value = 1

for i in range(YEARS_COUNT):
    pow_value *= 1+YEARS_INTEREST
    sum_value += pow_value

print(YEARS_INSTERT*sum_value)