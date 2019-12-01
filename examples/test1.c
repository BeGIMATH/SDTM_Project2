#include "tp4.h"

#include <stdio.h>

void print_part1()
{
	printf("VERSION=%s\n", VERSION);
	printf("PI=%lg\n", PI);
	printf("pi()=%lg\n", pi());
	printf("PI+5=%lg\n", add_pi(5));
}

int main()
{
	stats();
	print_part1();
	set_log(1);
	print_part1();
	set_log(0);
	stats();
	return 0;
}
