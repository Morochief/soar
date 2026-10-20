# Stellar Cyber 7.0 Product Update Transcript

> **Documento:** 7_0_product_update_transcript.pdf  
> **Total Páginas:** 7  
> **Tipo:** Transcripción Oficial Stellar Cyber Academy (Markdown)

---

<!-- Página 1 -->

SCO-UPDATE-7.0-v1 
7.0.0 Product Update Transcript 
 
Part 1: Introduction (01m:45s) 
 
00:00-01:45 
Welcome and thank you for joining us. Every release matters, but 7.0 is one we are especially proud 
of. So, before we get into everything that is new, let me take you back to how we got here. 
This is the road to 7.0. It began with machine learning, then geo and asset mapping, SaaS scale, 
graph correlation, and threat intelligence. Then came the autonomous SOC, each step steeper 
than the last, and today it leaves the ground. This is Stellar Cyber 7.0, agentic AI for any 
environment, any use case. It comes with three promises. It runs where you run. Its agents work 
across your SecOps, and you set the guardrails. Agentic AI across your whole SecOps platform. 
Generation seven starts now. Here is how 7.0 delivers on it. At the heart of the release, the 
autonomous SOC takes real steps toward Agentic. MCP goes generally available, evidence linkage 
makes every AI finding auditable, the AI assistant gains live data analytics, and you get far more 
control over what the AI works and where. Around it, the platform gets broader and sharper. 
Parser Studio reaches general availability, detection engineering steps up with a daily, AI-assisted 
emerging threats pipeline and new SLA tracking, and there is more across detections, integrations, 
sensors, and a new dashboard experience. That is a lot of ground, so let us get into it. 
 
Part 2: Autonomous SOC (10m:45s) 
 
00:00-01:00 
I will start with the autonomous SOC, then hand over to my colleagues for the rest. It is a milestone 
many of you have been waiting for. The autonomous SOC now running on-premises. It is available 
through our early access program. Here is how your data flows. It starts in your environment. 
Telemetry, alerts, and logs from your network, endpoints, and cloud stream into the on-prem Data 
Processor. Raw data is handed to the Stellar AI back end running on Oracle Cloud in your local 
region. There, it is aggregated and stripped down. Only the minimized security context is extracted, 
and every hop is encrypted. Observables are checked against threat intel services for added 
metadata. That context goes to OpenAI as a single, stateless request. Nothing is retained. No 
models are trained. The verdict returns in seconds.  
 
01:00-02:00 
The finished verdict, summary, and analysis flow back to your on-prem Data Processor. 
Autonomous alert triage on-premises, your data stays yours. In 7.0, we are answering one of the 
most common requests we hear. Let me decide which cases the AI works and how. Here is the 
idea. A case queue is a rule-based view of your cases built with a simple query builder. You pick the 
cases you care about by any attribute: severity, tenant, alert type, data source, and more. What is

---

<!-- Página 2 -->

SCO-UPDATE-7.0-v1 
new in 7.0 is what you attach to that queue. For each queue, you decide what the AI does: simply 
analyze and summarize the cases or fully auto triage them, reaching a verdict on each one. Let me 
show you. First, the cases I want fully triaged. I create a queue in my Stellar Cyber tenant and set the 
condition.  
 
02:00-03:00 
Severity is high or critical. Everything matching flows into this queue. Then I switch auto triage on. 
From now on, those cases get the deep AI investigation and verdict automatically. Now the other 
side. For another tenant, I create a second queue. I will call it case analysis only with its own 
condition. And this time, I turn on case summary and leave auto triage off. Those cases get 
analyzed and summarized without consuming auto triage. So, you decide queue by queue which 
cases qualify and then whether they are analyzed or fully auto triaged. And that is exactly the 
control our MSSP partners have been asking for. It lets them package auto triage into their own 
service, bundle it, offer it as a premium tier or turn it on only for specific tenants. Of course, letting 
the AI triage more of your cases only matters if you trust the verdicts it returns.  
 
03:00-04:00 
So next, let us look at how 7.0 earns that trust. It comes down to one thing every analyst values, 
proof. Here is the idea in one picture, what the AI says and the records that prove it. In 7.0, we 
connect the two for you. Every claim the AI can back with a query now carries a link straight to it. 
One click and you are in threat hunting with the exact query, and the exact time window, already run. 
When a finding is built from several checks, each one gets its own link. So, you can confirm any 
piece independently and see exactly how it fits together. And where the AI is reasoning rather than 
querying, it tells you so. In plain language, you always know what is backed by data and what is 
inference. Because every link you confirm builds real calibrated trust.  
 
04:00-05:00 
First you check it, then you spot check it, then you let it act. Let me show you what that looks like on 
an actual case. This one is a true positive, an external brute force that landed a successful login. 
And the finding says that same address is running broad internal port scans, host after host across 
199 ports. See the highlighted phrases? Those are the evidence links. I hover over many internal IPs 
and up comes the exact query the AI ran. Scope to this tenant, this address, and the exact window it 
checked. I can copy it or open it in one click. I click open in Threat Hunting. The page opens, already 
populated, already run, low-volume connections from that one address, fanning out host after host 
across 199 ports, a few hundred bytes each. That is not a login. That is a port scan, exactly what the 
AI said.  
 
05:00-06:00 
Assertion to evidence in seconds. And you can go deeper. Expand any record for the full detail. 87 
fields of metadata, threat intel enrichments, geolocation. The AI showed its work, and now you have 
seen the receipts. Two things on screen. On the left, the case you are triaging. The alerts that 
correlated, the verdict, the findings. On the right, everything else your tenant has seen. Every event, 
whether or not it made it into this case. Up to now, the assistant lived entirely on the left. It could 
explain the case to you very well, but only the case. And the question an analyst actually has almost

---

<!-- Página 3 -->

SCO-UPDATE-7.0-v1 
never stops at that boundary. Is this normal for this user? Has this address done this before? The 
case cannot tell you; it was never in scope. So now it crosses. You ask in plain language and the 
assistant writes a query and reads the live records, right then, on demand. None of this was 
precomputed.  
 
06:00-07:00 
The question decides what gets fetched. Then it does the part that used to be your afternoon. 
Thousands of raw records counted, grouped, and ranked over time, reduced to a clear pattern. This 
is the manual work that sat between an analyst question and their answer, and the reason people 
stopped asking at all. And then that pattern turns into what it means, not a result set, a sentence. 
What is concentrated, what is anomalous, what the baseline is, and attached to it, the source it 
queried, the time range, and how many records it actually read, so you can check the work rather 
than take its word. That is the shift. You ask past the boundary of the case, and you get an answer 
instead of a search to go run. Read only your data, your tenant, every number traceable to a query 
that actually executed.  
 
07:00-08:00 
And if it cannot reach an answer, it tells you; it does not invent one. Here is an example. A login 
location anomaly on one external address. The assistant lives right in the case, and it answers the 
question the case cannot. It flags that something is anomalous, but not what normal looks like. So, 
list every login location for this address ranked by count. Four locations, 97 logins from London, 52 
more from London, then it falls off a cliff, two from the US, and one from Frankfurt. One hundred 
fifty-two events over seven days. That shape is the finding. This address lives in London and only 
touched two other places. And here is what makes it usable in a SOC. The analysis details show the 
actual query it ran. Three indices matched on the address filtered to logins, seven days, 152 events.  
 
08:00-09:00 
Not a summary, the query itself. I can read it, check it, and see exactly why the number is what it is. 
Second question. And notice I do not repeat the address. It carries the context. Any alerts for this 
address in the last seven days and are they bursty? Four alerts, all inside the same one-hour 
window, around seven in the evening on the sixth, nothing the rest of the week. So, bursty. It 
characterized the pattern over time, not just a list. That is the difference between retrieval and 
analysis. Two questions, about a minute, and I never left the case. Context I would have spent ten 
minutes assembling by hand. And the guardrails matter. Read only, your data, your tenant, a query 
shown for every answer.  
 
09:00-10:00 
And if it cannot reach one, it says so instead of inventing it. That is the assistant we built for you: 
capable and fully guard railed. But not every team wants to use our AI. Some want to build their own 
on top of Stellar Cyber. And that is what the last piece of 7.0 is all about. Since we opened the MCP 
early access program this year, customers showed us what they would build with it. Four patterns 
emerged. First, multi-tenant SOC acceleration, MSSPs correlating alerts across every tenant at once, 
cutting the time analysts spend gathering context. Second, custom AI agents, customers pairing

---

<!-- Página 4 -->

SCO-UPDATE-7.0-v1 
MCP with their own AI stack, their models, and their data fully under their control. Third, data 
extraction, feeding Stellar Cyber data straight into their own reports and the tools they already run.  
 
10:00-10:45 
And fourth, red-team automation, verifying that simulated attacks are actually caught by their 
detections. The through line? Customers do not want us to build every AI workflow for them. They 
want a scoped, secure way to build their own. That is exactly what MCP is. And today, it is generally 
available, on by default, every customer, SaaS and on-prem. And that is the autonomous SOC in 7.0. 
But it all starts with detection. So let me hand over to my colleague Thomas for what is new in 
detections and detection engineering. Thomas, over to you. 
 
 
Part 3: Detection (05m:15s) 
 
00:00-01:00 
Thank you, Christophe. Now let us talk about some key detection improvements in 7.0. When a new 
campaign breaks, the research goes public fast. Independent researchers publish indicators within 
hours. Feeds carry them along quickly too, hours to days, depending on the feed. The slow part has 
never been publication. It is turning intelligence into a shipped detection. In 7.0, an AI agent works 
the front of that timeline. New indicators reach detections inside 24 hours, hands off, and every 
technique is matched against a bundled MITRE catalog and evidenced in the source data. This is 
how the pipeline works. Every day, the agent reads about 45 curated research feeds, EDR vendors, 
national labs, emergency response teams, and independent research units. What it extracts is 
enriched against a bundled MITRE catalog.  
 
01:00-02:00 
Real threat actor names and tactics are filled in. Techniques are confirmed against the source data. 
Details are enriched with appropriate context. This becomes a knowledge graph. Intrusion sets, 
malware, and the relationships between them, not flat keyword tags. That drives detections. Update 
it every twenty-four hours with no manual review. Sigma-based rules and behavior detections are 
currently under research. While not a 7.0-native feature, you will see this new feed populating 
detections shortly after the 7.0 release. Account takeover almost always begins with a login from 
somewhere new, but alerting on every new IP address is a dead end. People roam, home, office, 
mobile, VPN, a coffee shop. We measured it.  
 
02:00-03:00 
An IP-based version fired on 2% of logins, 800 alerts a day at one customer. So the detection moves 
up one level to the ASN, the network operator behind the address. A person rarely changes 
operator. An attacker almost always does. Same signal, a third of a percent, about six and a half 
times less noise. And one clean alert the moment a Microsoft 365 login arrives from a network that 
account has never used. Sensitivity is tunable per environment through options such as ASN history 
and the number of training days. Pass the ticket is a quiet way to move through a network. When a 
user signs in, the domain controller issues their machine a Kerberos ticket. That is Event 4768. The

---

<!-- Página 5 -->

SCO-UPDATE-7.0-v1 
correlation engine records where it was issued. This account, this host. An attacker on another 
machine steals that ticket and replays it. No password needed.  
 
03:00-04:00 
Their host asks the domain controller for a service ticket. Event 4769. The engine checks: Has that 
address ever held a ticket for this account? No. Then it rules out the innocent explanations: a 
service account, the same subnet, a shared server, a DHCP change. None apply, so it raises 
possible pass-the- ticket attack. Correlation, not machine learning, so it is working a day after you 
turn it on. Automated brute-force tools hammer SSH and abort each connection before the login 
finishes. Previous detections counted completed attempts. They needed a login result field, and an 
aborted session does not have one. So those sessions were skipped, leaving a blind spot. Now the 
detector reads the raw network traffic directly. Fifteen aborted SSH sessions against one 
destination inside five minutes is a fingerprint.  
 
04:00-05:15 
A model scores the traffic shape, bytes, packets, duration, to confirm it. This is not a new alert to 
learn. It adds a subtype aborted SSH network events to the three brute force detections you already 
use. When an IDS alert fires, the first question is often, what was actually in that traffic? Until now, 
answering it meant getting onto the sensor by command line, pulling a packet capture and decoding 
it. This added minutes to each alert. In 7.0, the readable payload sits on the alert itself, pretty-
printed in the Overview and Details tabs, raw in the JSON tab. You can search it in threat hunting. It 
travels with the case, and autotriage uses it as evidence. Seconds instead of command-line 
archaeology, and full PCAP has not changed. It is still there when the question is forensic rather 
than operational. 
 
Part 4: SOC Metrics: MTTA & MTTR (01m:15s) 
 
00:00-01:5 
Next, let us review automated case metrics we added in this release. Every SOC gets judged on two 
numbers, how fast you acknowledge a case and how fast you resolve it. In 7.0, those clocks live on 
the case. Start from the built-in templates, time to acknowledge, respond, and resolve, or define 
your own. You choose the field and value that starts the clock, what pauses it, and what stops it. 
Turn a metric on, and every case times itself, acknowledged at 7:10, resolved at 8:47. No manual 
time stamps. No rebuilding the timeline afterward. You see it where you already work. MTTA and 
MTTR are columns in the case list, and you can save that as a view so the whole team scans the 
same two numbers. On the case itself, the metrics pill opens the tracking panel: each timer, its 
state, and its total. The analyst sees exactly what the manager scans. That is step one, case 
metrics you define and control, with goals and reporting coming in future releases. 
 
Part 5: Connectors & Integrations (03m:30s) 
 
00:00-01:00

---

<!-- Página 6 -->

SCO-UPDATE-7.0-v1 
Thank you, Thomas. Now let us take a look at what is new with connectors and parsers in 7.0. In 
version 7.0, we are adding seven new connectors and response actions along with 14 
improvements to existing ones, deepening coverage across endpoint, privileged access, network, 
and cloud environments while continuing to harden the reliability of what is already there. On the 
parser side, 11 new parsers joined the platform with 20 improvements across existing ones, 
bringing in everything from OT and storage systems to observability telemetry, so more of your 
environment shows up as structured and actionable data. Together, these updates push the 
platform closer to a complete picture: more of your stack covered, more automated response 
options available, and fewer gaps for threats to hide in. ThreatDown Nebula is a new single-tenant 
API connector that brings Malwarebytes endpoint protection platform into Stellar Cyber. For MSSPs 
managing dedicated environments, this means endpoint telemetry feeding directly into detections.  
 
01:00-02:00 
Next is Trend Micro Vision One. We have migrated from the V2 to V3 API, which keeps the 
integration current, but more importantly, unlocks Vision One Pro support and expands the 
response actions available to analysts directly from the platform. Idira Privilege Cloud, formerly 
known as CyberArk, now flows PAM audit logs into Stellar Cyber. That covers privileged session 
activity, password lifecycle events, and access failures. For teams needing visibility into insider 
threats, having that identity layer alongside your security telemetry changes what you can correlate. 
On the enhancement side, Fortinet gains block and unblock URL response actions, ESET now 
resolves endpoint UUIDs from Cato event IPs for automated response routing, and Cloudflare 
expands to pull in WAF events, adding web application layer visibility. Seven updates, each one 
closing a gap in your existing stack.  
 
02:00-03:00 
Fewer context switches and more response from within the platform. The parser library in version 
7.0 adds 11 new parsers spanning privileged access, network infrastructure, storage, and security 
telemetry backed by 20 improvements to existing coverage. On the new parsers front, Claude OTel, 
covering both Code and Cowork, is the first step toward bringing AI platform activity into your 
security environment. As AI tooling becomes part of everyday workflows, having that telemetry 
normalized and feeding into detections matters. Cisco Secure Workload brings in network 
infrastructure telemetry from enterprise-grade environments. For storage and infrastructure, Dell 
PowerMax and IBM TS4500 add log coverage from environments that have historically been 
outside the SOC's visibility. Check Point WAF (formerly CloudGuard WAF) rounds out web 
application layer coverage, with six additional parsers, further expanding the library.  
 
03:00-03:30 
On the improvement side, ManageEngine PAM360, VMware ESXi, Barracuda CloudGen Firewall, and 
Symantec Messaging Gateway receive expanded coverage and normalization, alongside 12 
additional improvements across parsers including F5, WatchGuard, and DefensX. More of the 
environment covered, more consistently, with better structured data feeding detection, correlation, 
and investigation across the platform.   
 
Part 6: Parser Studio (02m:30s)

---

<!-- Página 7 -->

SCO-UPDATE-7.0-v1 
 
00:00-01:00 
Parser Studio goes GA in version 7.0, one of the most anticipated milestones on our roadmap. This 
is the shift from waiting on us to ship a parser, to building it yourself, on your timeline, for your 
environment. Let us walk through the features. Before we dive into what is new, a quick recap of 
Parser Studio for anyone who is joining us for the first time. Parser Studio is a guided, AI-assisted 
workflow that takes you from a raw log sample to a fully normalized, deployed parser. It works in 
four steps. First, you upload your raw log sample exactly as it would arrive from the source. Parse 
this data, where AI assistance is at your disposal to speed up this process. Normalize the fields to 
Stellar Cyber's schema and optionally apply enrichment logic for anything custom. Once complete, 
your parser is saved, ready to be enabled from the Parser Studio library. Let us see what we are 
shipping with GA to make it streamlined. First, we have create from scratch.  
 
01:00-02:00 
You no longer need to clone an existing parser as a starting point. You can now build directly from a 
blank slate. Once you choose this option, the underlying workflow remains the same four-step 
process. Next up is download and upload. Once you have built a parser in Parser Studio, you can 
now download it directly from the Management page. That means if you need to onboard the same 
log source across multiple tenants, you can simply upload the same parser and you are up and 
running. And last, bulk enable and disable. As your parser library grows, so does the noise from 
parsers that are no longer actively ingesting data. The Management page now gives you a 
threshold- based slider: surface everything below your ingestion threshold over the last seven days 
and bulk disable them in one action. And beyond just housekeeping, disabling inactive parsers also 
frees up sensor memory so your active data sources get the resources they need. Here is what to 
expect in the subsequent releases after GA. 
 
02:00-02:30 
AI assistance for parsing and normalization, making the workflow even faster for complex log 
formats Additional format support, starting with KVP, JSON, CEF and Regex. Multi-sample 
validation, so you can test your parser against multiple log samples before deploying. Smart Index 
recommendation, index suggestions based on your log structure, right within the workflow. With 
that, I will hand it over to Christophe. 
 
 
Part 7: Release Overview (01m:00s) 
 
00:00-01:00 
That is 7.0. We wanted the Autonomous SOC to be more capable and more yours. It runs where you 
need it. It shows its evidence when you question a verdict and it triages only the cases you choose. 
Sharper detections and Parser Studio round it out. It is a release we are proud to hand you. Try it 
and tell us what works and what does not. That is what shapes the next one. Thanks for your time 
today. As always, your feedback drives what we build. So please keep it coming and you can 
always reach us afterward directly or through Support. Thanks again for your time today. We look 
forward to seeing how you use these new capabilities to secure your environments.

---

