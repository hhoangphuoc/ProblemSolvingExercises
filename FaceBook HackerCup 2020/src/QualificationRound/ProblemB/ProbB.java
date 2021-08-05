package QualificationRound.ProblemB;

import java.io.PrintWriter;
import java.util.Scanner;

public class ProbB {
    static final Scanner in = new Scanner(System.in);
    static final PrintWriter out = new PrintWriter(System.out);

    public static void main(String[] args) {
        int test = in.nextInt();
        for (int i = 1; i <= test; i++) {
            out.println("Case #" + i + ": ");
            new Solver();
        }
        out.close();
    }

    static class Solver {
        Solver() {
            int n = in.nextInt();
            char[] chars = in.next().toCharArray();

            int totalA = 0;
            /*
            we can also consider calculating totalB, but it the same as totalA so it doesn't really matter
            */
            
            for (char c : chars) {
                if (c == 'A') {
                    ++totalA;
                }
            }
            /*
             Base on the pattern in the input and the output result, we see that the possible pairs of (A,B)
             can be found as: ( (n-1)/2 , (n+1)/2 ) which each element refer to total A or B.
             */
            out.println(totalA == (n - 1) / 2 || totalA == (n + 1) / 2 ? 'Y' : 'N');

        }
    }
}
