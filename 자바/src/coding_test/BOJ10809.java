package coding_test;
import java.util.Arrays;
import java.util.Scanner;

public class BOJ10809 {
	public static void main(String[] args) {
		// ���ڿ� �Է¹ޱ� -> ��µ� ���ڿ� ���� -> abc?
		Scanner in = new Scanner(System.in);
		int check[] = new int[26]; // ��µ� �迭, ���ĺ� ��ġ ����ϴ� �迭
		
		// -1 �� �ʱ�ȭ
		for (int i=0;i<check.length;i++) {
			check[i]=-1;
		}
		
		// baekjoon �Է¹ޱ�
		String input = in.next();
		
		// �Է¹��� ���ڿ��� ������ ��ȯ�� �ε����� �����ֱ�����
		// �ƽ�Ű�ڵ尪������ check[tmp]�� -1�� �ƴϸ� i�� �������ִµ�
		// i�� �� �ڸ����� ��Ÿ���ֱ� ����.
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
