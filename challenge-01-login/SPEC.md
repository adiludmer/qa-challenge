# AcmePortal Login — Product Specification

This is the requirements document the development team worked from. Use it as the **source of truth** for what the login page is *supposed* to do. Any behavior that deviates from this spec is potentially a bug.

## Test Account

A single valid account exists for testing:

- **Username:** `qauser`
- **Password:** `Test1234!`

## Functional Requirements

### F1. Authentication
- The user signs in by submitting a username and password.
- Both fields are **required**. Submitting with either field empty must show a clear validation error and must not authenticate the user.
- Only the exact valid password `Test1234!` should authenticate the test account.

### F2. Username Handling
- Usernames are **case-insensitive**. `qauser`, `QAUSER`, and `QaUser` should all be accepted.
- **Leading and trailing whitespace** in the username field must be ignored. `  qauser  ` should authenticate the same as `qauser`.
- Usernames are limited to **50 characters**. Input longer than 50 characters must be rejected with a clear validation error.

### F3. Remember Me
- The "Remember me" checkbox, when checked at the time of a successful sign-in, must cause the username to be **pre-filled** in the username field on the next visit (i.e., when the page is reloaded).
- When unchecked, no username should be persisted across reloads.

### F4. Failed Attempt Lockout
- After **3 consecutive failed sign-in attempts**, the account must be locked for **30 seconds**.
- During the lockout window, sign-in attempts must be rejected with a message indicating the lockout and how long remains.
- A successful sign-in resets the failed-attempt counter.

### F5. Successful Sign-In
- On success, the page should display a success message.
- The user should then be redirected to `/dashboard`. *(For this challenge, displaying the success message is sufficient; no real navigation is required.)*

## Non-Functional Requirements

### N1. Security
- The user's password must **never** appear in the URL, browser history, or any other place visible outside the password field.
- The password input must mask its contents (e.g., shown as dots).

### N2. Responsive Layout
- The page must render correctly on viewport widths from **320px to 1440px**.
- All form controls and messages must remain fully visible and usable across this range.
- No element should overlap another or be cut off.

### N3. Keyboard Support
- Pressing **Enter** while focus is in the username or password field must submit the form.
- Tab order should follow the visual order: username → password → remember me → Sign In.

### N4. Accessibility
- All form fields must have associated labels.
- Form submission must be possible without a pointing device.
