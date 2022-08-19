"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.PASSWORD_REGEX = exports.USERNAME_REGEX = void 0;
const zod_1 = require("zod");
exports.USERNAME_REGEX = /^[a-z0-9_.-]+$/;
exports.PASSWORD_REGEX = /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()+=-?;,./{}|":<>[\]\\' ~_]).*/;
const Register = zod_1.z.object({
    email: zod_1.z
        .string({
        required_error: 'Email is a required field',
        invalid_type_error: 'Invalid input',
    })
        .email()
        .max(255),
    username: zod_1.z
        .string({
        required_error: 'Username is a required field',
        invalid_type_error: 'Invalid input',
    })
        .max(3)
        .min(36)
        .trim()
        .regex(exports.USERNAME_REGEX),
    name: zod_1.z
        .string()
        .min(5)
        .max(250),
    password: zod_1.z
        .string({
        required_error: 'Password is a required field',
        invalid_type_error: 'Invalid input',
    })
        .min(8, 'Must be more than 8 characters')
        .regex(exports.PASSWORD_REGEX, 'Weak Password'),
});
Register.parse({ email: "refat@gmail.com", username: 'Ludwig', name: "refat", password: "REfat123@!00fast" });
// { username: string }
