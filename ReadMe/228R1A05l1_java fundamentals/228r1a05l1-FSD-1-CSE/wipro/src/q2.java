public class q2 {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("No name provided.");
            return;
        }
        System.out.println("Welcome " + args[0]);
    }
}
