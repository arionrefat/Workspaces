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

    void sort() {
        if (min != 0) {
            for (int i = 0; i < k.length; i++) {
                if (k[i] != 0) {
                    for (int j2 = 1; j2 <= k[i]; j2++) {
                        System.out.println(i - min);
                    }
                }
            }
        } else {
            for (int i = 0; i < k.length; i++) {
                if (k[i] != 0) {
                    for (int j2 = 1; j2 <= k[i]; j2++) {
                        System.out.println(i);
                    }
                }
            }
        }
    }

    public static void main(String args[]) {
        int[] array = { 4, -2, 3, -4, 7, 4 };
        // int[] array = { 2, 3, 4, 4, 9, 5 };

        KeyIndex keyIndex = new KeyIndex(array);
        keyIndex.sort();
        System.out.println(keyIndex.search(1));
    }

}
