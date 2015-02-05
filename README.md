# munki_preflight

This will abort munki auto runs during school hours.

This is in response to infrequently used laptops being removed from a cart and performing poorly but is honestly something that has been on the back burner for a while. The script is obviously quite simple but I started from not even knowing if something like this was possible.

See [Munki Preflight and Postflight Scripts][preflight] for more info.

I still want to be able to run MSC or managedsoftwareupdate by hand or have the students do so when required.

## Potential Enhancement ##

One school's final bell is actually at 15:15. Add another if statement for hour 15 to check the minutes and allow a run if after 15:25 or :30. I will probably add this if testing is successful and I push the aborting preflight to the entire district or all the student machines.

## Makefile ##

The pack location for the Makefile is a subdirectory called [preflight_abort.d][abort] because I use [munkireport-php][]

[preflight]: https://github.com/munki/munki/wiki/Preflight%20And%20Postflight%20Scripts
[abort]: https://github.com/munkireport/munkireport-php/blob/master/docs/setup.md#advanced-client-setup
[munkireport-php]: https://github.com/munkireport/munkireport-php
