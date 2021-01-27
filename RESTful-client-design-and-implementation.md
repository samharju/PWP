# Important information for Deadline 5


:bangbang:&nbsp;&nbsp;**This chapter should be completed by Deadline 5** *(see course information at [Lovelace](http://lovelace.oulu.fi))*

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Chapter summary</strong>
</summary>

<bloquote>
In this section your group must design, implement and test a client application that uses the RESTful API implemented by you. The application MUST provide a GUI for a user to control it. If you want to implement a machine-to-machine application please contact the assistants first.  If you utilize HTML and JavaScript, it is mandatory that the HTML is contained in static files. It means that your server cannot generate HTML dynamically (using PHP or JSP).  All modifications made to the webpage must be done in the client side using javascript. Of course,  you can use anchors (<a>) to load a new URL. Please, consider  the <a href="http://en.wikipedia.org/wiki/Same_origin_policy">Same Origin Policy"</a>  because it might cause problems to your client implementation. It is recommend to host the files in a local HTTP server and not directly in your file system. We will give you more instructions in Exercise 4. 

It is not mandatory to write code for test the application. Client testing would be considered extra work.</strong>
<h3>CHAPTER GOALS</h3>
<ul>
<li>Learn how to use APIs</li>
<li>Implement a client that uses the project API</li>
</ul>
</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Chapter evaluation (max 15 points)</strong>
</summary>

<bloquote>
You can get a maximum of 15 points after completing this section. More detailed evaluation is provided after each heading.
</bloquote>

</details>

---

# RESTful Client


## Client application description
### Overview
---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
You must provide a description of the application. You must clarify which are the goals of the application and why a user would like to use this application. <strong>You must also state what is the functionality provided by the RESTful API used by this application.</strong>


</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 1.0 points)</strong>
</summary>

<bloquote>
You can get a maximum of 1.0 points in this section:
<ul>
	<li>The clients purpose is clearly described: <strong>0.5</strong></li>
	<li>Description of the API client not just a GUI: <strong>0.5</strong></li>
</ul>
</bloquote>

</details>

---

### Functional requirements

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Provide a use case diagram of your application. For each case, specify which is the API resource/s that cover the given functionality

</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 2.0 points)</strong>
</summary>

<bloquote>
You can get a maximum of 2.0 points in this section:
<ul>
	<li>Diagram below presents the different use cases and they are correctly explained:  <strong>1.25</strong></li>
	<li>Description + diagram shows clearly what functionality of the API the client uses:  <strong>0.75</strong></li>
</ul>
</bloquote>

</details>

---



:pencil2: *Write here your text*



## Client design
### GUI layout

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Draw a diagram of the client layout. Students can use any software they want to do the sketching. For more professional-like design, students can use any wireframing tool available in Internet. Some of them can be found from <a href="http://webdesignledger.com/tools/13-super-useful-ui-wireframe-tools">http://webdesignledger.com/tools/13-super-useful-ui-wireframe-tools</a>. <a href="http://pencil.evolus.vn/Default.html">Pencil </a>is free, open source and easy to use. Other options are Visio and Balsamiq (you need a license). You can also create the UI using a paper and a pencil and scan the resulting drawing.
</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 1.5 points)</strong>
</summary>

<bloquote>
You can get a maximum of 1.5 points in this section:
<ul>
	<li>Client layout present: <strong>0.5</strong></li>
	<li>UI is stetically pleasant: <strong>1.0</strong></li>
</ul>
</bloquote>

</details>

---

:pencil2: *Add your diagrams here*

### Screen workflow

---
<details>
<summary>
:bookmark_tabs:&nbsp;&nbsp;<strong>Content that must be included in the section</strong>
</summary>

<bloquote>
Draw the screen workflow of your client (which are the possible screens that you can access from one specific screen?)

</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 1.0 points)</strong>
</summary>

<bloquote>
	You can get a maximum of 1.0 points in this section:
<ul>
	<li>Workflow diagram available. Navigation is coherent <strong>1.0</strong></li>
</ul>

</bloquote>

</details>

---

:pencil2: *Add your diagrams here*

## Client implementation

---
<details>
<summary>
:computer:&nbsp;&nbsp;&nbsp;&nbsp; <strong>TODO: SOFTWARE TO DELIVER IN THIS SECTION</strong>
</summary>

<bloquote>
<strong>The code repository must contain: </strong>
<ol>
	<li>The source code for the client application.&nbsp;</li>
	<li>External libraries. You can also report them in the <a href="doc/README.md">README.md</a> if the libraries are very big or need to be installed.</li>
	<li>The code for testing the application (if it exists).</li>
	<li>We recommend to include a set of scripts to run your application and tests.</li>
	<li>A <a href="doc/README.md">README.md</a> file containing:
		<ul>
			<li>Dependencies (external libraries)</li>
			<li>How to setup/install the client</li>
			<li>How to configure and run the client</li>
			<li>How to run the different tests of your client (if you have implemented unit testing)</li>
		</ul>
	</li>
</ol>
<strong>NOTE: Your code MUST be clearly documented. </strong>For each public method/function you must provide: a short description of the method, input parameters, output parameters, exceptions (when the application can fail and how to handle such fail). Check Exercise 4 for examples on how to document the code.
<strong> addition, should be clear which is the code you have implemented yourself and which is the code that you have borrowed from other sources.</strong>
</bloquote>

</details>

---

---
<details>
<summary>
:heavy_check_mark:&nbsp;&nbsp;&nbsp;&nbsp; <strong>Evaluation criteria(max 9.5 points)</strong>
</summary>

<bloquote>
	In this section you can get a maximum of 9.5 points.
<ul>
	<li>Instructions to set up the client and run the tests are provided in the <a href="doc/README.md">README.md</a> file<strong>: 0.5</strong>
		<ul>
			<li>this means there should be no undocumented extra steps in running the code/tests!</li>
		</ul>
	</li>
	<li>The code has clear structure and naming for variables and methods<strong>: 1.0</strong></li>
	<li>You have clearly marked which parts of the code are your own work and which is borrowed code<strong>: 0.5</strong></li>
	<li>Client is usable and navigation is coherent (no broken links)<strong>: 1.0</strong></li>
	<li>Demonstrate through a presentation or screenshots that your client fulfills the minimum requirements<strong>: 1.0</strong></li>
	<li>Client works as expected<strong>: 2.0</strong>
		<ul>
			<li>We do not find errors while using the application</li>
		</ul>
	</li>
	<li>The client uses a different API in addition to using your own API (i.e. finds additional information from somewhere else)<strong>: 1.5</strong>
		<ul>
			<li>For full points the client should utilize at least two different methods from the uniform interfaces OR utilize at least 4 differents API calls.</li>
			<li>For full points the functionality provided by the external API should be integrated in the client functionality and not as an incosistent addition.</li>
		</ul>
	</li>
	<li>The client is a true hypermedia client (if you are not using an hypermedia API you won't get these points): <strong> 2.0</strong>
		<ul>
			<li>this means that the client uses the hypermedia links to find URLs, uses forms from the hypermedia to form its requests, follows correctly link relations, workflow is mainly in the server, not the client... etc. If any of these aspects are not considered cannot get full points in this section.</li>
			<li>The ideal client is resistant to changes in the API because it only relies on information it gets from the API in runtime</li>
		</ul>
	</li>
</ul>
</bloquote>

</details>

---

:pencil2: *Implement your client and include a few screenshots of the final version of the client to show that meets the requirements*

## Resources allocation
|**Task** | **Student**|**Estimated time**|
|:------: |:----------:|:----------------:|
|||| 
|||| 
|||| 
|||| 
|||| 