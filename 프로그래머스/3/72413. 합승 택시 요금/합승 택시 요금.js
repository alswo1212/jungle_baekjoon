function solution(n, s, a, b, fares) {
    let answer = Number.MAX_VALUE;
    const maps = Array.from({length: n}).map(() => Array(n).fill(Number.MAX_VALUE));
    for (let i = 0; i < n; i++) maps[i][i] = 0;
    fares.forEach(([c, d, f]) => {
        c--, d--;
        maps[c][d] = maps[d][c] = f;
    })
    
    for (let k = 0; k < n; k++) {
        for (let i = 0; i < n; i++) {
            for (let j = 0; j < n; j++) {
                if (maps[i][j] > maps[i][k] + maps[k][j]) {
                    maps[i][j] = maps[j][i] = maps[i][k] + maps[k][j]
                }
            }
        }
    }
    
    s--, a--, b--;
    for (let k = 0; k < n; k++) {
        const temp = maps[s][k] + maps[k][a] + maps[k][b];
        answer = Math.min(answer, temp)
    }
    return answer;
}