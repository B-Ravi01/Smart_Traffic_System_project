public class q4 {
    public static void main(String[] args) {
        //a
        int num = Integer.parseInt(args[0]);

        if (num > 0)
            System.out.println("Positive");
        else if (num < 0)
            System.out.println("Negative");
        else
            System.out.println("Zero");
        //b
                int a = Integer.parseInt(args[0]);
                int b = Integer.parseInt(args[1]);

                if (a % 10 == b % 10)
                    System.out.println("true");
                else
                    System.out.println("false");
            }
        }


