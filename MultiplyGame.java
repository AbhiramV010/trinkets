import java.util.Scanner;

class MultiplyGame {
	public static void main(String[] args) {
		System.out.println("Multiplication Game, type 9999 to stop");
		int score = 0;
		int ctr = 0;
		while (true) {
			int m1 = (int)(Math.random() * 7);
			int m2 = (int)(Math.random() * 13);
			
			Scanner sc = new Scanner(System.in);
			System.out.printf("%d x %d >> ", m1, m2);
			int a = sc.nextInt();
			ctr++;
			
			if (a == 9999) {
				sc.close();
				System.out.printf("You got %d out of %d",score, ctr);
				
				System.exit(0);
			}
			else if (a == m1*m2) {
				score++;
				System.out.println("+1");	
			}
			else {System.out.println("X");}
			sc.nextLine();
			
		}
	}	
}