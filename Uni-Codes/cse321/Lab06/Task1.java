import java.io.BufferedReader;
import java.io.FileReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Task1 {

    public Task1() {
    }

    @Override
    public String toString() {
        return "Task1 []";
    }

    public static void main(final String[] args) throws Exception {
        final BufferedReader b = new BufferedReader(new FileReader("file1.txt"));

        final int c1 = Integer.parseInt(b.readLine());
        final int c2 = Integer.parseInt(b.readLine());

        final int[][] max = new int[c1][c2];
        final int[][] allocation = new int[c1][c2];
        final int[][] need = new int[c1][c2];
        final int[][] avail = new int[c1 + 1][c2];

        for (int i = 0; i < c1; i++) {
            final String s = b.readLine();
            final StringTokenizer st = new StringTokenizer(s, " ");
            for (int j = 0; j < c2; j++) max[i][j] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < c1; i++) {
            final String s = b.readLine();
            final StringTokenizer st = new StringTokenizer(s, " ");
            for (int j = 0; j < c2; j++) {
                allocation[i][j] = Integer.parseInt(st.nextToken());
                need[i][j] = max[i][j] - allocation[i][j];
            }
        }

        System.out.print("Need Matrix:");

        for (int i = 0; i < c1; i++) {
            System.out.println();
            for (int j = 0; j < c2; j++) System.out.print(need[i][j] + " ");
        }

        System.out.println();
        final String s = b.readLine();
        final StringTokenizer st = new StringTokenizer(s, " ");
        final LinkedList<Integer> sl = new LinkedList<>();

        int c3 = 0;
        while (st.hasMoreTokens()) {
            avail[0][c3] = Integer.parseInt(st.nextToken());
            c3++;
        }
        c3 = 0;
        for (int i = 0;; i++) {
            i = i % c1;

            for (int j = 0; j < c2; j++) {
                if (need[i][j] <= avail[c3][j]) {

                } else {
                    break;
                }
                if (j == c2 - 1 && !sl.contains(i)) {
                    for (int g = 0; g < c2; g++) avail[c3 + 1][g] = avail[c3][g] + allocation[i][g];
                    sl.addLast(i);
                    c3++;
                }
            }
            if (sl.size() == c1) break;
        }
        System.out.println("Safe Sequence:");

        for (final Integer integer : sl) System.out.print(Character.toString((char) (integer + 65)) + " ");

        System.out.println();
        System.out.print("Change in available resource matrix : ");

        for (int y = 1; y < avail.length; y++) {
            System.out.println();
            for (int y1 = 0; y1 < c2; y1++) System.out.print(avail[y][y1] + " ");
        }

        System.out.println();
        b.close();
    }
}
