March 2020 update
=================

.. feed-entry::
   :author: flavio
   :date: 2020-3-7

Hi! Here is an update about my development progresses.

.. cut::

New site
--------

Here is the new *Sphinx*-powered site. Since my main activity is coding, a site that is tightly coupled with my code is a big improvement for me.

Yorg updates
------------

I have worked on several things in Yorg. You will find these in the next release.

New features:

* added vibration for weapons and crashes;
* concurrent use of keyboard and joypads;
* a new page for configuring joypads' buttons;
* support for AppImage packages.

Fixes:

* CPU usage;
* AI;
* camera's inertia.

Refactorings:

* removed some dependencies (*bson*, *feedparser*, *yaml*);
* optimization of network usage;
* *yracing* submodule.

As for the last point, Yorg has been splitted in three modules: *yorg*, *yyagl* and *yracing*. I have done this for reusability. *yyagl* is a library which contains some utilities. *yracing* contains code for abstract racing games. *yorg* contains Yorg's specific code. The point is that I can reuse *yyagl* among my projects (also non-racing games), while *yracing* can be reused for a new racing game (more on this in the next section).

Finally, I have added some *unit tests*.

Roadmap
-------

I am doing a lot of refactorings since this is very important in my roadmap. Aside maintaining Yorg, I am going to make a new racing game. I would love to use the new awesome features that they are developing in *Panda3D*, and Yorg's current assets are not the best for them. So, before starting, I am adapting the current code for making a new game without reinventing the wheel.

Support me
----------

Finally, I would love if you may consider to :ref:`support me <support-page>`. As usual, you may consider my campaign on `Patreon <http://www.patreon.com/ya2>`_ (minimum pledge: **only $1**!). Thank you very much!
