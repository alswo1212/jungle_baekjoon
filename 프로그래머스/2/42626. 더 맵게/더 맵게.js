class Heap {
    constructor(cmp){
        this.values = [];
        this.cmp = cmp;
    }
    get size(){return this.values.length}
    peek(){return this.values[0]}
    push(val){
        const arr = this.values;
        arr.push(val);
        let i = arr.length - 1;
        while (i) {
            const p = (i - 1) >> 1;
            if (this.cmp(arr[p], arr[i]) < 0) break;
            [arr[p], arr[i]] = [arr[i], arr[p]];
            i = p;
        }
    }
    pop(){
        const arr = this.values, top = arr[0], last = arr.pop();
        if (arr.length) {
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

function solution(scoville, K) {
    let answer = 0;
    const heap = new Heap((a,b) => a-b);
    scoville.forEach(s => heap.push(s));
    
    while (heap.size >= 2 && heap.peek() < K) {
        heap.push(heap.pop() + heap.pop() * 2);
        answer++;
    }
    
    return heap.size === 0 || heap.peek() < K ? -1 : answer;
}