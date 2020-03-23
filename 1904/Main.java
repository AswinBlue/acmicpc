import java.util.Scanner;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		int N = input.nextInt();

		ArrayList<Integer> arr = new ArrayList<>();
		arr.add(0);
		arr.add(1);
		arr.add(2);
		arr.add(3);
		// 1 2 3 5 8 13 21 ...
		
		for (int i = 4; i <= 1000000; i++) {
			arr.add((arr.get(i - 2) + arr.get(i - 1)) % 15746);
		}
		System.out.println(arr.get(N));
	}
}
