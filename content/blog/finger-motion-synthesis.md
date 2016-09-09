Title: Finger Motion Synthesis
Date: 2015-06-29 23:05
Author: Ben Sledge
Category: Projects
Slug: finger-motion-synthesis
Status: draft

While I was at Clemson University, I had the opportunity to take a class
on computer animation with Dr. Sophie Jörg. The course explored the
nuts-and-bolts of computer animation by examining the history and
technology that drives current innovations in the graphics field. Our
final assignment was to "do something cool" with something we learned
over the semester. For my project, I created an implementation of Dr.
Jörg's paper, [*Data­driven Finger Motion Synthesis for Gesturing
Characters*](http://people.cs.clemson.edu/~sjoerg/fms.html). The paper
analyzes motion capture data to create a database of finger motions. A
motion sequence without finger animation is then used as an input to
synthesize finger movements based on the data in the database.

The Problem
-----------

Character animation is traditionally produced through time-intensive
key-frame animation. An animator manually creates a series of poses for
each individual part of a character, that, when viewed in sequence, give
the illusion of movement. Hand animation can be particularly
tedious--each finger has three sections (or joints) and there are three
to five fingers per hand. One solution to the complex problem of finger
animation is motion capture. Motion capture allows the performance of an
actor to be translated from real-life and applied to a digital character
with minimal manual processing, thus reducing the amount of time needed
for an animator to create believable motion.

Motion capture has it's own problems though. The resolution required to
accurately reproduce finger motions limits the capture area and can even
constrain the actor to a standing position. To solve this limitation,
Jörg et al. proposed using a limited input set and a database of
previously recorded finger motions to create new, believable hand
animation. Through their research, they determined the movement of a
human's wrist can be indicative enough to produce favorable results.
Check out their paper for the details.

The Solution
------------

![Wrist movement + motion database = Believable finger animation]({filename}/images/fms1.png)
Finger Motion Synthesis Overview

My implementation pars down Dr. Jörg's solution to it's minimum (mainly
due to development time constraints). I took a motion capture session
and segmented the wrist motion using acceleration. I stored each wrist
animation segment with it's corresponding finger movements. Then, I
selected motion clips to use as an input to the system. I threw away the
finger motion and segmented the wrist movement using the same methods
used to create the database. Then, I compared each segment of input
motion to the database. I looked at position and rotation deltas to
determine the overall distance between two segments in question, and
selected the entry closest to the input motion. Finally, I blended all
the finger motion segments back together and attached them to the rest
of the body.

![A line graph showing the speed of wrist motions, with lines indicating segmented motion clips.]({filename}/images/fms2.png)
Wrist speed is graphed in red. The vertical blue lines denote motion segments (the green line indicates the threshold for "interesting motion.

Results
-------

The resultant animation contains believable finger animation. It's
important to note, the goal was never to exactly recreate the
ground-truth motion, only to synthesize a believable approximation. Jörg
et al. performed limited perception analyses on their final animation
clip. Their discussion is definitely worth a read.

My method ended up being less successful than the original paper's
results. My segment matching algorithm was less precise than Jörg et
al.'s implementation of Dijkstra's Algorithm. I also used rudimentary
motion blending techniques to combine the final finger motion clips. A
more advanced blending method would have drastically improved the
results.
