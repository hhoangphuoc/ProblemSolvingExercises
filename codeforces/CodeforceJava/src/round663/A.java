package round663;

 
import java.util.Scanner;

public class A {
    public static void main(String[] args) {
        Scanner scn = new Scanner(System.in);
        int cases = scn.nextInt();
        while (cases-- > 0) {
            int num = scn.nextInt();
            for (int i = 1; i <= num; i++) {
                System.out.print(i + " ");
            }
            System.out.println();
        }
    }
}
