# simplesqlmapcsrfproxy

## What is 'simplesqlmapcsrfproxy'?

`sqlmap` is a wonderful piece, first of its class, when one is working on a pentest is one of the tools you should definitively use beside `nmap`, `cansina` or `metasploit` and others.

But, sometimes, we found a request we want to test but a csrf-token is needed.

`sqlmap` is intelligent enough to extract it from many places like fields, params, etc.

But in some situations (see example.py) I found that a little help will help `sqlmap` help you.

## What work it does?

Here is the purpose of 'simplesqlmapcsrfproxy':

It raises a simple http server you pass to `sqlmap`.

It makes a request to the real url you are testing and process the content scraping for the elusive csrf token.

When the token is found, it serves a mock html form with the token ready to `sqlmap` to consume.

## How does it work?

First of all:

**You need** to know how to extract the token and code a scrapper in a Python script file. Filename is up to you.

**You need** to call the main function of your module **process** and it will need to accept a **string** which hopefully will contain the html text where the token must be found.

See *example.py* it served me to extract `_glpi_csrf_token` from `meta` tags in a real case.

Next:

`simplesqlmapcsrfproxy.py <target_url> <cookie> <you_script>`

Finally, in `sqlmap`:

`sqlmap -u http://REDACTED/?_glpi_csrf_token\=f51b7042afe499bc95c4b66daffb2f534c320333096c37a36f4821181a5d1698 --cookie="glpi_REDACTED=REDACTED" --csrf-url http://localhost:54321 --csrf-token=_glpi_csrf_token`

And that's all.

## Why is the name so long?

Actually, it is shorten than `pysimplesqlmapgenericcsrftokenextractorproxy`
