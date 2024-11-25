#include <cstdio>
#include <cstring>

int main(void) {
	int t, maxd = 0, mind = 1 << 30;
	char max_name[33], min_name[33];
	for (scanf("%d", &t); t--;){
		int y, m, d, temp;
		char name[30] = "";
		scanf("%s %d %d %d", name, &d, &m, &y);
		temp = y * 10000 + m * 100 + d;
		if (temp > maxd) maxd = temp, strcpy(max_name, name);
		if (temp < mind) mind = temp, strcpy(min_name, name);
	}
	printf("%s\n%s", max_name, min_name);
	return 0;
}