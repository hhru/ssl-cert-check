# Changelog

## 0.0.4 (2017-09-20)

* fix getting current user login when running from crontab
* add `--password-file` option

## 0.0.3 (2016-07-20)

* add an `--seconds-until-expiration` option for printing certificate expire
  time to stdout

## 0.0.2 (2016-07-12)

* initial release
* check expire day in certificates
* supports an PKCS#12 container (.p12), a PEM, a certificate from
  an SSL connection
* send email if certificate is about to expire

