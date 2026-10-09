Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Pre-DPI Filters

You can optimize sensor performance by filtering unnecessary traffic before doing Deep Packet
Inspection (DPI). To configure this, you create a filter to accept or drop traffic based on the IP
addresses, protocols, ports, and other packet attributes that are present in traffic. Unlike Traffic
Filters, which apply rules after the DPI engine inspects all packets, pre-DPI filters streamline
processing by discarding unnecessary data earlier. This reduces overhead and increases
throughput.

The pre-DPI filter rules that Stellar Cyber uses are based on expressions that packet capture
tools like tcpdump and Wireshark employ to define which network traffic to capture or exclude.
Stellar Cyber follows the same syntax to determine which traffic to include or exclude before
performing DPI, thereby conserving processing resources. For more information about filtering
expressions and their syntax, see TCPDUMP & LIBPCAP .

Term Definition

Usage in Stellar Cyber

Example

Expr
essio
n

A statement in valid tcpdump syntax
that defines one or more conditions for
filtering traffic.

Multiple conditions in an expression are
combined by using the operators and,
or, and not.

Rule

A set of one or more expressions with a
directive to Accept or Drop traffic.

Multiple rules in a filter are joined by
using the operator or.*

src host 10.0.0.1 and src
port 443 (one expression)

dst host 192.168.1.1 (another
expression)

(src host 10.0.0.1 and src
port 443) or (dst host
192.168.1.1)

* In Stellar Cyber, you can create a filter by entering one or more rules, each on its own line, and letting Stellar Cyber implicitly

add or between them, or you can define a rule by placing it inside parentheses and explicitly entering or between each

parenthetically enclosed rule in a single line.

To access the Pre-DPI Filter option, select System | DATA MANAGEMENT | Sensors | Sensor
Profiles | Create | Add Modular Sensor Profile or Add Standard Sensor Profile and then
enable Network Traffic and Traffic Filtering. You can also access it by editing a previously
created sensor profile.

Common Pre-DPI Filter Rules
Depending on the action you choose—Accept or Drop—the following rules define traffic
attributes that must be present for a Stellar Cyber sensor to either accept or drop traffic before
performing Deep Packet Inspection (DPI).

Filter by IP Address

This rule matches traffic originating from 10.36.22.54:

src host 10.36.22.54

This rule matches traffic destined for 192.168.1.1:

dst host 192.168.1.1

This rule matches traffic from or to 192.168.1.112:

host 192.168.1.112

The behavior of a rule in a pre-DPI filter is different if you specify the source or destination for
host, ip, or port or if you don’t specify it. The different behaviors depend on whether the traffic
is sensor-initiated or pass-through:

Sensor-initiated traffic: src { host | ip | port } and dst { host | ip | port
} do not take effect. Use host, ip, or port, which applies regardless of direction.

Pass-through traffic: src { host | ip | port } and dst { host | ip | port }
work correctly, filtering based on traffic source or destination. host, ip, and port also
work and are applied whether they are the source or destination.

Because the pre-DPI filter is stateless, you must define rules for both directions when you want
to accept or drop bidirectional pass-through traffic. For example, to block DNS traffic between a
subnet (10.1.1.0/24) and a DNS server (192.168.1.12), define a filter with rules for both
directions as shown below and set the action to Drop. The filter automatically applies an or
operator between each rule:

src net 10.1.1.0/24 and dst host 192.168.1.12 and port 53

src host 192.168.1.12 and dst net 10.1.1.0/24 and port 53

Filter by Network Range (CIDR)

This rule matches traffic for the entire 192.168.1.0/24 subnet:

net 192.168.1.0/24

Filter by Protocol

This rule matches only TCP packets:

tcp

This rule matches only UDP packets:

udp

Filter by Port

This rule matches traffic on port 443 (HTTPS):

port 443

This rule matches traffic sent to port 22 (SSH):

dst port 22

Combine Conditions and Rules with Logical Operators
When using the Pre-DPI filter in Stellar Cyber, you can enter one or more filtering rules in a
single line and in multiple lines:

Single line, where you enter a valid expression to express one or more rules and
explicitly join them by entering the logical operator or between parenthetically enclosed
rules.

Multiple lines, where each new line represents one or more rules and each line is
implicitly joined by or within the filter.

Understanding how these operators work is essential for creating effective filters:

When you combine conditions using and, all specified conditions must be met for the
rule to apply.

When you combine conditions using or, the rule applies if any of the conditions are met.

When you combine conditions using not, the rule excludes traffic that matches the
specified condition.

Use not at the beginning of a rule to negate the entire condition. Use and not within an
expression to match the first condition but exclude the second.

When entering one or more rules in a single line, you can combine multiple conditions with and,
or, or not in a parenthetically enclosed rule and then combine these rules with or.

When entering rules on separate lines, you can combine multiple conditions with and, or, or not
on each line. The filter then automatically joins all rules with or.

With either approach—rules enclosed in parentheses and explicitly joined by or or rules entered
individually on their own lines and implicitly joined by or--traffic matches the filter if it meets the
conditions defined in any of its rules.

 Filters do not work if the operators are uppercase AND, OR, NOT. They must be lowercase

and, or, not to take effect.

Example: Create a Filter with Two Rules

In this example, you want to drop HTTP and HTTPS traffic (ports 80 and 443) from 10.0.0.1 and
all traffic from 10.0.0.2. After setting the action as Drop, create a filter consisting of either two
rules in the same line or two individual rules on separate lines.

Option 1: Use a single line

If you prefer entering both rules on a single line, put each rule in parentheses and explicitly set
or as the logical operator between them:

(src host 10.0.0.1 and (src port 80 or src port 443)) or (src host
10.0.0.2)

These rules state that traffic from 10.0.0.1 is only dropped if it is on port 80 or 443 while all traffic
from 10.0.0.2 is dropped regardless of port.

Option 2: Use multiple lines

Instead of entering multiple rules on a single line, you can enter each rule on its own line:

src host 10.0.0.1 and (src port 80 or src port 443)

src host 10.0.0.2

The rules in the second option achieve the same result as those in the first option, while making
the filter a little easier to read.

Example: Create a Filter with Three Rules

In this example, you want to accept TCP traffic from the 192.168.1.0/24 network, all traffic except
SSH (port 22) from 10.0.0.5, and all traffic destined for 172.16.0.1 regardless of source or
protocol. After setting the action as Accept, create a filter consisting of either three rules on a
single line or three individual rules on separate lines.

Option 1: Use a single line

If you prefer entering all three rules on the same line, put each rule in parentheses and explicitly
set or as the logical operator between them:

(net 192.168.1.0/24 and tcp) or (src host 10.0.0.5 and not port 22) or
(dst host 172.16.0.1)

By enclosing each rule in parentheses and joining the rules with or, the filter ensures that traffic
is accepted if it matches any of the rules.

Option 2: Use multiple lines

Instead of entering all three rules on a single line, you can enter each rule on its own line:

net 192.168.1.0/24 and tcp

src host 10.0.0.5 and not port 22

dst host 172.16.0.1

The rules in the second option achieve the same result as those in the first, while making the
individual rules that constitute the filter a little clearer to read.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

