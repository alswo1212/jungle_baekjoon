class Heap{
    constructor(cmp){
        this.values = [];
        this.cmp = cmp;
    }
    get size(){return this.values.length}
    peek(){return this.values[0]}
    push(val){
        const arr = this.values;
        arr.push(val)
        let i = arr.length - 1;
        while (i) {
            const p = (i-1) >> 1
            if (this.cmp(arr[p], arr[i]) <= 0) break
            [arr[p], arr[i]] = [arr[i], arr[p]]
            i = p
        }
    }
    pop(){
        const arr = this.values, top = arr[0], last = arr.pop();
        if (arr.length){
            arr[0] = last;
            let now = 0;
            while (now < arr.length) {
                const left = (now << 1) + 1, right = left + 1;
                let next = now;
                if (left < arr.length && this.cmp(arr[left], arr[next]) < 0) next = left
                if (right < arr.length && this.cmp(arr[right], arr[next]) < 0) next = right
                if (now === next) break
                [arr[now], arr[next]] = [arr[next], arr[now]]
                now = next
            }
        }
        return top;
    }
}

function solution(n, k, enemy) {
    let round = 0;
    const heap = new Heap((a,b) => b-a)
    for(const e of enemy){
        round++;
        heap.push(e)
        n -= e
        while (n < 0 && k && heap.size) {
            const num = heap.pop()
            n += num
            k--;
        }
        if (n < 0) {
            return round - 1
        }
    }
    return round;
}