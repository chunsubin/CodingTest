package coding_test;
import java.util.Arrays;
import java.util.Scanner;

public class BOJ10809 {
	public static void main(String[] args) {
		// 문자열 입력받기 -> 출력될 문자열 선언 -> abc?
		Scanner in = new Scanner(System.in);
		int check[] = new int[26]; // 출력될 배열, 알파벳 위치 기록하는 배열
		
		// -1 로 초기화
		for (int i=0;i<check.length;i++) {
			check[i]=-1;
		}
		
		// baekjoon 입력받기
		String input = in.next();
		
		// 입력받은 문자열을 정수로 변환해 인덱스를 맞춰주기위해
		// 아스키코드값을빼고 check[tmp]가 -1이 아니면 i를 대입해주는데
		// i가 곧 자릿값을 나타내주기 때문.
		for(int i=0;i<input.length();i++) {
			char c = input.charAt(i);
			int tmp = (int)c;
			tmp-=97;
			if (check[tmp]==-1)
				check[tmp]=i;
		}
		
		for(int i=0;i<check.length;i++) {
			System.out.print(check[i]+" ");
		}
	}
}
