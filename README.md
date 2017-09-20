# SSL certificates check script


## Requirements

* python 2.7
* openssl


## Installation

Choose any of:

* [.deb package](https://github.com/hhru/ssl-cert-check/releases/download/0.0.4/hh-ssl-cert-check_0.0.4_all.deb)
* `pip install hh-ssl-cert-check`
* Just get [hh-ssl-cert-check](./hh-ssl-cert-check) and use


## Usage

```
hh-ssl-cert-check [general arguments] command [command arguments]
```

Quick help:

```
hh-ssl-cert-check -h
hh-ssl-cert-check command -h
```

Script return codes:

* 0 - OK
* 1 - bad arguments
* 2 - certificate warning


## Commands

* `p12` - Check a certificate in a PKCS#12 container (.p12).
* `pem` - Check a PEM certificate.
* `https` - Check a HTTPS certificate by receiving it from a SSL connection. Optional SNI supported.


## License

Apache License 2.0
