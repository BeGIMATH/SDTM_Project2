import tp4

def print_part1():
   print("pi()=%lg" % tp4.pi())
   print("VERSION=%s" % tp4.VERSION)
   print("pi()=%lg" % tp4.pi())
   print("PI+5=%lg" % tp4.add_pi(5.0))

tp4.stats()
print_part1()
tp4.set_log(1)
print_part1()
tp4.set_log(0)
tp4.stats()

