class Main {

    static void testRobot(String fileName) {
        Robot robby = new Robot();
        Logger logger = new Logger();
        Room room = new Room(fileName, logger);

        while (!robby.isDone()) {
            System.out.println(room);
            room.moveRobot(robby.step(room.getRobotSurroundings()));
        }
        System.out.println(room);
        System.out.println(logger);
    }

    public static void main(String[] args) {
        for (int i = 0; i < args.length; i++) {
            testRobot(args[i]);
        }
    }
}