#!/bin/sh
#
#

  echo Content-type: text/html
   cat << EOF1

<html>
<head>
<title>Build LifetimeLearning and eCFI Email List</title>
<body bgcolor="#ffffff" text="#000000" vlink="#0000ff" link="#0000ff">
<BASE TARGET="output">
</head>
<br>
<br>
<blockquote>
<hr size=1>
<center>
<b><font color=#800000 size=+2>Building LifetimeLearning and eCFI Email List</font></b>
</center>
<hr size=1>
<blockquote>
<b>
<p align=justify>
Building (LifetimeLearning-List)...<br>
`cat ./lifetimelearning-list >> /roxy/usr/local/lists/email-admin-list`
Done.
<br>
------
<br>
Building (eCFI-List)...<br>
`cat ./ecfi-list >> /roxy/usr/local/lists/email-admin-list`
Done.
<br>
------
<br>
<blockquote>
<table><tr><td nowrap><b>
LifetimeLearning-List:
<blockquote>
`ls -al /usr/home/nuckolls/emaillist/lifetimelearning-list`
</blockquote>
eCFT-List:
<blockquote>
`ls -al /usr/home/nuckolls/emaillist/ecfi-list`
</blockquote>
<br>
</b>
</td></tr>
</table>
</blockquote>
<p>
Build Complete.<p>
</blockquote>
</blockquote>
</center>
</html>

EOF1
