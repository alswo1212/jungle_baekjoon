function solution(jobs) {
    jobs.sort(([a, b], [c, d]) => a - c || b - d);

    const waiting = [];
    const count = jobs.length;

    let jobIndex = 0;
    let processedTime = 0;
    let time = 0;

    while (jobIndex < count || waiting.length) {
        while (
            jobIndex < count &&
            jobs[jobIndex][0] <= time
        ) {
            waiting.push(jobs[jobIndex++]);
        }

        if (waiting.length === 0) {
            time = jobs[jobIndex][0];
            continue;
        }

        let minIndex = 0;

        for (let i = 1; i < waiting.length; i++) {
            const [a, b] = waiting[i];
            const [c, d] = waiting[minIndex];

            if (b < d || (b === d && a < c)) {
                minIndex = i;
            }
        }

        const [start, duration] = waiting[minIndex];
        waiting.splice(minIndex, 1);

        time += duration;
        processedTime += time - start;
    }

    return Math.floor(processedTime / count);
}