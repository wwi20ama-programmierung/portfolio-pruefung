import java.util.ArrayList;
import java.util.List;

public class Logger {
    private List<IntPair> positionHistory = new ArrayList<>();

    public void moveRobot(IntPair nextPosition) {
        this.positionHistory.add(nextPosition);
    }

    public String toString() {
        String result = "";
        for (IntPair c : positionHistory) {
            result += c.toString() + ",";
        }
        return result;
    }
}