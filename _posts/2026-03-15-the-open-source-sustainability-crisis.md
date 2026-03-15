---
title: "The Open Source Sustainability Crisis: We're All Free-Riding, and Nobody's Talking About It"
date: 2026-03-15 15:35:00 +0800
categories: [Technology, Open Source]
tags: [open-source, sustainability, software, industry]
---

# The Open Source Sustainability Crisis: We're All Free-Riding, and Nobody's Talking About It

Here's an uncomfortable truth about modern software: the foundation it's built on is cracking.

Every Fortune 500 company, every billion-dollar startup, every government agency runs on open source software. OpenSSL. Log4j. curl. The Linux kernel. These aren't nice-to-haves — they're load-bearing walls in the infrastructure of the internet.

And many of them are maintained by a handful of people, working in their spare time, for free.

## The numbers don't add up

Let's do some math.

OpenSSL is used by approximately 85% of all web servers. It had, until recently, a single full-time maintainer. The Heartbleed bug in 2014 — which exposed hundreds of millions of passwords — existed in a codebase maintained by two people with a combined budget of a few hundred thousand dollars.

Compare this to the companies that depend on it. Apple's market cap: $3 trillion. Google's: $2 trillion. Microsoft's: $3 trillion. Each of these companies deploys OpenSSL across millions of devices and servers.

The ratio of value extracted to value contributed is not 10:1 or 100:1. It's closer to 1,000,000:1.

## Why smart people don't maintain open source

Open source maintenance is not glamorous work. It's:

- **Reviewing pull requests** from strangers who don't follow your coding standards
- **Responding to issues** filed by people who haven't read the documentation
- **Fixing security vulnerabilities** that you didn't create and don't understand
- **Releasing versions** for platforms you don't use
- **Being blamed** when things break, regardless of whether they're your fault

Meanwhile, the same skills that make a good maintainer make $200,000+ at a tech company. The opportunity cost is enormous and growing.

## The "passion" trap

The open source community has long relied on a narrative of passion: people build things because they love it, and maintain them because they care.

This narrative is both true and dangerous. It's true that passion drives the creation of open source. It's dangerous because we've used it as justification for not paying people.

"Maintainers are volunteers" is a description, not a business model. When your entire industry runs on volunteer labor, you don't have a sustainable ecosystem. You have a charity — except nobody's donating.

## Corporate "contributions" in quotes

To be fair, companies have tried. GitHub Sponsors. Open Collective. Tidelift. Corporate sponsorship programs. And these have helped — to a degree.

But the scale is off. A company might sponsor a maintainer for $1,000/month while extracting value worth $10 million/month from their work. It's the equivalent of leaving a $1 tip on a $10,000 dinner.

Some companies have gone further, employing maintainers directly. But this creates its own problems: now your infrastructure depends on a maintainer who can change jobs, be reassigned, or be laid off. The bus factor isn't solved; it's just shifted from "volunteer with no backup" to "employee at one company."

## What would actual sustainability look like?

True open source sustainability would require a fundamental shift in how we think about software infrastructure:

### 1. Mandatory infrastructure funding

If a company derives more than $X million from open source dependencies, a percentage should flow back to those projects. This isn't charity — it's infrastructure maintenance, like paying for roads you drive on.

### 2. Professional maintainer roles

Open source maintainers should be recognized as professionals, not volunteers. This means salaries, benefits, and career paths — not sponsor buttons and coffee money.

### 3. Shared maintenance pools

Instead of each company sponsoring their own favorite project, industry-wide pools could fund maintenance based on usage metrics. Like insurance, but for software infrastructure.

### 4. Standards for corporate dependency

If you ship software that depends on open source, you should be required to disclose those dependencies and contribute to their maintenance. Not necessarily money — code contributions, security audits, documentation — but *something*.

## The alternative

The alternative to sustainability is fragility. Heartbleed wasn't a one-time accident — it was a preview. The next critical vulnerability will find code maintained by three people who haven't slept properly in months and haven't been paid in years.

We've built a trillion-dollar industry on unpaid labor, and we've done it without shame. The question isn't whether the crisis will come. It's whether we'll fix the foundation before or after it collapses.

---

*Published on March 15, 2026. Ironically, this article depends on open source software for its delivery.*
