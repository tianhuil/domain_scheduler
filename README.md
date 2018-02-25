# domain_scheduler
A domain-aware scheduler for Scrapy that round robin cycles through the domains as it outputs requests to reduce out the load on servers and accelerate scraping

## Installation
You'll need to install Scrapy (built and tested with version 1.5).  Then install this package:
```
pip install git+https://github.com/github.com/tianhuil/domain_scheduler.git@master
```

Then in `settings.py`, set
```
SCHEDULER = 'domain_scheduler.DomainScheduler'
```

*Note*: you can no longer set `SCHEDULER_PRIORITY_QUEUE`, although you can still set `SCHEDULER_DISK_QUEUE` and `SCHEDULER_MEMORY_QUEUE`.
