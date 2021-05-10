class Tester {
    public static void main(String args[]) {
        int[] array = { 4, -2, 3, -4, 7, 4 };
        // int[] array = { 2, 3, 4, 4, 9, 5 };

        // KeyIndex keyIndex = new KeyIndex(array);
        // int[] answer = keyIndex.sort();

        // for (int i : answer) {
        // System.out.println(i);
        // }
        // System.out.println(keyIndex.search(1));

        // index = ((consonentCount * 24) + sum) % 9;

        String[] word = { "12G0", "AB1J0", "ST1E89B8A32", "11060", "ABBY1", "KLKA090", "GHUA991", "GHAA011",
                "PAN1110" };
        Hashing hash = new Hashing(word);
        hash.print();
    }
}

class KeyIndex {
    int[] k;
    int min = 0;

    KeyIndex(int[] a) {

        int temp = a[0];
        int max = 0;
        boolean flag = false;

        for (int i = 0; i < a.length; i++) {
            if (a[i] < 0) {
                flag = true;
                break;
            }
        }

        if (flag) {
            for (int i = 0; i < a.length; i++) {
                if (temp > a[i]) {
                    min = a[i];
                    temp = a[i];
                } else
                    min = temp;
            }
        }

        min = min * -1;

        for (int i = 0; i < a.length; i++) {
            a[i] = a[i] + min;
        }

        for (int i = 1; i < a.length; i++) {
            if (temp < a[i]) {
                max = a[i];
                temp = a[i];
            } else
                max = temp;
        }

        k = new int[max + 1];

        for (int i = 0; i < a.length; i++) {
            int index = a[i];
            k[index] = k[index] + 1;
        }
    }

    boolean search(int num) {

        if (num > k.length)
            return false;

        if (min == 0) {
            if (k[num] != 0)
                return true;
            else
                return false;
        } else {
            num = num + min;
            if (num < 0)
                return false;
            else {
                if (k[num] != 0)
                    return true;
                else
                    return false;
            }
        }
    }

    int[] sort() {
        int count = 0;

        for (int i = 0; i < k.length; i++) {
            if (k[i] != 0)
                count++;
        }

        int arra[] = new int[count + 1];
        int index = 0;

        if (min != 0) {
            for (int i = 0; i < k.length; i++) {
                if (k[i] != 0) {
                    for (int j2 = 1; j2 <= k[i]; j2++) {
                        arra[index] = i - min;
                        index++;
                    }
                }
            }
        } else {
            for (int i = 0; i < k.length; i++) {
                if (k[i] != 0) {
                    for (int j2 = 1; j2 <= k[i]; j2++) {
                        arra[index] = i;
                        index++;
                    }
                }
            }
        }
        return arra;
    }
}

class Hashing {
    String[] aux = new String[9];
    int index = 0;
    int sum;
    int consonentCount;

    Hashing(String[] array) {
        String tempString = "";

        // ST1E89B8A32
        for (int i = 0; i < array.length; i++) {
            sum = 0;
            consonentCount = 0;
            tempString = array[i];

            for (int j = 0; j < tempString.length(); j++) {
                char ch = tempString.charAt(j);

                if (ch >= 'A' && ch <= 'Z') {
                    if (ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U')
                        continue;
                    else
                        consonentCount++;
                }
            }

            for (int j = 0; j < tempString.length(); j++) {
                char ch = tempString.charAt(j);

                if (ch >= 'A' && ch <= 'Z')
                    continue;
                else
                    sum += (ch - 48);
            }

            index = ((consonentCount * 24) + sum) % 9;

            System.out.println(index);
            System.out.println();

            if (aux[index] != null) {
                for (int j = 0; j < aux.length; j++) {
                    if (aux[j] == null) {
                        aux[j] = tempString;
                        break;
                    }
                }
            } else
                aux[index] = tempString;
        }
    }

    void print() {
        for (String string : aux) {
            System.out.println(string);
        }
    }
}
