import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.function.Function;

class Solution {
    public int solution(int[] picks, String[] minerals) {
        return new Mine().calculateMinFatigue(picks, minerals);
    }

    private static class Mine {
        public int calculateMinFatigue(int[] picks, String[] minerals) {
            return calculateMinFatigue(
                    Picks.of(picks),
                    Minerals.of(minerals)
            );
        }

        public int calculateMinFatigue(Picks picks, Minerals minerals) {
            return minerals.digInMinFatigue(picks);
        }
    }

    private static class Minerals {
        private final List<Mineral> minerals;

        public Minerals(List<Mineral> minerals) {
            this.minerals = minerals;
        }

        public static Minerals of(String[] minerals) {
            List<Mineral> list = new ArrayList<>();
            for (String mineral : minerals) {
                list.add(new Mineral(MineralType.findType(mineral)));
            }
            
            return new Minerals(list);
        }

        public int digFrom(Pick pick) {
            int sum = 0;
            for (Mineral mineral : minerals) {
                sum += pick.dig(mineral);
            }
            return sum;
        }

        public int digInMinFatigue(Picks picks) {
            int fatigue = 0;
            int len = Integer.min(picks.size(), minerals.size() / 5 + (minerals.size() % 5 > 0 ? 1 : 0));
            List<Minerals> toDig = new ArrayList<>();
            for (int j = 0; j < len; j++) {
                toDig.add(new Minerals(minerals.subList(j * 5, Integer.min(5 + j * 5, minerals.size()))));
            }
            toDig.sort(compareTo().reversed());

            for (Minerals next : toDig) {
                Optional<Pick> pick = picks.pollFor(next);

                if (pick.isEmpty()) {
                    break;
                }
                fatigue += pick.get().dig(next);
            }

            return fatigue;
        }

        private Comparator<Minerals> compareTo() {
            return Comparator.comparingInt(a -> {
                int sum = 0;
                for (Mineral mineral : a.minerals) sum += mineral.weight();
                return sum;
                });
        }
    }

    private static class Mineral {
        private static final Map<MineralType, Function<Pick, Integer>> DIGGING = Map.of(
                MineralType.DIAMOND, Pick::digDiamond,
                MineralType.IRON, Pick::digIron,
                MineralType.STONE, Pick::digStone
        );
        private final MineralType mineralType;

        public Mineral(MineralType mineralType) {
            this.mineralType = mineralType;
        }

        public int digFrom(Pick pick) {
            return DIGGING.get(mineralType).apply(pick);
        }

        public int weight() {
            return mineralType.getWeight();
        }
    }

    private enum MineralType {
        DIAMOND("diamond", 25),
        IRON("iron", 5),
        STONE("stone", 1);

        private final String type;
        private final int weight;

        MineralType(String type, int weight) {
            this.type = type;
            this.weight = weight;
        }

        public static MineralType findType(String type) {
            for (MineralType mineralType : values()) {
                if(mineralType.type.equals(type)) return mineralType;
            }
            return null;
        }

        public int getWeight() {
            return weight;
        }
    }

    private static class Picks {
        private final List<Pick> picks;

        public Picks(List<Pick> picks) {
            this.picks = picks;
        }

        public static Picks of(int[] picks) {
            return new Picks(List.of(
                    new DiamondPick(picks[0]),
                    new IronPick(picks[1]),
                    new StonePick(picks[2])
            ));
        }

        public Optional<Pick> pollFor(Minerals minerals) {
            return picks.stream()
                    .filter(Pick::isNotEmpty)
                    .min(Comparator.comparingInt(pick -> pick.dig(minerals)))
                    .map(pick -> {
                        pick.decrease();
                        return pick;
                    });
        }

        public int size() {
            int sum = 0;
            for (Pick pick : picks)
                sum += pick.getSize();
            return sum;
        }
    }

    private interface Pick {
        int dig(Minerals minerals);

        int dig(Mineral mineral);

        int digDiamond();

        int digIron();

        int digStone();

        void decrease();

        boolean isNotEmpty();

        int getSize();
    }

    private static abstract class AbstractPick implements Pick {
        protected MineralType mineralType;
        protected Integer count;

        public AbstractPick(MineralType mineralType, int count) {
            this.mineralType = mineralType;
            this.count = count;
        }

        @Override
        public int dig(Minerals minerals) {
            return minerals.digFrom(this);
        }

        @Override
        public int dig(Mineral mineral) {
            return mineral.digFrom(this);
        }

        @Override
        public void decrease() {
            count--;
        }

        @Override
        public boolean isNotEmpty() {
            return count > 0;
        }

        @Override
        public int getSize() {
            return count;
        }
    }

    private static class DiamondPick extends AbstractPick {
        public DiamondPick(int count) {
            super(MineralType.DIAMOND, count);
        }

        @Override
        public int digDiamond() {
            return 1;
        }

        @Override
        public int digIron() {
            return 1;
        }

        @Override
        public int digStone() {
            return 1;
        }
    }

    private static class IronPick extends AbstractPick {
        public IronPick(int count) {
            super(MineralType.IRON, count);
        }

        @Override
        public int digDiamond() {
            return 5;
        }

        @Override
        public int digIron() {
            return 1;
        }

        @Override
        public int digStone() {
            return 1;
        }
    }

    private static class StonePick extends AbstractPick {
        public StonePick(int count) {
            super(MineralType.STONE, count);
        }

        @Override
        public int digDiamond() {
            return 25;
        }

        @Override
        public int digIron() {
            return 5;
        }

        @Override
        public int digStone() {
            return 1;
        }
    }
}