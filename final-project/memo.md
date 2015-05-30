#Child-Product Recall Twitter Bot
###By Carolina, Sabrina & Jay

**Pitch:**
Scared of the toys your kids are playing with? Follow @toyrecalls for the latest child-product recalls. Make sure the play pen is safe.

**The old way:**
Previously, for a parent to figure out if a child-product had been recalled, they would have had to rely on word of mouth, or some scary segments on the evening news. If they were particularly proactive about being informed about safe toys, they could check websites like safekids.org or manually check the RSS feed compiled by the US Consumer Product Safety Commission.

*Hypothetical Situation #1:*
1. Parent is suspicious about kid toy (perhaps she says a mother-friend write a Facebook status about it).
2. Parent googles the name of that toy with "recall" to figure out if the toy or product has been recalled.

*Hypothetical Situation #2:*
1. Parent turns on the six-o'clock news and hears that a certain toy has been recalled.
2. Parent throws out that toy.

*Hypothetical Situation #3:*
1. Parent is about to go buy new toys for toddler.
2. Parent scowers the US Consumper Product Safety Commission website, making sure he/she keeps those toys or products off their list.

**The new way:**
The @toyrecalls Twitter bot will be an easy way for parents to keep up-to-date with children toys and products that have been recalled. Since more and more people are using Twitter as a source for news, and are checking it frequently, keeping current with child product safety is as easy as following the @toyrecalls Twitter account. As soon as a product has been recalled, the bot will tweet a message, alerting its followers of possible danger.

**Where does the data come from?**
The US Consumer Product Safety Commission has an updated [RSS feed](http://www.cpsc.gov/recalls/childrss) that includes a quick snippet including:
- The name of the recalled product and why it was recalled (Nantucket Distributing Recalls Mason Jar Night Light Due to Burn Hazard)
- A link to a more robust [report](http://www.cpsc.gov/en/Recalls/2015/Nantucket-Distributing-Recalls-Mason-Jar-Night-Light/?utm_source=rss&utm_medium=rss&utm_campaign=US+Consumer+Product+Safety+Commission+-+Recent+Child-Related+Product+Recalls) describing the recall further
- A more detailed, but still short description of the reason for which the product was recalled (The plastic around the base of the light bulb can melt, posing a burn hazard.)
- The date on which the product was recalled (Thu, 28 May 2015)

**What data-cleaning/processing needs to be done?**
We would have to write a program that would scrape the RSS feed and send out a tweet with a brief message about the product that was recalled & why it was recalled (so probably the title field under the "item" subheading. Maybe we would even run the report link through some type of link condesner (like bit.ly). We would then tweet this text from a Twitter account, say named "@toyrecalls".

**How will the data be stored?**
I guess our data won't really be stored, it would first have to be scraped and then immediately tweeted. But, if you did want it stored somewhere, I guess we could save the recalls in some type of text file, and then tweet from there? This would also allow there to be a larger text file or database available of all the recent tweets...although *that is* what the RSS feed is and already provides.


**Who else has done it and how is your attempt better?**
The FDA tweets out its recalls pretty efficiently, but no one tweets out specific types of recalls. This project could expand to have several subdivsions where you could follow an account that keeps you up-to-date on recalls *you* would be interested (sports/recreation products, only foods, etc.)
