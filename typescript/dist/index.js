"use strict";
function checkUUID(x) {
    return /^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$/.test(x);
}
console.log(checkUUID('03b569e9-7c2b-4eaf-8eb1-9282bce55703'));
console.log(checkUUID('refat'));
