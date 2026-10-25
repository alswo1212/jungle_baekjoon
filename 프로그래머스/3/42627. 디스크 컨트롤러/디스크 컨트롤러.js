class Heap {
    constructor(cmp){
        this.items = [];
        this.cmp = cmp;
    }
    get size(){return this.items.length}
    peek(){return this.items[0]}
    push(val){
        const arr = this.items;
        arr.push(val)
        let i = arr.length - 1;
        while (i) {
            const p = (i - 1) >> 1;
            if (this.cmp(arr[p], arr[i]) < 0) break;
            [arr[p], arr[i]] = [arr[i], arr[p]];
            i = p;
        }
    }
    pop(){
        const arr = this.items, top = arr[0], last = arr.pop();
        if (arr.length){
            arr[0] = last;
            let now = 0;
            while (now < arr.length) {
                const left = (now << 1) + 1, right = left + 1;
                let next = now;
                if (left < arr.length && this.cmp(arr[left], arr[next]) < 0) next = left;
                if (right < arr.length && this.cmp(arr[right], arr[next]) < 0) next = right;
                if (now === next) break;
                [arr[next], arr[now]] = [arr[now], arr[next]];
                now = next;
            }
        }
        return top;
    }
}

function solution(jobs) {
    let answer = 0;
    const n = jobs.length;
    const heap = new Heap((a,b) => a.needTime-b.needTime || a.start-b.start || a.id-b.id);
    let done = 0;
    const inputJobs = jobs.map((j, i) => ({
        start: j[0],
        needTime: j[1],
        id: i,
    }))
    inputJobs.sort((a,b) => a.start - b.start || a.id - b.id);
    let now = 0;
    let jobIdx = 0;
    while (done < n) {
        if (!heap.size && jobIdx < n) {
            heap.push(inputJobs[jobIdx++]);
            if (heap.peek().start > now) now = heap.peek().start;
            continue;
        }
        while (jobIdx < n && inputJobs[jobIdx].start <= now) {
            heap.push(inputJobs[jobIdx++]);
        }
        
        const job = heap.pop()
        now += job.needTime;
        answer += now - job.start;
        done++;
    }
    return Math.floor(answer / n);
}