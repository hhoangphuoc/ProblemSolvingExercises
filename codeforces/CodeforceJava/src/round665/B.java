package round665;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class B {
    public static void main(String[] args) {
		FastScanner fs=new FastScanner();
		int T = fs.nextInt();
		for (int tt=0; tt< T; tt++) {
			int[] a = fs.readArray(3);
			int[] b = fs.readArray(3);
			int score = Math.min(a[2],b[1]); //find the min of 2s and 1s between a and b
			// to find the max possible number for pair(2,1)
			a[2]-=score;
			b[1]-=score;
			a[0]+=a[2];
			a[2]=0;
			int toSub=Math.min(b[2], a[0]);
			a[0]-=toSub;
			b[2]-=toSub;
			
			int losePoints=Math.min(b[2], a[1]);
			
			System.out.println((score-losePoints)*2);
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

