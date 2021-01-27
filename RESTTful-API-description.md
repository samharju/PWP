# Important information for Deadline 1


:bangbang:&nbsp;&nbsp;**This chapter should be completed by Deadline 1** *(see course information at [Lovelace](http://lovelace.oulu.fi))*

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Chapter summary</strong>
</summary>

<bloquote>
This chapter must provide a good overview of the Web API that your group is going to develop during the course. You should not focus in implementation aspects such as database structure,  interfaces or the request/responses formats. We recommend that you look into existing APIs (see Related work below) before writing the description for your own API.

In this Chapter you must describe JUST the RESTful API, NOT THE CLIENT. Remember that client and Web API should be totally decoupled.

<h3>Chapter GOALS:</h3>
<ol>
<li> Understand what is an API</li>
<li>Describe the project topic API</li>
<li>Describe how the API will be used in the project</li>
</ol>
</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Chapter evaluation (max 7.5 points)</strong>
</summary>

<bloquote>
You can get a maximum of 7.5 points after completing this Chapter. More detailed evaluation is provided after each heading.
</bloquote>

</details>

---

# RESTful API description
## Overview
---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>

Describe the Web API briefly and comment which is the main functionality that it exposes to clients. Focus in the Web API not in the application which is using this API. Take into account that in the end, a WEB API is an encapsualted functionality as well as the interface to access that functionality. This section CANNOT include a description of an application or client that uses the API.  

Justify also why you want to implement this API. Comment why a developer would like to integrate this API into their application. Try to "sell" the API to your potential customers.

A really short version of an overview for the RESTful Web API could be: 

<em>“The discussion forum Web API offers different functionalities to structure non-real-time conversations among the people of a group about topics they are interested in certain topic. Messages are grouped in Threads, that at the same time are grouped in Topics. The messages are accessible to anyone, but posts can only be created by providing credentials of a registered user [...] Clients using this service may implement applications similar to [...]“</em>


Remember: The general description IS NOT just a description of the functionality. Try to market your API to potential customers.

</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 1.75 points)</strong>
</summary>

<bloquote>
You can get a maximum of <strong>1.75 points in this section</strong>
<ul>
<li>The description is clearly written and explains what the API is for: <strong>0.5</strong></li>
<li>The description includes a clear justification of why this project is useful. Why do you want to build this API:</li> <strong>0.5</strong>
<li>The description describes an API - not an application or client: <strong>0.75</strong>
<ul>
<li>This means that the description is written in terms of the functionality it makes available for clients, and internal working of the API</li>
<li> <em>tip</em>: don't think about human users when writing the description - think about machines </li>
</ul>
</li>
</ul>
</bloquote>

</details>

---

:pencil2: *Write here your description*

## Main concepts and relations
---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
<strong>Define</strong> the <strong>main concepts</strong> and describe the <strong>relations</strong> among them textually. Roughly, a concept is a real-world entity that is expected to be of interest to users. This section will be used in Deadline 3 to generate the list of resources. Students should remember that some of the concepts might not be a resource by themselves, but just a part of it (resource property). In this section, students should not describe the RESTful resources, but identify which are the main ideas of the API. Do not forget to include the relations among the concepts.

A description of the main concepts for the Forum API could be: 

<em>"The API permits users send messages. The forum contains a list of categories and a list of users. Each category specifies a name, a description and a thread. A thread is [...]The forum may contain 0 or more categories… Each category may have 0 or more threads… Users can write and read messages to a forum thread. A user has a profile, basic information, activity information (stores, for instance, all the messages sent by a user, the messages marked as favorites). [...]The user history contains information of the last 30 messages sent by the user.[…]"</em>

Include a diagram which shows easily the relations among concepts.

This section is important because it outlines the concepts that you will later implement. In particular, the diagram defined here will follow you throughout the project report and you will be adding more details to it. 


</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 1.5 points)</strong>
</summary>

<bloquote>
In this section you can get a maximum of <strong>1.5 points:</strong>
<ul>
<li>Concepts are named and described: <strong>0.5</strong></li>
<li>Relations among concepts is clear: <strong>0.5</strong></li>
<li>A diagram that shows relations between concepts is provided: <strong>0.5</strong></li>
</ul>
</bloquote>

</details>

---



:pencil2: *Write here your text and draw the diagram*



## API uses
---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Describe at least two clients that could use your Web API. You must explain here which is the functionality provided by the client, and how use the Web API to implement this functionality.
</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 1.75 points)</strong>
</summary>

<bloquote>
In this section you can get a maximum of <strong>1.75 points</strong>
<ul>
<li>The client descriptions are written clearly and explain what they are for: <strong>0.75</strong></li>
<li>Descriptions outline what parts of the API each client uses, and how: <strong>0.5</strong></li>
<li>At least two more examples of clients are provided (1-2 sentences per client):<strong>0.5</strong></li>
</ul>

</bloquote>

</details>

---



:pencil2: *Write here your text*



## Related work
---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Find at least one API that resembles the functionality provided by yours. Explain in detail the functionality provided by the API. Classify the API according to its type (RPC, CRUD REST, pure REST, hypermedia driven ...) justifying your selection. Provide at least one example client that uses this API.

The purpose of this task is to get more familiar with what an API is. This will be helpful in describing your own API. Therefore, it is recommended to do this section after you have decided the topic of your project but before writing your API description.
</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 2.5 points)</strong>
</summary>

<bloquote>
You can get a maximum of <strong>2.5 points</strong> in this secton:
<ul>
<li>The selected API is similar or related to the project topic: <strong>0.5</strong></li>
<li>The API classified correctly, and is described in terms of offered functionality: <strong>1.0</strong></li>
<li>An example of a client that uses this API is provided, explaining briefly what it does: <strong>0.5</strong></li>
<li>An additional API is provided <strong>0.5</strong></li>
</ul>
</bloquote>

</details>

---



:pencil2: *Write here your text*



## Resources allocation
|**Task** | **Student**|**Estimated time**|
|:------: |:----------:|:----------------:|
|||| 
|||| 
|||| 
|||| 
|||| 