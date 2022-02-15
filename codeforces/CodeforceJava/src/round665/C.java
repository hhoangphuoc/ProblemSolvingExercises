package round665;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Random;
import java.util.StringTokenizer;

 /**
  * Time Complexity: O(nlogn) 
  * 	- comparing elements of 2 arrays takes 0(n)
  * 	- but sorting the array beforehands take avg O(nlogn)
  * 
  *	Space Complexity: O(n) - we need n more spaces for a cloned sortedArray
  * 
  */

public class C {
	public static void main(String[] args) {
		FastScanner fs=new FastScanner();
		int T = fs.nextInt();
		outer: for (int tt=0; tt< T; tt++) {
			int n = fs.nextInt();
			int[] arr = fs.readArray(n);
			int[] sortedArr = arr.clone(); //make a copies of the array and this copies will be sorted
			
			sort(sortedArr);
			int min = sortedArr[0];
			
			for(int i = 0; i<n; i++) {
				//check for the wrong position of array compare to sortedArray
				if(arr[i] != sortedArr[i]) {
					//then, check whether it is swap by gcd() operation
					if(arr[i] % min != 0) {
						System.out.println("NO");
						continue outer; //break out to the outer for loop
					}
				}
			}
			//otherwise, this is true and we don't need to check.
			System.out.println("YES");
			
		}
	}
	static final Random random=new Random();
	
	static void sort(int[] a) {
		int n=a.length;
		//shuffle, then sort 
		for (int i=0; i<n; i++) {
			int oi=random.nextInt(n), temp=a[oi];
			a[oi]=a[i]; a[i]=temp;
		}
		Arrays.sort(a);
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
