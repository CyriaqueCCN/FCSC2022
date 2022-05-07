#include <stdio.h>
#include <stdlib.h>

const unsigned char F = 0x00;
const unsigned char T = 0x01;

typedef struct	s_bin {
	unsigned char x0;
	unsigned char x1;
	unsigned char x2;
	unsigned char x3;
	unsigned char x4;
}		t_bin;

int	main(void) {
	
	t_bin test = { T, F, F, F, F }; // test set, should return 10100
	t_bin flag = { T, F, F, T, T }; // flag set, test before trying
	t_bin res  = { F, F, F, F, F }; // result set
	t_bin s    = flag;

	res.x0 = s.x0 ^ (s.x3 & ~s.x4);
	res.x1 = s.x1 ^ (s.x4 & ~s.x0);
	res.x2 = s.x2 ^ (s.x0 & ~s.x1);
	res.x3 = s.x3 ^ (s.x1 & ~s.x2);
	res.x4 = s.x4 ^ (s.x2 & ~s.x3);
	
	printf("FCSC{%d%d%d%d%d}\n", res.x0, res.x1, res.x2, res.x3, res.x4);
	return 0;
}
