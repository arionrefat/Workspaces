console.log("Task 1: " + task1(3, 2));
console.log("Task 3: " + task3(1));
console.log("Task 5(a): ");
task5_a(1, 5);

function task1(base, n) {
    if (n == 0) return 1;
    else return base * task1(base, n - 1);
}

function task3(height) {
    if (height != 0) {
        if (height == 1)
            return 8;
        else
            return 5 + task3(height - 1);
    }
    else return "Houses cann't be build";
}

// Use node.js to run this code
function task5_a(row, input) {

    if (row > input) return;

    for (let i = 1; i <= row; i++)
        process.stdout.write(i + " ");

    console.log();
    task5_a(row + 1, input);
}

/*
    void task5_b(int row, int input) {
        if (row > input)
            return;

        for (int i = input; i > row; i--)
            System.out.print(" ");

        for (int i = 1; i <= row; i++)
            System.out.print(i);
        System.out.println();

        task5_b(row + 1, input);
    }
*/

/*
def friday(lst,a,b,idx):
k=len(lst)
if (len(lst)==1):
    return lst[0]
else:
    if a[idx]==2 or a[idx]==4:
        for i in range(0,len(lst)):
            if (lst[i]==b):
                break
        if(i<len(lst)):
            k=len(lst)-1
            for j in range(i,k,1):
                lst[j]=lst[j+1]
        return k
    b=(b+1)%len(lst)
    idx=(idx+1)%len(a)
return friday(lst,a,b,idx)
x=[1,2,3]
dice=[1,5,2]
c=0
d=0
print(friday(dice,x,c,d))
*/

function fridayFun(array, array2, val, index) {
    let arraysize = array.length;

    if (arraysize == 1) return array[0];
    else {
        if (array2[index] == 2 || array2[index] == 4) {
            for (let i = 0; i <= arraysize; i++) {
                if (array[index] == val) break;

                if (i < arraysize) {
                    let k = arraysize - 1;
                    for (let j = i; j < k; i++) {
                        array[j] = array[j + 1];
                    }
                }
                return k;
            }
            val = Math.trunc((val + 1) % array.length);
            idx = Math.trunc((idx + 1) % array2.length);
        }
    }
    return fridayFun(array, array2, val, index);
}



class FinalQ {
    static print(array, index) {
        if (index < array.length) {
            let profit = this.calcProfit(array[index]);
            console.log(`${index + 1}. Investment: ${array[index]}; Profit: ${profit}`);
            this.print(array, index + 1);
        }
    }

    static calcProfit(investments) {
        if (investments > 100000)
            return 8 + this.calcProfit(investments - 100);
        else if (investments > 25000)
            return 4.5 + this.calcProfit(investments - 100);
        else
            return 0;
    }
}
let array = [25000, 100000, 250000, 350000]
FinalQ.print(array, 0);

// task7(5, 5, [1, 1, 2, 2, 5], [3, 1, 4, 1, 5]);

function task7(arr1size, arr2size, arr1, arr2) {

    for (let i = 0; i < arr2size; i++) {

        let L = 0;
        let R = arr1size - 1;
        let count = 0;

        while (L <= R) {

            let mid = Math.trunc((L + R) / 2);

            if (arr1[mid] <= arr2[i]) {
                count = mid + 1;
                left = mid + 1;
            }
            else
                R = mid - 1;
        }
        console.log(count);
    }
}

