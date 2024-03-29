# munki_preflight

**NOTE:** these will work but only if they are munki's only *preflight* script. I used to run it via munkireport-php's preflight.d directory which was deprecated last summer.

## student_no_auto_time

This will abort munki auto runs during school hours.

This is in response to infrequently used laptops being removed from a cart and performing poorly, but is honestly something that has been on the back burner for a while.

See [Munki Preflight and Postflight Scripts][preflight] for more info.

I still want to be able to run MSC or managedsoftwareupdate by hand or have the students do so when required so this only targets 'auto' runs. Editing the launchd plists is not ideal because they may get overwritten with an update.

## Enhancements ##

I added the ability to run after 15:15 and also to auto run on weekends. This is something that I'm only likely to take advantage of at the beginning of the school year if something is **REALLY** broken, but it is a nice CYA measure. My thanks to [@rtrouton][] and [@rsaeks][] for the feedback.

## Makefile ##

The pack location for the Makefile is a subdirectory called [preflight_abort.d][abort] because I use [munkireport-php][]

See my [luggage.local][] for the relevant [lines][] (link highlights proper lines at the time of this writing)

[preflight]: https://github.com/munki/munki/wiki/Preflight%20And%20Postflight%20Scripts
[abort]: https://github.com/munkireport/munkireport-php/blob/master/docs/setup.md#advanced-client-setup
[munkireport-php]: https://github.com/munkireport/munkireport-php
[luggage.local]: https://github.com/rmanly/luggage_local
[lines]: https://github.com/rmanly/luggage_local/blob/master/luggage.local#L45-L52
[@rtrouton]: https://twitter.com/rtrouton
[@rsaeks]: https://twitter.com/rsaeks
