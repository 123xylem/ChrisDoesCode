/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    length = 0
    if(args) {
        args.forEach(a =>{length++})
    }
    return length
};


// argumentsLength(1, 2, 3, {}, '99s9s9s9s9'); // 3

