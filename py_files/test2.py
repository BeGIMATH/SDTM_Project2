import sys 
sys.path.append("../build/lib")
import tp4 

def f():
    v1 = tp4.Vector_create(1,2,3)
    v2 = tp4.Vector_create(4,5,6)
    v = tp4.Vector_add(v1,v2)
    tp4.stats()
    val_v = tp4.Vector_str(v)
    print("Vector v: %s" % val_v)
    tp4.Vector_destroy(v2)
    tp4.Vector_destroy(v1) 
    #tp4.Vector_destroy(v)
    return v

tp4.stats()
vector = f()
tp4.stats()
val_v = tp4.Vector_str(vector)

