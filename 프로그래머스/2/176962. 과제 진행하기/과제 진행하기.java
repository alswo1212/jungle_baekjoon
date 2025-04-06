import java.util.PriorityQueue;
import java.util.Stack;
import java.util.Arrays;

class Solution {
    public String[] solution(String[][] plans) {
        String[] answer = new String[plans.length];
        PriorityQueue<Plan> pq = new PriorityQueue<>((p1, p2) -> p1.startTime - p2.startTime);
        Stack<Plan> stack = new Stack<>();
        int idx = 0;
        
        for (String[] plan : plans)
            pq.add(new Plan(plan));

        int now = pq.peek().startTime;

        while (!pq.isEmpty()) {
            Plan plan = !stack.isEmpty() && pq.peek().startTime > now
                    ? stack.pop()
                    : pq.poll();

            if (pq.peek() == null) {
                answer[idx++] = plan.name;
                continue;
            }
            
            now = Math.max(plan.startTime, now);
            int canUseTime = pq.peek().startTime - now;
            if (plan.getRemainTime() <= canUseTime) {
                answer[idx++] = plan.name;
                now += plan.getRemainTime();
                continue;
            }
            stack.add(plan);
            plan.doingTime += canUseTime;
            now += canUseTime;
        }

        while (!stack.isEmpty())
            answer[idx++] = stack.pop().name;

        return answer;
    }
}

class Plan {
    String name;
    int startTime;
    int playTime;
    int doingTime;

    public Plan(String[] plan) {
        this.name = plan[0];
        this.startTime = parseTime(plan[1]);
        this.playTime = Integer.parseInt(plan[2]);
    }

    private int parseTime(String time) {
        String[] arr = time.split(":");
        return Integer.parseInt(arr[0]) * 60 + Integer.parseInt(arr[1]);
    }

    public int getRemainTime() {
        int remainTime = playTime - doingTime;
        return Math.max(0, remainTime);
    }
}