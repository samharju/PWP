# Important information for Deadline 3


:bangbang:&nbsp;&nbsp;**This chapter should be completed by Deadline 3** *(see course information at [Lovelace](http://lovelace.oulu.fi))*

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Chapter summary</strong>
</summary>

<bloquote>
In this chapter, the students&nbsp;<strong>must design the RESTful API.The minimum requirements are summarized in the&nbsp;<a href="">Minimum Requirements</a>&nbsp;section of the Project Work Assignment. Note that if you do not meet Minimum Requirements this section wont be evaluated.</strong>

<h3>SECTION GOALS: </h3>
<ul>
<li>Understand REST principles</li>
<li>Understand connectedness and/or hypermedia</li>
<li>Design a small API</li>
<li>Write API documentation</li>
</ul>

<p>
	You have two options:
		<ol>
			<li>Implement the API using a non-hypermedia format (RESTful CRUD). In this case, it is mandatory that all your resources are connected. <strong>You cannot get full points in this section if you do not design your API using an hypermedia format</strong></li>
			<li>Using an hypermedia format. Lots of examples provided in Exercise 2. You can get full points. In this case you need to clearly include in the documentation a profile with link relations and semantic descriptors.</li>
		</ol>

</p>

<strong>The recommended step-by-step process &nbsp;is:</strong>
<ol>
<li><strong>Identify all the resources</strong>&nbsp;to be exposed by the Web API. To that end, students should make an abstraction of the concepts defined in section 1. Be aware that a one-to-one mapping between the resources and the concepts defined in section 1 is not usually the best option. Sometimes it is better to pack several concepts in the same resource.</li>
<li><strong>Establish the resource hierarchy and assign a URI to each resource.</strong></li>
<li>Establish relations and possible actions among resources.&nbsp;<strong>Create the state diagram of your API.</strong></li>
<li><strong>Expose</strong>&nbsp;each one of the resources&nbsp;<strong>to the uniform interface</strong>.</li>
<li><strong>Design the resource representation using adequate format. </strong><br />
<ol>
<li>Define the media type and its extension (if any)</li>
<li>Define the profiles (if you are using an hypermedia format). Try to reuse existing profiles as much as possible. For instance, utilize schemas defined in <a href="http://schema.org/docs/schemas.html">schemas.org</a>.
<li>Do not forget to include the format of the requests. If you are using hypermedia format and the media type does not define the format of the requests, they must be defined in the profile. Otherwise, the request formats must be defined in the documentation.</li>
<ul>
</ul>
</li></ol></li>
<li><strong>Define protocol attributes</strong>: headers, possible response codes ... must be clearly specified both for requests and responses.</li>
<li>Define the&nbsp;<strong>error conditions</strong>. When errors are triggered?
<ul>
<li>Define the format of each HTTP error response, including message body, status code and headers.&nbsp;</li>
<li>It is recommended to use a hypermedia type for the response. <a href="http://soabits.blogspot.no/2013/05/error-handling-considerations-and-best.html">This blog post</a> contains some good recommendations.</li></ul></li></ol>

</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Chapter evaluation (max 25 points)</strong>
</summary>

<bloquote>
You can get a maximum of 25 points after completing this section. More detailed evaluation is provided after each heading.
</bloquote>

</details>

---

# RESTful API design

## Resources and relations
---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
<ol>
<li>Fill the table below with a description of the API resources</li>
<li>Include a state diagram of your application, in which each resource is a state. Describe also the state transitions. To build this diagram you should reuse the diagram created in DL1. You can use online tools such as <a href="https://www.draw.io/">draw.io or <a href="https://www.lucidchart.com/">lucidchart</a> to create the diagrams. You have an example in the following image</li>
</ol>
<img src="uploads/448d6edbd82d4784e9aff04dcbb1c60c/Forum_state_diagram.png"></img>


</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 2.5 points)</strong>
</summary>

<bloquote>
You can get a maximum of 2.5 points after completing this section.

<ul>
	<li>Resource table with URLs and short descriptions is provided: <strong>0.5</strong></li>
	<li>State diagram with transitions exists (see below): <strong>0.5</strong></li>
	<li>State diagram follows relationships from DL1: <strong>0.5</strong></li>
	<li>State diagram is correct, states make sense, transitions are clear and all possible transitions documented: <strong>1.0</strong></li>
</ul>
</bloquote>

</details>

---

:pencil2: *This table might serve you as a guide*

|  Resource name       | Resource url | Resource description |
|:-------------------: |:------------:|:--------------------:|
|Resource Name 1       |              |                      |
|Resource Name 2       |              |                      |


:pencil2: *Draw here your state machine diagram*



## Uniform interface

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Fill the following table with a description of how your resources are exposed to the uniform interface (GET, PUT/PATCH, POST and DELETE methods). You must describe the action executed in each request.  For example, a GET request to the URL /messages/{message_id} "gets the body and the title of a specific message".

</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 0.75 point)</strong>
</summary>

<bloquote>
You can get a maximum of 0.75 points after completing this section.
<ul>
<li>The uniform interface shows all possible requests and actions are described for each: <strong>0.75</strong></li>
</ul>
</bloquote>

</details>

___

:pencil2: *This table might serve you as a guide*

|         | **GET**|**PUT**|**PATCH**|**POST**|**DELETE**|
|:------: |:------:|:-----:|:-------:|:------:|:--------:|
|Resource Name 1|||||| 
|Resource Name 2||||||  
|Resource Name 3||||||  
|Resource Name 4|||||| 
|Resource Name 5||||||  



## API design

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
<p>Use any of the tools presented in Exercise 2 (e.g. Apiary) to document the API. Follow the format specified in that exercise also.
You can take the <a href="http://docs.tvflix.apiary.io/">TVflix service REST API</a> or <a href="https://cryptotrading.docs.apiary.io/#">Cryptotrading API</a>(created by previous year students) as a model. 


For all resources you must cover:
<ul>
<li>The possible HTTP methods exposed by this resource</li>
<li>The headers in the request and responses</li>
<li>The media type utilized (in the response Content-Type header). If you are utilizing your own media-type you must describe it in the section Own media type implementation.</li>
<li>If you are using an hypermedia type you must provide the profile utilized, including. 
<ul>
<li>Link relations. Include methods and format of the requests if they are defined in the media type. Use as much as possible IANA defined relations.</li>
<li>Semantic descriptors. If you utilize a descriptor used in some other profile (e.g. <a href="http://schema.org/docs/schemas.html">schema.org</a>) provide the link. </li>
<li>If you are extending other profiles, do not forget to link to the extended profile.</li></ul></li>
<li>The format of the HTTP response body, providing a clear example. If necessary, comment the example.</li>
<li>The format of the HTTP request body (just for PUT/POST), providing a clear example. If necessary, comment the example.</li>
<li>The error conditions, status code and format of the error response, providing a clear example.</li></ul>

</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 13.75 points)</strong>
</summary>

<bloquote>
You can get a maximum of 13.75 points in this section:
<ul>
<li> You are using a hypermedia API: <strong>3.0</strong></li>
<li>Each request has the correct media type: <strong>0.5</strong></li>
<li>The media type is used according to its specification: <strong>1.0</strong></li>
<li>Link relations are described (either in the profile for hypermedia types, or in the resource documentation for the CRUD approach): <strong>1.0</strong>
	<ul>
		<li>Do not forget you can use link relations from <a href="http://www.iana.org/assignments/link-relations/link-relations.xhtml">http://www.iana.org/assignments/link-relations/link-relations.xhtml</a></li>
	</ul>
</li>
<li>Attributes are clearly explained ( either in the profile - for hypermedia types - or in the resource documentation - for the CRUD approach -): <strong>1.0</strong></li>
<li>Examples are provided for each request: <strong>0.5</strong></li>
<li>Examples provided for each request do not contain errors: <strong>0.5</strong></li>
<li>Examples are provided for each response: <strong>0.75</strong></li>
<li>Examples provided for each response do not contain errors: <strong>1.0</strong></li>
<li>Examples includes error responses <strong>0.25</strong></li>
<li>Examples provided in error responses do not contain errors <strong>0.5</strong></li>
<li>Examples provide all possible/reasonable error responses for each method <strong>0.5</strong></li>
<li>Examples have correct headers: <strong>0.5</strong></li>
<li>Profiles are linked in each response (only for hypermedia APIs, CRUD implementation receive 0 points in this section): <strong>0.5</strong></li>
<li>Examples use correct status codes: <strong>1.25</strong></li>
<li>Design is coherent: <strong>1.0</strong></li>
</ul>
</bloquote>

</details>

---



:pencil2: <strong>Include here the link to the hypermedia API documentation </strong>



## REST conformance

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Explain briefly how your API meets REST principles. Focus specially in the four principles: <strong>Addressability, Uniform interface, Connectedness, Statlessness</strong>

</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 8.0 points)</strong>
</summary>

<bloquote>
You can get a maximum of 8.0 points in this section:
<ul>
	<li>The justification is clear and coherent, and shows an understanding of REST principles: <strong>2.0</strong></li>
	<li>The Api is addressable (no errors regarding addressability): <strong>1.0</strong></li>
	<li>The Api uses correctly the uniform interface: <strong>1.0</strong></li>
	<li>The Api does not hold state in the server: <strong>0.5</strong></li>
	<li>The different resources of the API are connected, that is there are not isolated resources: <strong>2.0</strong>
		<ul>
			<li>isolated resource is a resource that either is not linked to from anywhere, or doesn't contain links itself</li>
		</ul>
	</li>
	<li>Protocol semantics are clearly provided either by the response or by the profile (If you are using a CRUD API you won't get points in this section): <strong>1.5</strong></li>
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
