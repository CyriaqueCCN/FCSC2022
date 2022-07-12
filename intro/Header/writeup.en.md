We get a landing page and its source code.

Looking at it, we see it waits for a header with a special value to return the flag

Using the browser's dev tools, we resend the request with the following header :

`X-FCSC-2022: Can I get a flag, please?`

The server amiably answers back with the flag

FCSC{9ec57a4a72617c4812002726750749dd193d5fbbfeef54a27a9b536f00d89dfb}
