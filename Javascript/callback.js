const function1 = () => {
    setTimeout(() => {
        console.log('this is a word haha');
    }, 3000);
}

const function2 = () => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            console.log('thsi is a another one');

            const flag = true;

            if (!flag) resolve();
            else reject('Error: something is wrong here');
        }, 2000);
    });
};

async function inin() {
    await function2();
    function1();
}

function2().then(function1).catch(err => console.log(err));
