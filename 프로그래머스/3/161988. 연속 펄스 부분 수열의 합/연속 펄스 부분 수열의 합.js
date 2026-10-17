function solution(sequence) {
    let m = 0, M = 0;
    let acc = m;

    for (let i = 0; i < sequence.length; i++) {
        acc = i % 2 == 1 ? acc - sequence[i] : acc + sequence[i];
        M = Math.max(M, acc);
        m = Math.min(m, acc);
    }
    return M == m ? M : M - m;
}