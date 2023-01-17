public class Java {
    public static void main(String[] args) {
        for (int i = 0; i < 1e10; i++) {
            if (i % 1e9 == 0) {
                System.out.print("\u001b[36m");
                System.out.print("Java => ");
                System.out.printf("%d000000000", i / 1000000000);
                System.out.println("\u001b[39m");
            }
        }
    }
}