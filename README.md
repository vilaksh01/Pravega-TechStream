# KONNEX UPDESH
<b>Pitch Sentence:</b> <i>Imagine a yoga teacher, sets up camera or edge device to stream video to his students; pose detection, sentiment analysis, conversation transcript models running for students and school authority to see the performance and interaction of teachers with students and make parents understand teachers commitment during this pandemic.</i>
<pre>
<img src="https://github.com/vilaksh01/Pravega-TechStream/blob/main/Images/Cover.png">
</pre>
Konnex Updesh means <b>Connecting Guidance</b>  
<br>
# Problem
Bringing educational content quality control for schools to monitor and get insights from realtime online classes. Providing schools real measures to improve engagement among students and teachers. The world has sifted massively towards online platforms like zoom, google meet and classrooms to ensure that education of students is not harmed due to ongoing pandemic. High speed internet has been a big savior during this time, from rapid medical advancements to logistics everything is powered by data. However, we still needs to understand that schools has been playing foundation roles in any child's career development and future teaching prospects lies with more flexibility in terms of teaching without compromising quality lessons and sessions. Schools are having hard times getting control over the quality teaching in remote classes and teachers promotions are harder than ever- 'no matter how hard a teacher tries, remote classes without any metrics and data analytics schools can't trust.' Only data can help us find real caveats with their teachings, engagements and commitments. So let's harness the <b>UNBOUNDED DATA</b>
<pre>
<img src="https://github.com/vilaksh01/Pravega-TechStream/blob/main/Images/Problem.png">
</pre>
# Solution
Remote learning generates massive amounts of unstructured data and there is a need for practical unbounded content storage and retrieval system to deliver insights from those data. The data generated during remote learning are text conversation data, video meetings or uploaded tutorials, audio narration while lesson explanations. Those generated data grow with time and it will be difficult to track those then. Pravega can be best utilized here, it's performance, scalability and search efficiency makes it an ideal tool for our project. So the working flow is very simple, all conversation data including text .txt, video meeting in .mp4 and audio is .wav is streamed live to Pravega, Pravega API and GStreamer tools. Another set of APIs handle data stream from pravega to Symbl.Ai API which is an advanced NLP we are using to gather insights from all types of conversation data https://symbl.ai/
Here's the simple steps:
1. Stream media data like camera and audio feed together from webcam, only audio feed from microphone or text file to Pravega.
2. Read data streams from Pravega anywhere and run Symbl.ai NLP APIs for sentiment, speech, conversation analysis.
3. Store performance analytics results for the system admins
<pre>
<img src="https://github.com/vilaksh01/Pravega-TechStream/blob/main/Images/Working.png">
</pre>

# Install
The Pravega client library can be installed using pip.
<pre>pip install pravega</pre>

# Future Works
Many of the features mentioned could not be implemented due to lack of time, this project was started for a three day hackathon and we ran into lot of technical issues and we lacked skills in solving those on time. Some of GStreamer Pravega features would require future patch updates to remove some bugs and file flush issues.
