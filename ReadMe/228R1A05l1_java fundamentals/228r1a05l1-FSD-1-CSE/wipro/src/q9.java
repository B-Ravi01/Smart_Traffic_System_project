public class q9 {
    public static void main(String[] args) {
        char ch = args[0].charAt(0);
        if (Character.isLowerCase(ch))
            System.out.println("Given : " + ch + "\nConverted : " + Character.toUpperCase(ch));
        else if (Character.isUpperCase(ch))
            System.out.println("Given : " + ch + "\nConverted : " + Character.toLowerCase(ch));
    }
}
