import { z } from 'zod';
export const USERNAME_REGEX = /^[a-z0-9_.-]+$/;
export const PASSWORD_REGEX =
  /(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()+=-?;,./{}|":<>[\]\\' ~_]).*/;

export function registerUserPayloadSchema() {
  return z
    .object({
      email: z
        .string({
          required_error: 'Email is a required field',
        })
        .email()
        .max(255, { message: 'Cannot be more than 255 characters' }),
      username: z
        .string({
          required_error: 'Username is a required field',
        })
        .max(36, { message: 'must be more than 3 characters' })
        .min(3)
        .trim()
        .regex(USERNAME_REGEX),
      name: z.string().min(5).max(250),
      password: z
        .string({
          required_error: 'Password is a required field',
        })
        .min(8, { message: 'Must be more than 8 characters' })
        .regex(PASSWORD_REGEX, 'Weak Password'),
    })
    .strict();
}

export function loginUserPayloadSchema() {
  return z
    .object({
      usernameOrEmail: z.string({
        required_error: 'Username is a required field',
      }),
      password: z.string({
        required_error: 'Password is a required field',
      }),
      remember: z.boolean(),
    })
    .strict().shape;
}

export function changeUserPasswordPayloadSchema() {
  return z
    .object({
      currentPassword: z.string({
        required_error: 'CurrentPassword is a required field',
      }),
      newPassword: z
        .string({
          required_error: 'New Password is a required field',
        })
        .min(8, { message: 'Must be more than 8 characters' })
        .regex(PASSWORD_REGEX, { message: 'Weak Password' }),
    })
    .strict()
    .refine((obj) => obj.currentPassword === obj.newPassword, {
      message: 'Passwords do not match',
      path: ['newPassword'],
    });
}

export function changeUserPasswordClientPayloadSchema() {
  return z.object({
    currentPassword: z.string({
      required_error: 'CurrentPassword is a required field',
    }),
    newPassword: z
      .string({
        required_error: 'NewPassword is a required field',
      })
      .min(8, { message: 'Must be more than 8 characters' })
      .regex(PASSWORD_REGEX, { message: 'Weak Password' }),
    confirmNewPassword: z.string({
      required_error: 'ConfirmNewPassword is a required field',
    })
  }).shape;
}

registerUserPayloadSchema().parse({
  email: 'refat@gmail.com',
  username: 'ludwig_as',
  name: 'refatul',
  password: 'REfat123@!00fast',
});

// extract the inferred type
/* type Register = z.infer<typeof Register>; */
// { username: string }
