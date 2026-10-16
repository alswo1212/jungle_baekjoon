function solution(m, n, puddles) {
    var answer = 0;
    const board = Array.from({length:n+1}).map(() => Array(m+1).fill(0))
    board[1][1] = 1;
    for (const [x,y] of puddles) {
        board[y][x] = -1;
    }
    
    for (let i = 1; i <= n; i++ ){
        for (let j = 1; j <= m; j++) {
            if (board[i][j] === -1) continue;
            let temp = 0;
            if (board[i-1][j] !== -1) board[i][j] += board[i-1][j]
            if (board[i][j-1] !== -1) board[i][j] += board[i][j-1]
            board[i][j] %= 1_000_000_007
        }
    }
    
    return board[n][m];
}