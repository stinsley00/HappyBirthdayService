# A Happy Birthday MicroService
# an almost production ready service for Birthdays. 
#         iiiiiiiiii
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    ~~~~~~~~~~~~~~~~~~~
#    A service responsible for emailing people on their birthdays.
#
* if this were the real deal, I'd connect to aws secrets / thycotic for passwords
* make a helm chart for a kubernetes cron
* write out to an sns queue or something for the emails. 
* have a pretty html Birthday email template so people don't vomit


Requirements: 
postgresql installed. 
python 3.7


Test Db table on localhost
```CREATE TABLE if not exists public.person (
	date_of_birth date NULL, --IRL this would likely be epoch time
	person_name varchar NULL,
	person_email varchar NULL, 
	id uuid not NULL);```

populate some data. 
```
INSERT INTO public.person (date_of_birth, person_name, person_email, id) VALUES('1990-06-20'::Date, 'local smokey', 'lsmokey@example.com',gen_random_uuid());
INSERT INTO public.person (date_of_birth, person_name, person_email, id) VALUES('1983-01-12'::Date, 'makers mark', 'mmark@example.com',gen_random_uuid());
INSERT INTO public.person (date_of_birth, person_name, person_email, id) VALUES(now()::Date, 'wild turkey', '101@example.com',gen_random_uuid());
```