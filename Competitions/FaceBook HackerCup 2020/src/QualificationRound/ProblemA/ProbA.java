package QualificationRound.ProblemA;

import java.io.PrintWriter;
import java.util.Scanner;

public class ProbA {
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
            char[] incoming = in.next().toCharArray(); // write in the array of accessibility of IncomingFlight
            char[] outgoing = in.next().toCharArray(); // write in the array of accessibility of OutgoingFlight

            // check each number in the array whether it has element on the left/right or not.
            boolean[] canLeft = new boolean[n - 1], canRight = new boolean[n - 1];
            for (int i = 0; i < n - 1; i++) {
                // incoming i; outgoing i+1; (flight is set if 2 neighbor are accessibly connected )
                if (incoming[i] == 'Y' && outgoing[i + 1] == 'Y') {
                    canLeft[i] = true;
                }
                //incoming i+1, outgoing i;
                if (incoming[i + 1] == 'Y' && outgoing[i] == 'Y') {
                    canRight[i] = true;
                }
            }

            // write down the answer in the form of a matrix: P_j,k
            for (int j = 0; j < n; j++) {
                boolean[] answer = new boolean[n];
                answer[j] = true;
                // write answer in the left-side:
                int left = j;
                // if left -1 works, can go to the left
                while (left - 1 > 0 && canLeft[left - 1]) {
                    answer[--left] = true;
                }

                int right = j;
                //if right+1 works, can go to the right side
                while (right + 1 < n && canRight[right]) {
                    answer[++right] = true;
                }

                for (int k = 0; k < n; k++) {
                    out.print(answer[k] ? 'Y' : 'N');
                }
                out.println();
            }
        }
    }
}

