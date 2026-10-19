function solution(n, roads, sources, destination) {
    const answer = [];
    const numToIdx = {}
    sources.forEach((source, i) => {
        answer.push(-1);
        numToIdx[source] = i;
    })
    const edges = Array.from({length:n+1}).map(() => [])
    roads.forEach(([n1,n2]) => {
        edges[n1].push(n2)
        edges[n2].push(n1)
    });
    const targets = new Set(sources)
    const visit = new Set([destination]);
    const q = [[destination, 0]];
    let qIdx = 0;
    
    
    while (qIdx < q.length) {
        const [now, cnt] = q[qIdx++];
        if (targets.has(now)) {
            answer[numToIdx[now]] = cnt;
            targets.delete(now)
        }
        
        edges[now]?.forEach(next => {
            if (visit.has(next)) return
            q.push([next, cnt+1])
            visit.add(next)
        })
    }
    return answer;
}
