function solution(sequence) {
    const getMaxSubSum = (arr) => {
        let temp = 0, result = 0;
        for (const num of arr){
            if (temp + num < 0) {
                temp = 0;
                continue
            }
            temp += num
            result = Math.max(result, temp)
        }
        return result
    }
    const answer1 = getMaxSubSum(sequence.map((s,i) => s * (i%2 ? -1 : 1)))
    const answer2 = getMaxSubSum(sequence.map((s,i) => s * (i%2 ? 1 : -1)))
    
    return Math.max(answer1, answer2);
}