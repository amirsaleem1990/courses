# (print) or (return) k darmyan farq
def price(mobile, cover, charger):
      return mobile + cover + charger

my = price(3,5,2)
## 10
my
## 10
my * 2
## 20


# opar (retrun) ki command use ki h.. jis ki wajah sy jab ham ny (my*2) chalaya to wo chal gya or result bhi
# aa gya,, agar ham function me (return) k bajay (print) ki command use karty to kya hota.....
# (print) or (return) k darmyan farq
def price(mobile, cover, charger):
      print (mobile+cover+charger)

my = price(3,5,2)
## 10
my
## (function chal gya, or answer bhi print ho gya, magar ye kaam memori me nahi gya,, yani k is ka koi 
##memorey adress nahi h.. agar ham baad me is ko use karna chahen to nahi kar sakty, chahy ham is ko 
## ksi veriable me store bhi kar den tab bhi wo store nahi kary ga.. is ko aap is tarah check kar sakty
## hen k (my) ka type check karen: type(my) to is ko answer me int. dena chahye  q k (my) k andar (10)
## store h jo k int. h magar aap ko jawab mily ga (<class 'NoneType'>) or ap (my) ko wapis hasil karny 
## k lye (my) likhen gy to koi result nahi show ho ga q k (my) darasal memory me gya hi nahi!

my * 2
## Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    u*4
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
