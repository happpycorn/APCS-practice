r, g, b = map(int, input().split())

mx = max(r, g, b)
mn = min(r, g, b)

l = (mx+mn)/2

if mx == mn: h = 0
elif mx == r and g >= b: h = 60*(g-b)/(mx-mn)
elif mx == r and g < b: h = 60*(g-b)/(mx-mn)+360
elif mx == g: h = 60*(b-r)/(mx-mn)+120
else: h = 60*(r-g)/(mx-mn)+240

if l == 0 or mx == mn: s = 0
elif 0 < l <= 0.5 or mx == mn: s = (mx-mn)/(mx+mn)
else: s = (mx-mn)/(2-(mx+mn))

s *= 255
l *= 255

print(int(h), int(s), int(l))