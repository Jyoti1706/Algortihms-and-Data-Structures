package HE;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class binaryQueries {
	static class FastReader {
		BufferedReader br;
		StringTokenizer st;

		public FastReader() {
			br = new BufferedReader(new InputStreamReader(System.in));
		}

		String next() {
			while (st == null || !st.hasMoreElements()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}

		int nextInt() {
			return Integer.parseInt(next());
		}

		long nextLong() {
			return Long.parseLong(next());
		}

		double nextDouble() {
			return Double.parseDouble(next());
		}

		String nextLine() {
			String str = "";
			try {
				str = br.readLine();
			} catch (IOException e) {
				e.printStackTrace();
			}
			return str;
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FastReader s = new FastReader();
		String[] sn = s.nextLine().split(" ");
		int n = Integer.parseInt(sn[0]);
		int q = Integer.parseInt(sn[1]);
		String[] arr = s.nextLine().split(" ");
		int[] arr_ele;
		arr_ele = new int[n];
		for (int i = 0; i < n; i++) {
			arr_ele[i] = Integer.parseInt(arr[i]);
		}
		for (int i = 0; i < q; i++) {
			sn = s.nextLine().split(" ");
			int len = sn.length;
			if (len == 2) {
				int temp = Integer.parseInt(sn[1]);
				if (arr_ele[temp - 1] == 0)
					arr_ele[temp - 1] = 1;
				else
					arr_ele[temp - 1] = 0;
			} else {
				if (arr_ele[Integer.parseInt(sn[len - 1])-1] == 1)
					System.out.println("ODD");
				else
					System.out.println("EVEN");
			}
		}

	}

}
