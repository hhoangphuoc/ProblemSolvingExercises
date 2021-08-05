package QualificationRound.ProblemC;

import java.io.PrintWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class C {
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
            Pair[] a = new Pair[n];
            for (int i = 0; i < n; i++) {
                a[i] = new Pair(in.nextInt(), in.nextInt());
            }
            //sort the entire array by increasing position.
            Arrays.sort(a);

            //create Dynamic Programming:
            Map<Integer, Integer> dp = new HashMap<Integer, Integer>();
            int ans = 0;
            
            for (int i = 0; i < n; i++){
                int x = a[i].a - a[i].b; // the previous position of the first ( subtracted by it height)
                int y = a[i].a; // the first position itself.

                //finding max length of 2 close position x and y
                // ans can be either P_(i + H_(i)) or P(i) + H_(i) (the new length of x after cutting down or the position of y)
                ans = Math.max(ans,Math.max(dp.getOrDefault(x, 0), dp.getOrDefault(y, 0)) + a[i].b); 

                //update the position ( x, y)
                //the new position is max of the new value or the old position + height.
                dp.put(y + a[i].b, Math.max(dp.getOrDefault(y, 0) + a[i].b , dp.getOrDefault(y + a[i].b , 0)));
                dp.put(x + a[i].b, Math.max(dp.getOrDefault(x, 0) + a[i].b , dp.getOrDefault(x + a[i].b , 0)));
            }
            out.println(ans);
        }
        class Pair implements Comparable<Pair> {
            int a, b;
            Pair(int a, int b) {
                this.a = a;
                this.b = b;
            }
            @Override
            public int compareTo(Pair o) {
                return a == o.a ? b - o.b : a - o.a;
            }
        }
    }

}
