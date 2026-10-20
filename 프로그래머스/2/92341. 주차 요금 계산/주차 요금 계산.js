function solution(fees, records) {
    const timeToInt = time => {
        const [hh,mm] = time.split(':')
        return Number(hh) * 60 + Number(mm);
    }
    const answer = []
    const LAST_TIME = timeToInt('23:59')
    const carIO = {}
    
    records.forEach((record) => {
        const [time, car, t] = record.split(' ')
        if(!(car in carIO)) carIO[car] = []
        carIO[car].push(timeToInt(time))
    })
    
    const keys = []
    for (const key in carIO) keys.push(key)
    keys.sort()
    keys.forEach(key => {
        const arr = carIO[key];
        let sum = 0
        for(let i = 0; i < arr.length; i+=2) {
            sum += (arr[i+1] ?? LAST_TIME) - arr[i]
        }

        if (sum <= fees[0]){
            answer.push(fees[1])
        } else{
            sum -= fees[0]
            answer.push(fees[1] + Math.ceil(sum / fees[2]) * fees[3])
        }
    })
    return answer;
}