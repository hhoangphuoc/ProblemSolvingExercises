package round663;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B {
	
	public static void main(String[] args) {
		FastScanner fs=new FastScanner();
		int T=fs.nextInt();
		for (int tt=0; tt<T; tt++) {
			
			//read the cols and rows and fill all the cell into a board
			int h=fs.nextInt(), w=fs.nextInt();
			char[][] board=new char[w][h];
			for (int y=0; y<h; y++) {
				char[] line=fs.next().toCharArray();
				for (int x=0; x<w; x++)
					board[x][y]=line[x];
			}
			int c=0;
			
			//check in all the Rows, the cell in positions (i, m-1) must be 'R' in order to go right when they are in
			// bottom row, so that they can reach the end (n,m)
			for (int x=0; x+1<w; x++) {
				if (board[x][h-1]!='R') c++;
			}
			//check in all the Cols, the cell in positions (n-1,m ) must be 'D' so that it will go down when reach border and 
			//move to the end cell (n,m)
			for (int y=0; y+1<h; y++) {
				if (board[w-1][y]!='D') c++;
			}
			System.out.println(c);
				
			
		}
		
	}
	static class FastScanner {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer("");
		
		public String next() {
			while (!st.hasMoreElements())
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
	}
	
}
