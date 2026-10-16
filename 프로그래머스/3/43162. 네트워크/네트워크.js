function solution(n, computers) {
    let answer = 0;
    const visit = Array(n).fill(false);
    const bfs = (index) => {
        const q = [index]
        visit[index] = true;
        let q_i = 0;
        while (q_i < q.length) {
            const num = q[q_i++];
            for (let i = 0; i < n; i++) {
                if (visit[i] || !computers[num][i]) continue;
                q.push(i);
                visit[i] = true;
            }
        }
    }
    
    for (let i = 0; i < n; i++) {
        if (!visit[i]) {
            answer++;
            bfs(i);
        }
    }
    return answer;
}