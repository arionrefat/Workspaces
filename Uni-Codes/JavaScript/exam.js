function encodeString(word, index, rand_num, str = "") {
    if (index === word.length) return str;
    else {
        const encodedWord = (word.charCodeAt(index) + rand_num) % 122;
        str += String.fromCharCode(encodedWord);
        return encodeString(word, index + 1, rand_num, str);
    }
}
