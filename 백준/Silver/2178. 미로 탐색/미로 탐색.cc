#include <cstdio>
#include <queue>

int n, m;
char map[102][102] = {};
const short dx[4] = { 1, 0, -1, 0 };
const short dy[4] = { 0, 1, 0, -1 };


int bfs() {
	short q[10000][3] = { 1, 1, 1 };
	short sp = 0, ep = 1;

	while (1) {
		short y = q[sp][0], x = q[sp][1], t = q[sp][2] + 1;
		sp++;

		for (int d = 0; d < 4; d++) {
			short ny = y + dy[d]; // 다음 행
			short nx = x + dx[d]; // 다음 열
			if (ny == n && nx == m) return t;

			if (map[ny][nx] != '1') continue;
			map[ny][nx] = 0;
			q[ep][0] = ny, q[ep][1] = nx, q[ep][2] = t;
			ep++;
		}
	}
}

int main(void) {
	scanf("%d %d", &n, &m);
	for (int y = 1; y <= n; y++) scanf("%s", map[y] + 1);
	map[1][1] = 0;
	printf("%d", bfs());
	
}

