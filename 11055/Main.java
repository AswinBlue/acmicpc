import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class Main {
	public int exhausting(int N, int[] arr, int[] sum) {
		// 전수조사
		for (int i = 1; i < N; i ++) {
			for (int j = 0; j < i; j++) {
				if (arr[i] > arr[j]) {
					if (sum[j] + arr[i] > sum[i]) {
						sum[i] = sum[j] + arr[i];
					}
				}
			}
		}
		// Max 값 찾기
		int max = 0;
		for (int i = 0; i < N; i ++) {
			if (max < sum[i]) {
				max = sum[i];
			}
		}
		return max;
	}

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		// get inputs
		int N = input.nextInt();
		int[] arr = new int[N];
		int[] sum = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = input.nextInt();
			sum[i] = arr[i];
		}
	
		int max = exhausting(N, arr, sum);

		System.out.println(max);
	}
}
