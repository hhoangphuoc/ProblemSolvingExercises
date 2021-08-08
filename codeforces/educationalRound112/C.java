package codeforces.educationalRound112;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

/**
 * Link for this exercise:
 * <a href="https://codeforces.com/contest/1555/problem/C">C.Coin Rows</a>
*/
public class C {
 
	public static void main(String[] args) {
		FastScanner fs=new FastScanner();

		int T=fs.nextInt(); // read the number of test cases
		for (int tt=0; tt<T; tt++) {

			int n=fs.nextInt();// number of columns
			int[] b=fs.readArray(n), a=fs.readArray(n); //create first and second row
			long[] aCS=new long[n+1], bCS=new long[n+1]; //aCS: suffix for the first array, bCS: prefix for the second array
			for (int i=1; i<=n; i++) aCS[i]=aCS[i-1]+a[i-1];
			for (int i=1; i<=n; i++) bCS[i]=bCS[i-1]+b[n-i];
			
			long ans=Long.MAX_VALUE;
			
			for (int split=0; split<n; split++) {
				int aTake=split;
				int bTake=n-1-split;

                // find the position that Alice will move down.
                // Choosing the max value between suffix of first row & prefix of second row
                //Loop to all the possible way down position and choose the min value.
				ans=Math.min(ans, Math.max(aCS[aTake],bCS[bTake]));
			}
			System.out.println(ans);
		}
	}
 
	static void sort(int[] a) {
		ArrayList<Integer> l=new ArrayList<>();
		for (int i:a) l.add(i);
		Collections.sort(l);
		for (int i=0; i<a.length; i++) a[i]=l.get(i);
	}
	
	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		String next() {
			while (!st.hasMoreTokens())
				try {
					st=new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			return st.nextToken();
		}
		
		int nextInt() {
			return Integer.parseInt(next());
		}
		int[] readArray(int n) {
			int[] a=new int[n];
			for (int i=0; i<n; i++) a[i]=nextInt();
			return a;
		}
		long nextLong() {
			return Long.parseLong(next());
		}
	}
 
	
}