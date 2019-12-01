#ifndef _TP3_H
#define _TP3_H

/***********************************************************
 * Part 1
 */

#define VERSION "1.0.3"

extern const double PI;

/* return PI value */
double pi();

/* return PI+v */
double add_pi(double v);

/* log function */
void set_log(int v);

/* Some stats */
void stats();

/***********************************************************
 * Part 2
 */

/* opaque type vector of 3 component */
typedef struct _vector Vector;

/* Create a new vector using the given 3 doubles */
Vector *Vector_create(double a, double b, double c);
/* Create anew vector using two others */
Vector *Vector_add(Vector *v1, Vector *v2);
/*Compute the cross product using two others */
Vector *Vector_cross(Vector *v1, Vector *v2);
/*Compute the dor product of the two given vectors*/
double Vector_dot(Vector *v1, Vector *v2);
double Vector_angle(Vector *v1, Vector *v2);
/* Return coordinates of v*/
double Vector_elem(Vector *v, int coord);
/* Return a description of vector v */
char *Vector_str(Vector *v);
/* Destroy vector v */
void Vector_destroy(Vector *v);

#endif
