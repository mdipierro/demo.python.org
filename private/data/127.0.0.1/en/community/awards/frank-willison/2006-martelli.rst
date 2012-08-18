A Journey to Python
===================

.. image:: ../martelli.jpg
   :alt: ../martelli.jpg

by Alex Martelli, 2006 recipient of the `Frank Willison Award <../>`_ 

After a quarter century of experience in programming (once as a
sideline of my main job as a hardware designer, at Texas Instruments
and IBM Research, but as my main job for over half that time, at IBM
Research and Cad.Lab/think3), I finally stumbled upon Python in 1999.
This was thanks to the kind nagging of a friend and colleague whose
judgment I respected and to whom I still feel grateful for his
insistence (Alessandro Bottoni).

I had plenty of experience with languages high and low, from
microcoding (even FPGA &quot;programming&quot;, lower-level yet :-), through
assembly code for many machines, through standard &quot;high-level&quot;
languages (Pascal, Fortran, PL/I, C, C++, Java...), all the way to
&quot;higher-level&quot; languages which I had always used whenever feasible
(Rexx, APL, AWK, Icon, Perl, Scheme...).  But never had I met
something that &quot;fit my brain&quot; as perfectly as Python.

At my &quot;real job&quot;, at that time, the language *du jour* was mostly C++,
with a smattering of Visual Basic and a proprietary scripting language
that had been developed in-house and was embedded in the applications
we developed and sold.  However, in parallel, I was pursuing, at home,
a research project on the mechanics of the game of bridge (an ancient
but always-burning passion of mine) which resulted in articles
published in January and February 2000 in the extremely prestigious
magazine &quot;The Bridge World&quot; under the title &quot;How Shape Influences
Strength&quot;.  Unfortunately, the large software base underpinning that
research effort had grown &quot;organically&quot; into an unholy mix of C++,
Perl, and home-grown languages (an open-source one for dealing and
selecting bridge hands, one I had developed myself years before for
bridge bidding under the uninspiring name of BBL for &quot;Bridge Bidding
Language&quot;, and more besides) that had grown essentially impossible to
maintain and develop yet further, in order to continue my research.
So I was looking for the best way to re-code the whole system from
scratch.  Python offered me THE way to do that.

I fell in love, and immediately started making a nuisance of myself on
comp.lang.python, posting copiously (and, apparently, in ways that
many people found interesting, fun, or helpful).  Ominously, even my
very first post contained the sentence &quot;Books matter?a lot&quot; (in the
context of criticizing one existing book and praising two others).

A few months later (thanks to Greg Wilson reaching out to me), I was
negotiating with O'Reilly about writing a Python book.  I really
wanted to do a &quot;Python Cookbook&quot;, but O'Reilly had other ideas for
that, in cooperation with ActiveState, based on an *online* cookbook;
so I undertook instead to write **MISSING**, and meanwhile
I tried to help that cookbook project along by posting recipes,
commenting on others' posts, and so on.

Smack in the middle of the Nutshell's gestation, an emergency emerged
(as emergencies will :-)?the **MISSING** just wasn't going to
happen unless somebody with lots of Python nous AND some writing and
editing skills could devote a very substantial slice of time to
selecting and editing recipes.  I suspended the Nutshell work, took
all my accumulated vacation from work, and then some.  (I worked in
Italy, accumulating vacation at Italian rates, but typically *took*
amounts of vacation on more of an American scale.  So, after a few
years on the job, I had QUITE a lot of accumulated vacation.  And in
Italy, by law, you never &quot;lose&quot; vacation days you're due.)  I threw
myself into the task; the first edition of the **MISSING** emerged from
that long and frantic effort.  ActiveState's people who worked with me
on that project, chiefly David Ascher who's credited as co-author of
the **MISSING**, expressed their appreciation of my work by granting me
the &quot;Activators' Award&quot; in 2002 at OSCON.

By the time that was done, I was even deeper in love with Python;
while also going back to writing the Nutshell in my spare time, I
redoubled my efforts at work to &quot;muscle in&quot; the use of Python
alongside the &quot;corporately blessed&quot; languages.  I did find a point of
leverage, using Python's win32 extensions to implement COM objects for
Windows interfacing to legacy functionality in our apps?very much
of a &quot;skunkworks&quot; effort without any real support from top management,
who'd have preferred &quot;Microsoft-blessed&quot; languages.  Ironic, if you
think that today, finally!, Microsoft's IronPython is a first-rate
implementation of Python on .NET...  Anyway, Python is now firmly
ensconced at that firm, since so many apps have been developed and
sold based on those COM objects and their later dressing up in .NET
:-).  But at the time the experience was very frustrating and brought
home to me how much the company had changed since I had joined it many
years before when it was barely out of the startup stage?grown so
fast (perhaps too fast), acquired &quot;professional&quot; top management that
didn't think any more that it needed to listen to input from &quot;top
techies&quot;/&quot;highly technical managers&quot; such as myself.

Right about then, I got an offer to consult as a freelance Python
specialist for a Swedish startup, and I took the opportunity, quitting
my &quot;safe job&quot; and switching to freelance work, mostly but not
exclusively for that Swedish company.  It DID mean a lot of &quot;commuting
by plane&quot;, *sigh*, but it also gave me the opportunity to work almost
exclusively in Python (and in C, coding extensions for Python).  I
also managed to offer some contributions to Python itself, and develop
the gmpy project to offer advanced multiprecision arithmetic,
number-theoretical functions, etc., on top of the LGPL-licensed GMP
library (some of those advanced functionalities are precious to my
ongoing work in bridge simulation and analysis, though by now my
ongoing work maintaining and developing gmpy is mostly something I see
as a contribution to the community).

I did complete the **MISSING**, wrote many Python articles for various
magazines, both Italian and US ones, and went on a binge doing
presentations at all sorts of conference, such as PythonUK,
EuroPython, PyCon, OSCON, and many Italian open-source ones.

It's also through Python that I got back in touch with a woman, Anna,
whom I had known years before but had lost contact with.  She was
studying Python and recognizing my name mailed me to ask me for some
help.  She's now my wife, and became the first woman member of the
PSF.  We did the second edition of the **MISSING** together, and
although she's not officially an author of the second edition of
**MISSING**, she was so incredibly helpful with it that she
might as well be.

Through my Python books I got in touch with Google, at the time a
small company but already a substantial customer for the **MISSING**.
I tried to sell them on my services as a consultant and found myself
with an excellent job offer instead.  So I dropped the freelancer's
life, moved to California, and here I happily live, serving as &quot;Uber
Tech Lead&quot; for that deep-infrastructure software we call &quot;Production
Systems&quot;, where Python plays a crucial role (though not an exclusive
one, as C++ is also important here).

I was pleasantly surprised to find that working at Google, even in
such a fascinatigly challenging position as Uber Tech Lead is, allows
enough &quot;work-life balance&quot; (or in my case work-work balance :-) to let
me write the second edition of the **MISSING** (thanks also to Anna's
already-mentioned absolutely outstanding support).  Ever since I
finished that task, I've devoted my time to more and more promotion of
Python, and best Python practices, style, and usage, both at Google
and everywhere else.  My dream is to write another book, on Python
idioms, design patterns, and development methods, but I think I'll
take one more year off bookwriting before I start doing that.  In the
meantime, I'm also writing, presenting and teaching about &quot;highly
technical management of software development&quot;, a subject on which many
myths exist and on which I have substantial personal experience and
reflection to share with others.