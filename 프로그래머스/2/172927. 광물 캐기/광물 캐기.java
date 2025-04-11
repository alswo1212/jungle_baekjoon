import java.util.Arrays;
import java.util.Map;

class Solution {
    private Map<String, Integer> map = Map.of("diamond", 0, "iron", 1, "stone", 2);
    private int min = Integer.MAX_VALUE;

    public int solution(int[] picks, String[] minerals) {
        int[] pickaxeArr = getPickaxeArr(picks);
        int[] mineralNums = mineralToNum(minerals);
        dfs(pickaxeArr, mineralNums, 0, 0, 0);
        return min;
    }

    private void dfs(int[] pickaxeArr, int[] mineralNums, int mineralIdx, int sum, int pickCnt) {
        if (sum >= min)
            return;
        if (mineralIdx >= mineralNums.length || pickCnt >= pickaxeArr.length) {
            min = Math.min(min, sum);
            return;
        }

        for (int i = 0; i < pickaxeArr.length; i++) {
            if (pickaxeArr[i] == -1) {
                continue;
            }
            int tempSum = sum;
            int pickaxeNum = pickaxeArr[i];
            pickaxeArr[i] = -1;

            int mineralCnt = mineralIdx + 5 >= mineralNums.length ? mineralNums.length - mineralIdx : 5;
            int newMineralIdx = mineralIdx + mineralCnt;
            if (pickaxeNum == 0) {
                tempSum += mineralCnt;
            } else if (pickaxeNum == 1) {
                for (int j = mineralIdx; j < newMineralIdx; j++) {
                    tempSum += mineralNums[j] < pickaxeNum ? 5 : 1;
                }
            } else if (pickaxeNum == 2) {
                for (int j = mineralIdx; j < newMineralIdx; j++) {
                    tempSum += mineralNums[j] == 0 ? 25
                            : mineralNums[j] == 1 ? 5
                                    : 1;
                }
            }

            dfs(pickaxeArr, mineralNums, newMineralIdx, tempSum, pickCnt + 1);

            pickaxeArr[i] = pickaxeNum;

        }
    }

    private int[] getPickaxeArr(int[] picks) {
        int len = 0;
        for (int i : picks)
            len += i;
        int[] temp = new int[len];
        int tempIdx = 0;
        for (int i = 0; i < picks.length; i++) {
            for (int j = 0; j < picks[i]; j++) {
                temp[tempIdx++] = i;
            }
        }
        return temp;
    }

    private int[] mineralToNum(String[] minerals) {
        int[] result = new int[minerals.length];
        for (int i = 0; i < result.length; i++) {
            result[i] = map.get(minerals[i]);
        }
        return result;
    }
}