問題敘述
色彩空間是電腦影像中很重要的一個概念,HSL 和 RGB 都是常見的顏色模
型。與 RGB 相比,HSL 更符合人類感知顏色的直覺,使用了色相、飽和度、明度
三個維度去描述。某些軟體的色彩選擇功能會同時提供了這兩個色彩模型,但並非
所有軟體都有,因此有時你還是需要自己計算。
給定 (R, G, B) 為 RGB 色彩模型中的三個值,R、G 和 B 為 0 到 255 之間的
整數,以下是由 RGB 轉換成 HSL 的計算流程:
r = R/255
g = G/255
b = B/255
max = max(r, g, b)
min = min(r, g, b)
l =
1
2
(max + min)

h =

{
0, if max = min
60 ×
g − b
max − min

, if max = r and g ≥ b, max ≠ min

60 ×
g − b
max − min

+ 360, if max = r and g < b, max ≠ min

60 ×
b − r
max − min

+ 120, if max = g, max ≠ r, max ≠ min

60 ×
r − g
max − min

+ 240, if max = b, max ≠ g, max ≠ r, max ≠ min

s =
{
0, if l = 0 or max = min
max − min
max + min
=
max − min
2l
, if 0 < l ≤ 0.5, max ≠ min

max − min
2 − (max + min)
=
max − min
2 − 2l
, if 0.5 < l , max ≠ min

s = s × 255
l = l × 255
請你撰寫一個程式來完成 RGB 到 HSL 的轉換。

輸入格式
輸入三個整數 R、G 與 B,代表 RGB 色彩模型的值。兩數之間以一個空白間
隔。
輸出格式
將輸入 RGB 顏色轉換成 HSL 後輸出三個整數值(如計算後有小數點則四捨五
入) H、S 和 L,兩數之間以一個空白間隔。
輸入範例 1
255 000 000

輸出範例 1
0 255 128

輸入範例 1
255 195 195

輸出範例 2
0 255 225

評分說明
此題目測資分為兩組,每組測資有多筆測試資料,需答對該組所有測資才能獲得
該組分數,各組詳細限制如下。
第一組(40 分):計算過程中保證結果必為整數。
第二組(60 分):無特殊限制。

Link : [https://zerojudge.tw/ShowProblem?problemid=m900](https://zerojudge.tw/ShowProblem?problemid=m900)