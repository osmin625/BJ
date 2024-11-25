#include <stdio.h>

int main(void) {
	int n, p;
	scanf("%d", &n);
	
	for (int i = 0; i < n; i++) {
		scanf("%d", &p);
		int max_value = 0, value;
		int idx = 0;
		char name[100][1001];
		for (int j = 0; j < p; j++) {
			scanf("%d %s", &value, &name[j]);
			if (value > max_value) {
				idx = j;
				max_value = value;
			}
		}
		printf("%s\n", name[idx]);
	}
}
