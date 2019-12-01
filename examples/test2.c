#include "tp4.h"

#include <stdio.h>
#include <stdlib.h>

Vector *f()
{
  Vector *v1 = Vector_create(1, 2, 3);
  Vector *v2 = Vector_create(4, 5, 6);
  Vector *v = Vector_add(v1, v2);
  stats();
  char *val_v = Vector_str(v);
  printf("Vector v: %s\n", val_v);
  free(val_v);
  Vector_destroy(v2);
  Vector_destroy(v1);
  Vector_destroy(v);
  return v;
}

int main()
{
  stats();
  Vector *vector = f();
  stats();
  char *val_v = Vector_str(vector);
  /* Error at previous line v was destroyed */
  free(val_v);
  return 0;
}
