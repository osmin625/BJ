#include <stdio.h>

int main(void) {
	int M, N;
	int c = 0, m = 0;
	scanf("%d %d", &M, &N);
	for (int i = 100; i > 0; i--) {
		if (i*i >= M && i*i <= N) {
			c += i * i;
			m = i * i;
		}
	}
	if (c) printf("%d %d", c, m);
	else printf("-1");
}