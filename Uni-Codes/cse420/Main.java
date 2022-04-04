import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = Integer.parseInt(input.nextLine());
        String[] s = new String[n];

        // s = new String[] { "dilrubashowkat@gmail.com", "www.dlrubashowkat.com.bd", "www.9anime.to" };

        for (int i = 0; i < s.length; i++) {
            s[i] = input.nextLine();
        }

        for (int j = 0; j < n; j++) {
            System.out.println(dfacheck(s[j]) + ", " + (j + 1));
        }

        input.close();
    }

    public static String dfacheck(String s) {
        int state = 1;
        boolean matched = false;
        boolean email = false;

        for (char c : s.toCharArray()) {
            switch (state) {
                case 1:
                    if (c == 'w')
                        state = 5;
                    else if (Character.isLetter(c))
                        state = 4;
                    else
                        state = 15;
                    break;

                case 5:
                    if (c == 'w')
                        state = 7;
                    else if (Character.isLetter(c) || Character.isDigit(c))
                        state = 6;
                    else
                        state = 15;
                    break;

                case 7:
                    if (c == 'w') {
                        state = 9;
                    } else if (Character.isLetter(c) || Character.isDigit(c)) {
                        state = 6;
                    } else if (c == '@') {
                        email = true;
                        state = 8;
                    } else
                        state = 15;
                    break;

                case 9:
                    if (Character.isLetter(c) || Character.isDigit(c) || c == 'w') {
                        state = 6;
                    } else if (c == '@') {
                        state = 8;
                    } else if (c == '.') {
                        state = 11;
                    } else
                        state = 15;
                    break;

                case 11:
                    if (Character.isLetter(c) || Character.isDigit(c) || c == 'w') {
                        state = 2;
                    } else
                        state = 15;
                    break;

                case 2:
                    if (Character.isLetter(c) || Character.isDigit(c) || c == 'w') {
                        state = 2;
                    } else if (c == '.') {
                        state = 12;
                    } else
                        state = 15;
                    break;

                case 12:
                    if (Character.isLetter(c) || c == 'w') {
                        state = 3;
                    } else
                        state = 15;
                    break;

                case 10:
                    if (Character.isLetter(c) || c == 'w') {
                        state = 10;
                    } else if (c == '.') {
                        state = 12;
                    } else
                        state = 15;
                    break;

                case 8:
                    if (Character.isLetter(c) || c == 'w') {
                        state = 10;
                    } else
                        state = 15;
                    break;

                case 6:
                    if (Character.isLetter(c) || Character.isDigit(c) || c == 'w') {
                        state = 6;
                    } else if (c == '@') {
                        email = true;
                        state = 8;
                    } else
                        state = 15;
                    break;

                case 4:
                    if (Character.isLetter(c) || Character.isDigit(c) || c == 'w') {
                        state = 6;
                    } else
                        state = 15;
                    break;

                case 3:
                    matched = true;
                    if (Character.isLetter(c) || c == 'w') {
                        state = 3;
                    } else
                        state = 15;
                    break;

                case 15:
                    state = 15;
                    break;
            }
        }

        if (!matched) {
            return "Invaid";
        } else {
            String res = (email) ? "Email" : "Web";
            return res;
        }
    }
}
