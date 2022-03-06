package round666Div2;

import java.io.*;
import java.util.*;
 
 
public class B{
 
//	public static Reader sc = new Reader();
	public static FastScanner sc = new FastScanner();
	//public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	
   public static void main(String[] args) throws IOException{
	//BufferedReader br = new BufferedReader(new FileReader("input.in"));
 
	int n = sc.nextInt();
	Long[] a = new Long[n];
	for (int i = 0; i < n; i++) {
		a[i] = sc.nextLong();
	}
	Arrays.sort(a);
	// If anything exceeds pow(10,15) then stop.
	List<Integer> powerBase = new ArrayList<Integer>();
	powerBase.add(0);
	powerBase.add(1);
	int c = 2;
	while (true) {
		long base = c;
		boolean works = true;
		//try finding a possible base, but not reach max pow 
		for (long i = 1; i < n; i++) {
			base *= c;
			if (base > pow(10,15)) {
				works = false;
				break;
			} 
		}
		if (!works) break;
		powerBase.add(c); //if the base is found, add to list
		c++;
	}
	//finding min cost - find for all the possible base, which has the min cost
	long minCost = Long.MAX_VALUE;
	for (int b : powerBase) {
		long cost = 0;
		for (int i = 0; i < n; i++) {
			cost += Math.abs(a[i]-pow(b, i));
		}
		minCost = Long.min(cost, minCost);
	}
	System.out.println(minCost);
	
	
	System.out.close();
   }
   static long ceil(long a, long b) {
		return (a+b-1)/b;
	}
  
   static long powMod(long base, long exp, long mod) {
	   if (base == 0 || base == 1) return base;
	   if (exp == 0) return 1;
	   if (exp == 1) return base % mod;
	   long R = powMod(base, exp/2, mod) % mod;
	   R *= R;
	   R %= mod;
	   if ((exp & 1) == 1) {
		   return base * R % mod;
	   }
	   else return R % mod;
   }
   
   static long pow(long base, long exp) {
	   if (base == 0 || base == 1) return base;
	   if (exp == 0) return 1;
	   if (exp == 1) return base;
	   long R = pow(base, exp/2);
	   if ((exp & 1) == 1) {
		   return R * R * base;
	   }
	   else return R * R;
   }
	static class FastScanner {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");

		String next() {
			while (!st.hasMoreTokens())
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		int[] readArray(int n) {
			int[] a = new int[n];
			for (int i = 0; i < n; i++)
				a[i] = nextInt();
			return a;
		}

		long nextLong() {
			return Long.parseLong(next());
		}
	}
}

