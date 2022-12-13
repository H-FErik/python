wr = open('halmazok.txt','w')
'''
Halmaz (set):
- rendezetlen (elemeknek nincs indexe)
- egy elem csak egyszer szerepelhet
- többféle típust tárolhat egyszerre is
- a halmaz eleme maga nem változtatható meg
'''
wr.write("Halmaz (set):\n"
"- rendezetlen (elemeknek nincs indexe)\n"
"- egy elem csak egyszer szerepelhet\n"
"- többféle típust tárolhat egyszerre is\n"
"- a halmaz eleme maga nem változtatható meg\n")
wr.write("reggeli = {'víz', 'tea', 'vaj', 'pirítós'}\n")

reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
wr.write("ebed = {'víz', 'halászlé', 'kenyér'}\n")
ebed = {'víz', 'halászlé', 'kenyér'}

wr.write("# halmaz létrehozása\n"
"reggeli = {'tea', 'vaj', 'piritós'}\n")

# halmaz létrehozása
reggeli = {'tea', 'vaj', 'piritós'}

wr.write("# üres halmaz létrehozása\n"
"ebed = {}  <- SZÓTÁRT hoz létre!!!\n"
"ebed = set()\n")

# üres halmaz létrehozása
# ebed = {}  <- SZÓTÁRT hoz létre!!!
ebed = set()

wr.write("# bejárható gyűjteményből, pl. listából\n"
"ebed = set(['halászlé', 'kenyér', True])\n")

# bejárható gyűjteményből, pl. listából
ebed = set(['halászlé', 'kenyér', True])  

wr.write("# egy elem hozzáadása\n"
"reggeli.add('lekvár')\n")

# egy elem hozzáadása
reggeli.add('lekvár')

wr.write("# egy nem meghatározott elem eltávolítása\n"
"reggeli.pop()\n")

# egy nem meghatározott elem eltávolítása
reggeli.pop()

wr.write("# egy bizonyos elem eltávolítása\n"
"# ha nincs ilyen elem, akkor hibát eredményez\n"
"reggeli.remove('sajt')\n")
wr.write("# egy bizonyos elem eltávolítása\n"
"# ha nincs ilyen elem, nem eredményez hibát\n"
"reggeli.discard('sajt')\n")
# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, akkor hibát eredményez
reggeli.remove('sajt')


# egy bizonyos elem eltávolítása
# ha nincs ilyen elem, nem eredményez hibát
reggeli.discard('sajt')

wr.write("# metszet\n"
"print(reggeli & ebed)\n")
# metszet
print(reggeli & ebed)

wr.write("# unio\n"
"print(reggeli | ebed)\n")
# unio
print(reggeli | ebed)

wr.write("# különbség\n"
"print(reggeli - ebed)\n")
# különbség
print(reggeli - ebed)

wr.write("# csak az egyikben, vagy csak a másikban\n"
"print(reggeli ^ ebed)")
# csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed)


wr.close()