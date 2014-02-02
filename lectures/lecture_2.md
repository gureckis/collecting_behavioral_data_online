class: middle, center, bright

### Lecture 2
<hr>
# collecting behavioral data online
### a course by [todd m. gureckis](http://gureckislab.org/~gureckis)

.footnote[use arrow keys to navigate, type '?' for help]

???
welcome to class


---

class: middle, bright

# Online data collection: A revolution for behavioral science?  .blue[Or a curse]?


---
class:  middle

# Agenda
<hr>

1. What is online data collection? Basic issues
1. How the Internet works (hint: series of tubes)
1. Crowdsourcing labor markets - Amazon Mechanical Turk
1. Review studies looking at the replicability of laboratory-based studies online

---

class: middle
## Online data collection
<hr>

1. Collecting scientific data, often anonymously, over the Internet
1. Most typical example is online surveys
1. Also can include more dynamic browser-based tasks almost like video games
1. Could include mobile phone and tablet-based data collection (e.g., distributing experiment though App store)

---

class: middle

## Advantages
<hr>

1. Access to a larger population pool
1. Access to a potentially more diverse subject pool
1. Access to special populations which are difficult to recruit locally (e.g., patient groups)
1. Affordable: People will typically sign up for $2.00 for 15-25 minute session
1. **Anonymous** subject never meets experimenter, unlikely to know about "your lab"
1. **Replicable**: Very easy to share your experiment code


## Disadvantages
<hr>

1. No control over experiment context - .blue[does it matter?]
1. Massively hereogenous displays/computer setups
1. Potential for people lying (e.g., demographics) - .blue[Affects lab data too?]
1. Software development costs can be higher

---

class: middle

.left-column[

<img src="images/Computer_Workstation_Variables.jpg" width="300">
]

.right-column[
# typical laboratory-based experiment
<hr>

1. Office-style interaction
1. General control over lighting, temperature, viewing angle, distance
1. A few people at a time (1-5/hour), each on individual workstations
1. Data saved to local disc or to a local file server
]

---

class: middle

.left-column[
.center[
<img src="images/womenonlaptop.jpg" width="200"><img src="images/TabletUser.jpg" width="200">
<img src="images/smartphone.jpg" width="200"><img src="images/OutsideUser.jpg" width="200">
]
]

.right-column[
# typical online experiment
<hr>

1. Variable lighting, conditions, computer system, etc...
1. International subject pool
1. Many people at the same time (10-100/hour), each talking to a centralized server
1. Data saved in database to allow concurrent reading/writing


<br><br>
**This may not be all bad actually depending on your research project!!**
]

---
class: middle, center

# Anatomy of an Internet request
<hr>

<img src="images/web-hosting.gif">
<img src="images/dynamicpage.png" width="500">

.footnote[http://www.austinseoguy.com/web-hosting.php,
http://en.wikipedia.org/wiki/Dynamic_web_page
]

---
class: middle

# Typical requirements for online experiments .red[*]
<hr>

- An Internet accessible computer
  - .red[NOT] just a computer "on the Internet." Needs to be able to accept in-bound connections typically on port 80 (standard for web)
  - Can be a problem on University networks or home cable connections since firewalls and routers can limit incoming connections to your computer (for security reasons)
- Content that can be displayed in a browser
- Some type of database for managing concurrent connections

## You don't necessarily have to provide all these things yourself, but are necessary one way or another.

.footnote[.red[*] Of course, you could just do things using email or something simple.]

---
class: middle

# .red[Security]
<hr>


- All of the previous items expose your computer to security risks
- Hackers do scan university networks looking for outdated/misconfigured software
- Can turn your computer into a bot for attacking another system (Denial or service attacks)
- Could mess with or otherwise delete your data
- If it is also your main computer could gain access to personal information

---
class: middle

# Where do you find people to participate?
<hr>


- Advertise on bulletin boards, craigslist: "Work from home!  Make money!"
- Flyers around campus/town
- Crowdsourcing labor markets like Mechanical Turk
  - Systems designed to facilitate paying people to do work online
  - http://mturk.com
  - http://clickworker.com
  - http://microtask.com
  - http://crowdflower.com
  - See nice answer on [Quora](http://www.quora.com/What-are-some-crowdsourcing-services-similar-to-Amazon-Mechanical-Turk)

---

class: center, middle
# What is ".blue[Mechanical Turk]"?

---

class: middle

# The history
<hr>

- Developed by [Amazon.com](http://amazon.com)

- Originally for in-house use to detect duplicate product postings on Amazon's site .red[*]

<br><br>
.center[<img src="images/AMTLogo.png" width="300">
]

.footnote[.red[*] Nice summary in the [New York Times](http://www.nytimes.com/2007/03/25/business/yourmoney/25Stream.html)]

---

name: terminology
class: middle

# Key terminology
<hr>

- HIT = Human Intelligence Task (a unit of work, e.g. a trial or an entire sequence of trials in an experiment)

- .orange[**Requester**] = an entity (e.g., researcher) who posts HITs

- .blue[**Worker**] = a person who performs the task


---

class: middle

# What kinds of tasks?
<hr>

- Difficult for computer or machine learning systems
    - Provide three key words to describe an image
    - Does this photograph contain a car?
    - What event does this twitter search refer to?
    
- Traditional work
    - Write a positive review for this product online 
    - Translate this text from English to Spanish
    

- .green[Help with science!]
    - **Participate in my human cognition/perception/learning experiment!**

---

class: middle

# Who are the workers?
<hr>

- 46.80% US, 34% India, 19.20% Other

- United States demographic
    - 55-65% female
    - Most make  <$60k/year
    - Median age of 30
    - Hold bachelor's and are young
    - Distribution mostly similar to US internet pop.
    
- See Ipeirotis, et al. (2010) or Mason and Siddharth (2011).

---

# World distribution

<img src="images/world-turk-distribution.jpg" width="700">

Tamir (2011)

---

class: middle
# Compensation
<hr>

- Median wage is $1.38/hour

- Short tasks (~5 mins) award around 10 cents

- Requester can reject work and revoke payment

- And can also **award bonuses**

- Amazon takes 10% of payments

- Amazon tries to stay out of disputes

---
class: middle
# Outside of the US
<hr>

- Unfortunately, getting a requester account from outside the US can be a bit tricky

- Requires US billing address  and US debit or credit card

- If you can't get a US credit card, setting up the account with a US American collaborator is an option

- Or consider international/European alternatives to AMT, such as [clickworker](http://www.clickworker.com), [crowdflower](http://crowdflower.com). The latter actually uses AMT workers, but is accessible worldwide 

---
class: middle
# Why should I .red[not] use AMT?
<hr>

A few concerns have been raised about AMT data:
<br><br>

- **Selection Bias:** No control over who takes the experiment
    - 53% are self-identified liberals, 25% conservatives, 73% voted for Obama, see details [here](http://themonkeycage.org/2012/12/19/how-representative-are-amazon-mechanical-turk-workers)
    - Makes AMT sample probably less useful for research on ideology, or political attitudes (see [this](http://www.culturalcognition.net/blog/2013/7/10/fooled-twice-shame-on-who-problems-with-mechanical-turk-stud.html) blogpost for a discussion)

    - On the other hand, 20 year old university students are a very special sample too!

---
class: middle
# Why should I .red[not] use AMT?
<hr>

- **Contamination of subject base** 
    - Recent [study](http://www.jessechandler.com/uploads/2/8/0/5/2805897/13_chandler_mueller__paolacci.pdf) has addressed this question
    - Can be a problem for *very* widely used paradigms 
      - 56% had participated in Prisoner's Dilemma, 52% in Ultimatum game, 30% Trolley problem

    - Cross talk (e.g. in AMT forums) seems to be rare (workers share information about payment, duration, etc.)

    - For specific studies repeated participation can be prevented by recording worker's IDs
 - .blue[PsiTurk helps with this!]


---
class: middle

# Why not?
<hr>

- **Non-lab setting **
    - [This](http://www.jessechandler.com/uploads/2/8/0/5/2805897/13_chandler_mueller__paolacci.pdf) study showed
      - 27% were not alone while working on the HIT
      - 18% were watching tv
      - 14% were listening to music

    - Recording how often participants change windows/take breaks might help clean data
  - .blue[PsiTurk helps with this!]

    - Still, the lack of experimental control over a worker's environment might make some studies unsuitable for AMT

---
class: center, middle

# How does the data compare to that collected in the lab?

---

class: middle

# Lots of interest in this...
<hr>

.refs[

- Gosling, S.D., Vazire, S., Srivastava, S., & John, O.P. (2004). [Should we trust web-based studies? A comparative analysis of six preconceptions about Internet questionnaires](http://ww.w.simine.com/docs/Gosling_et_al_AP_2004.pdf). _American Psychologist_, 59, 2, 93-104.

- Paolacci, G., Chandler, J., & Ipeirotis, P. G. (2010). [Running experiments on Amazon Mechanical Turk](http://repub.eur.nl/res/pub/31983/jdm10630a[1].pdf). _Judgment and Decision Making_, 5, 411-419.

- Buhrmester, M., Kwang, T., & Gosling, S. D. (2011). [Amazon's Mechanical Turk A New Source of Inexpensive, Yet High-Quality, Data?](http://pps.sagepub.com/content/6/1/3.full). _Perspectives on Psychological Science_, 6(1), 3-5.

- Germine, L., Nakayama, K., Duchaine, B.C., Chabris, C.F., Chatterjee, G. & Wilmer, J.B. (2012).  [Is the Web as good as the lab?  Comparable performance from Web and lab in cognitive/perceptual experiments](http://www.springerlink.com/content/f0244t772070138w/)  _Psychonomic Bulletin & Review_,  19.5.


- Shapiro, D. N., Chandler, J., & Mueller, P. A. (2013). [Using Mechanical Turk to Study Clinical Populations](http://s3.amazonaws.com/academia.edu.documents/30554524/Clinical_Psychological_Science-2013-Shapiro-2167702612469015.pdf?AWSAccessKeyId=AKIAIR6FSIMDFXPEERSA&Expires=1374090987&Signature=%2B4nErhKWOQhoWYY9gpgV0EbvVa0%3D&response-content-disposition=inline). _Clinical Psychological Science_, 1(2), 213-220.

]

### More published all the time...

---

class: middle

# Do classic findings replicate?
<hr>

- Some members of our lab recently contributed to this study that tested some classic psychology experiments on AMT.red[*]

    - Crump, M. J., McDonnell, J. V., & Gureckis, T. M. (2013). [Evaluating Amazon's Mechanical Turk as a tool for experimental behavioral research.](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0057410) PloS one, 8(3).


- Focus was on reaction time findings that require sustained attention from subjects and precise recording of responses

- And learning experiments involving more cognitive effort 


.footnote[.red[*] For a summary of the paper see this [blog post](http://gureckislab.org/blog/?p=1297)]

---
class: middle

# Stimulus Detection
<hr>


.left-column[ 

### Stroop

  - People respond faster to congruent (e.g. .blue[blue]) than to incongruent (.green[blue]) items


### Task Switching

  - Faster RT if task stays the same (e.g. "Odd or Even?") than when tasks alternate ("Odd or Even?" / "Small or Large?")

### Flanker

  - When identifying a target (e.g. "h"), congruent flankers ("hhhhh") lead to faster RTs than incongruent ("ffhhff") ones

]
  

.right-column[.center[
<img src="images/StroopResult.png" width="160">
<img src="images/TaskSwitchingResult.png" width="160">
<img src="images/FlankerResult.png" width="160">
]
]

---
class: middle

# Stimulus Detection
<hr>


.left-column[ 

### Simon

  - Targets that are spatially compatible with response key are identified faster


### Visual Cuing 

  - Stimulus detection is faster for cued  versus uncued targets if cue is presented after short interval (<=300ms) and slower after longer interval (>=400ms)

### Attentional Blink

  - During rapid serial visual presentation visual target detection is impaired if target is displayed 100-500ms after another one


]


.right-column[.center[
<img src="images/SimonResult.png" width="160">
<img src="images/ContCueing.png" width="160">
<img src="images/AttentionalBlink.png" width="160">
]
]

---
class: middle

# Subliminal Perception
<hr>


Masked priming

  - Responding to arrow probes that are either compatibly (prime: >>, probe: >>) or incompatibly primed (prime: <<, probe: >>) at durations of 16, 32, 48, 64, 80, and 96 ms 

  -  Previous finding was that compatibility effects are negative for very short prime durations and positive for longer ones


  .center[
   <img src="images/PrimingResult.png" width="330">
   ]

  - Only partially replicated: no negative compatibility effect

  - Possibly lower bound on display duration in browser!

---

class: middle

# Category Learning
<hr>


- Classic Shepard, Hovland, & Jenkins (1961) paper

- Six different ways of classifying the same 8 items (geometric figures with 3 binary dimensions) into deterministic categories

- Generally Type I is learned faster than Type II which is faster that Types III-V, with Type VI the hardest
.center[
<img src="images/abstractstructureSHJ.png" width="150"><img src="images/dimstructureSHJ.png" width="170">
<img src="images/SHJDifficulty.png" width="550">
]

---

class: middle

# Results
<hr>


Although type I was learned easily, performance on all other types was significantly worse than in the original study
<br><br>

.center[
<img src="images/exp8-nosofsky.png" height="290"><img src="images/exp8-amt.png" height="290">
]

---

class: middle

# Incentives too low?
<hr>


There was little difference between high ($2 to $4.50 with bonus), medium ($1.50), and low-payment ($.75) groups
<br><br>

<img src="images/exp9-typeII.png" height="290">
<img src="images/exp9-typeIV.png" height="290">

---
class: middle

# Bad instructions?
<hr>


Including manipulation checks that asked non-trivial questions about the task improved performance on types II to VI
<br><br>

.center[<img src="images/exp10-l-vs-amt.png" height="310">]

---
class: middle

# Replication in other Areas
<hr>


1. Clinical (Shapiro, et al, 2013)

  - Scores on a range of psychometric tests had high internal consistency and test-retest reliability  (r =.87)

2. Personality (Buhrmeser, et al, 2011)

  - No difference in consistency on personality questionnaires at different payment levels, and absolute levels of consistency and test-retest reliability were high (r = .88)

3. JDM (Paolacci, et al, 2010)
  
  -  Compared classic JDM studies (Asian Disease, Linda, Physicians Problem) on AMT and university subject pool
  - No difference in failure rate of catch trials and pattern of behavior in studies but AMT subjects were more risk averse

---
class: middle

# Non-naivety and expert subjects
<hr>


1. What is same individual takes your experiment more than once?

1. "Expert experiment-takers" - people who take a lot of experiments may have encountered your manipulation before

- Mention study along those lines

**Discussion point** 

How naive are subject pool participants who are taking Intro to Psychology or other classes and have decided to study psychology?


---

class: middle
# Summary
<hr>


1. AMT  allows you to collect data quickly and conveniently

1. Web experiments can prevent experimenter effects and increase anonymity

1. Many classic psychology findings replicate with **reasonably** high fidelity
    - But  it's important to check for browser limits regarding presentation time, etc.

    - It's also helpful to check participants' understanding of the task

1. Changing payment does not have a large effect performance but does affect signup and dropout rates

---
class: middle

# Credits
<hr>

- Gureckis lab Mechanical Turk Workshop CogSci2013 [Slide deck](https://github.com/NYUCCL/MTurkWorkshop_CogSci2013)
- **John McDonnell** (https://github.com/johnmcdonnell)
- **Doug Markant** (https://github.com/dmarkant)
- **Jay Martin** (https://github.com/jbmartin)
- **Anna Coenen** (https://github.com/annacoenen)
- **Alex Rich** (https://github.com/alexanderrich)

???
Thanks to these people
