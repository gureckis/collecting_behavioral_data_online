class: middle, center, bright

### Lecture 1
<hr>
# collecting behavioral data online
### a course by [todd m. gureckis](http://gureckislab.org/~gureckis)

.footnote[use arrow keys to navigate, type '?' for help]

???
welcome to class

---
class:  middle, bright

# Agenda
<hr>

1. Introductions
1. Give a short overview of course of those still considering enrolling  
1. Go over tentative syllabus  

---

class: middle, bright

**Instructor**
<hr>

# Todd M. Gureckis

*Associate Professor, New York University, Psychology*  
*PHD, University of Texas at Austin, Psychology*  
*BSEE, University of Texas at Austin, Computer Engineering*  
<br>
**Office**: Meyer 859  
**Hours**: Immediately after class or by appointment  
**Email**: <a href="mailto:todd.gureckis@nyu.edu">todd.gureckis@nyu.edu</a>  
**Web**: [personal site](http://gureckislab.org/~gureckis), [lab](http://gureckislab.org)

When you email me, PLEASE make the subject line include **[online_data]**

---

class: center, middle, bright

<img src="images/brainbw.png" width="150px">
# Who are you?

---

class: middle, bright


# What is this course about
<hr>

- Online data collection for psychological experiments and surveys
- **NOT** about user tracking (e.g., cookies, browsing patterns, search behavior)
- Basically "regular behavioral psychology experiments in a browser"
- Also about leveraging large online labor markets like Amazon Mechanical Turk for subject recruitment

---

class: middle, bright

# Why do we need a course about this?
<hr>

- **Experiments in the browers are more complex than regular experiments**
- All data is coming to you over the internet which can intermittantly drop out
- Tens or hundreds of participants might view you experiment in 1 hour.  Need reliability, speed
- Many different browsers (Safari, Chrome, IE) present UI problems (will your experiment look correct?)
- You may want to monitor activity of user (e.g., mouse movement, switching windows, etc...)
- How you design an experiment for non-psych 101 subject pool participants may be different
- You don't have a captive audience (people can leave and watch youtube... there's an art to making it reasonably good)
- Requires knowledge of CSS/Javascript/Databases, etc...

---

class: middle, bright


# Why is this good stuff to learn?
<hr>

- Increase your research productivity 
- More studies with larger samples
- If you design experiment to be web-enabled can still run in lab of course
- **Direct replication**
- Leverage the ideas/tools of an **immense** web development community may help you develop better/more interesting experiments
- An employable skill
- You can totally make your tumblr look super cool

---

class: middle, bright


# Why isn't this just "IT" department stuff?
<hr>

- Go ask the IT people if they'll program your experiments for you
- Experimenters need a lot of control over things
- You can't trust other people to organize you data
- Understanding how it works is important when interpretting your data, in conceiving of designs
- You don't want to be tied to other people to help you do this basic aspect of your work ($$$ and waiting around)

Sure, send you mouth swabs out to a genetics lab, but as psychologists/marketers/computer scientists **you should be able to design a good, robust behavioral experiment which can be delivered to multiple people.**

---

class: middle, bright

#### The best reason
# It is actually pretty fun


---

class: middle, bright


# Course webpage
<hr>

<div class="well well-sm">
  <center>
[**http://gureckislab.org/courses/spring14/online_data_collection/**](http://gureckislab.org/courses/fall12/lhc)
  </center>
</div>

- All lectures, handouts, announcements, etc... will be made on the webpage.  Check back often!
- Easy to find if you forget: Google "nyu cognition", find my webpage (usually a top link), follow links

---

class: middle, bright


# This is a "Flipped" Classroom
<hr>

- In traditional courses you attend lectures, work on problem sets and programming at home
- In a [flipped classroom](http://www.knewton.com/flipped-classroom/), you watch videos/read **before** class, then class time is spent entirely in discussion, problem solving, debugging, sharing hints
- Get more feedback
- Don't spend hours fighting a simple bug when getting started
- Ask questions while you are working, not after
- Hopefully limits fustration
- I've never done this before, so let's see how it goes

---

class: middle, bright


# Computer requirement
<hr>

- The class is called **online** experiments.  You will need to be online during class
- There are no computers in this room
- The labs in the psychology department do not have Internet
- Thus, you need some type of Internet connected device with a real browser and keyboard that you can program on (NOT a tablet)
- Software will require Mac OS X or Linux/Unix
- Sorry, windows, but you suck for server-side development
- Locate a computer in your lab, borrow one, or buy one (a linux laptop can be had for $200 these days)

---

class: middle, bright


# Grading
<hr>

- **15%** In class attendence/participation
- **15%** Various assignments/exercises
- **70%** Final project

---

class: middle, bright


# The singular goal of this course is to help you build an experiment for your research.
I want you to go back to your labs and share it and get this tool into more people's hands.

---

class: middle, bright


# If you are just generally interested in online experiments, don't take this class.
There's not a ton of theory here.  It is a course for makers.

---

class: middle, bright


# What can be done in online experiments?
<hr>

**Good question!**

- Basic questionaire type things (obviously)
- Decision making studies (are there limits?)
- Reaction time studies (perhaps)
- Visual perception studies (yes for some things)
- fMRI/MEG/EEG (no, no, no)
- Memory experiments (maybe?)
- Learning experiments (yes, but requires care)
- Group experiments (yes)
- Multi-day experiments (yes)
- Stimulus norming (yes)

If your interest lies in these area, might not be bad course for you.

---

class: middle, bright


# What skills will we cover in this class?


Unlike learning "matlab" online development requires
a cluster of skills.  You can never master all of it. I'll help 
point you in the right direction so you can be productive with the 
following things

### General stuff
- How to get good data online
- Crowd sourcing via Amazon Mechanical Turk
- Some general software hints: git, code sharing, testing

### Client-side:
- CSS/HTML/Markdown:  How your experiment will look to a participant
- Javascript/JQuery/d3.js: Dynamically moving things on the screen, etc...

### Server-side
- Python: Writing custom technologies you want protected from user's browsers
- **psiTurk**: a software platform for Mechanical Turk that my lab has developed
- Databases, cloud-based stuff: organizing largeish (not BIG!) datasets for analysis

---

class: middle, bright


# Learning to learn
<hr>

What I really hope is to teach you the basic so you can more effectively
teach yourself to solve problems.  

---

class: middle, bright

# This class in **opinionated**
<hr>

- I have a way of doing things which I think works
- [We](http://gureckislab.org) have had success with this
- There are many other approaches (e.g., Flash instead of Javascript, PHP, whathaveyou)
- I can't consider or teach all different alternatives
- Tough cookie


---

class: middle, bright

### Most important rule for this class
# Be organized.  Be careful.

... and you won't make bugs and waste time.

---
class: middle, bright

# For next time
<hr>

- Go to class [website](http://gureckislab.org/courses/spring14/online_data_collection/) and read/watch the material for [lecture 2](lecture2.html), complete assignments
- Bring your laptop next time
