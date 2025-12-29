r, g, b = [int(i)/255 for i in input().split()]

vmax = max(r, g, b)
vmin = min(r, g, b)

l = (vmax + vmin) / 2
mi = vmax-vmin
pl = vmax+vmin

# h
if vmax == vmin: h = 0
elif vmax == r:
    h = 60*(g-b)/(mi)
    if g < b: h += 360

elif vmax == g: h = 60*(b-r)/(mi) + 120
else: h = 60*(r-g)/(mi) + 240

# s

if l == 0 or vmax == vmin: s = 0
elif 0 < l <= 0.5: s = mi/pl
else: s = mi/(2-pl)

s *= 255
l *= 255

print(int(round(h)), int(round(s)), int(round(l)))