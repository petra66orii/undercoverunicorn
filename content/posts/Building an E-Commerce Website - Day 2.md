---
title: Building an E-Commerce Website - Day 2
description: Blog post series about building and setting up an e-commerce website using Django, Bootstrap and other coding technologies
date: 2025-03-04
draft: false
tags:
  - blog
  - coding
  - e-commerce
  - projects
  - software
  - development
categories:
  - E-Commerce Website Series
---


## Outlining the Battle Plan

Welcome! So today I've done my flow chart, my wireframes and an ERD that will serve as my guiding light in this website-building journey. In this post, I'll pick up from my last [article](Building%20an%20E-Commerce%20Website%20-%20Day%201.md), initialize my repo in VS Code, create our own virtual environment and start documenting my plan in the README.md.

These are part of my course requirements in order to pass this project.

	"Woman, what are you on about? What's a flow chart? What's a wireframe? What are you saying?!"

Fear not! I will explain everything as we go. 🦄

## Getting Started

These are the steps I took to initialize my project, feel free to follow along!
*Note: Before proceeding, ensure you have an IDE installed (like VS Code), Python, Git and you need to have a GitHub account*

1. Create a repository in GitHub
2. Open VS Code - or whatever IDE you prefer
3. Create a new folder on your PC - preferably where you store your projects in general
4. Back in VS Code, go to *File* -> *Open Folder*
5. Select the folder you've just created
6. Go to your *Command Palette* and type *Create Environment*
7. Select *Python: Create Environment*
8. Choose *Venv* from the dropdown
9. Choose your Python version - preferably the more recent, the better
10. You'll notice a new folder *.venv* in your project
11. Add the folder to your *.gitignore* file - if you don't have a *.gitignore* file, simply create one and add *.venv* there
12. Back in GitHub, in your repo, select the green button *Code*
13. Clicking on *SSH*, copy the git clone command followed by your repo link
14. In your IDE terminal, paste the copied command and press *Enter*
15. Congrats, you've connected your GitHub repo to your IDE! Now the fun begins!

## Designing Before Applying 

Well... I lied. We need a plan before jumping in.  

Creating a website is a ton of work, especially if you're going full stack. That's why it is very important to organize yourself and always plan ahead so you don't get overwhelmed in the process.

Writing about your plan is probably the best thing you can do for yourself. That way, your brain will focus more on coming with new ideas instead of trying to juggle and remember what you're trying to do. Not to mention that writing about it helps you understand better the whole process! 🦄

Also, you can make use of very useful diagram and wireframing tools to better visualize your perfect project.

### Wireframes

One crucial part when it comes to front-end software development is envisioning your layout of the website. Before jumping in and writing code, we need to create sketches to have an idea about how our website is going to look like! This is where wireframes come in. They are like the skeleton of the website; they are a great way to figure out what goes where, what are going to be your core components of the website and the main features of your website.

There are a lot of software tools like Figma, Balsamiq, LucidChart and many more that enable you to do exactly that. I use Balsamiq because my school has offered us a key that enabled a free trial for a full year.

From what I know, Balsamiq isn't free. But fortunately, Figma is another great tool for creating wireframes (and from what I've seen, it's a lot more popular and in demand) that you can use for free! They have paid options as well, but if you're just getting started, I'd say Figma is a great option for you.

These are my wireframes, designed with Balsamiq:

<img src="/undercoverunicorn/images/home-page.png" alt="home-page.png">
<img src="/undercoverunicorn/images/product-list.png" alt="product-list.png">
<img src="/undercoverunicorn/images/product-detail.png" alt="product-detail.png">
<img src="/undercoverunicorn/images/shopping-bag.png" alt="shopping-bag.png">
<img src="/undercoverunicorn/images/checkout-page.png" alt="checkout-page.png">
<img src="/undercoverunicorn/images/user-profile.png" alt="user-profile.png">
<img src="/undercoverunicorn/images/blog-page.png" alt="blog-page.png">

### Flow Charts

According to Canva, *"A flow chart is a diagram that shows the steps of a workflow or a process. These flow charts are used to recreate the sequence of actions or information needed for training, documenting, planning, and decision-making. They often use symbols, shapes, and arrows to illustrate how one step leads to another."*

Flow charts are very useful when you're trying to figure out the logic within your website. What happens when you click a certain button? Should there be a different result if a user is logged in or not? What process are you expecting from a certain page?

These are questions that can help you figure out how your flow chart works. You can use websites like draw.io, LucidChart or Mermaid.live. I personally used Mermaid.live to draw the flow chart for me; I previously used draw.io which turned out to be very frustrating for me, personally. They're free anyway so give it a go!

If you're using Mermaid, you don't have to sketch anything. All you have to do is to type into a text editor how the process flow works. I've attached my flow chart with the syntax written below. If you paste this in the left-hand side of the website, the program will generate a flow chart for you to download. It's so lovely! 🧜‍♀️

graph TD;

    A[Start: User lands on site] --> B[Browse Products]

    B -->|Add to Cart?| C[View Cart]

    B -->|No| B

    C -->|Proceed to Checkout?| D[Login/Register]

    C -->|No| C

    D --> E[Enter Shipping & Payment Details]

    E --> F[Confirm Order]

    F -->|Payment Successful?| G[Thank You Page]

    F -->|No| H[Retry Payment]

    H --> F

This is the result: 
<img src="/undercoverunicorn/images/flow-chart.png" alt="flow-chart.png">

### ERD

When planning a website, another crucial part is **data storage**. You need to store user data, products, blog posts, anything that contains information requires a database. The most popular databases are MySQL, PostgreSQL (the database I use) or ElephantSQL. There are other NoSQL databases available like MongoDB, but I haven't used them as of yet.

So far I have configured 8 models, the 9th one is built-in with Django so I don't need to create a new one. The models are displayed in the ERD below. 

Entity Relationship Diagram, also known as ERD, is **a structural diagram for use in database design**. An ERD contains all of the database models and connects them thorough foreign keys.

To provide an example, the model *Product* contains the field *category*, which is a foreign key that connects *Products* to the *Category* model. Each model contains information about users, products, orders and blog posts.

<img src="/undercoverunicorn/images/ERD-diagram.png" alt="ERD-diagram.png">

### README

In my case, I also have to write a comprehensive README that explains how the website was built, my thought process around this project and basically pitch my project as a business solution. The README document is very important when comes it to any website or package. It contains information on how to install and use software. My README is easily accessed in my [Honeypot](https://github.com/petra66orii/honeypot) repo.

I recommend having a thoroughly documented README. Why? 

Because I said so. 😊

I'm joking! 

You should have one because in case you return to your project after a few months, you probably wouldn't remember much about it. Also it's nice to have in case other people want to build upon your project!

## Ending Comments

Having a plan and good documentation is crucial before jumping into coding. It helps organize better and you know what to focus on first, without dividing yourself into 1000 parts.

*Be kind to yourself. Keep achieving!*

## References

Wireframes

* [Balsamiq](https://balsamiq.com/)
* [Figma](https://www.figma.com/pricing/#figma)

Flow Charts

* [LucidChart](https://www.lucidchart.com/pages)
* [draw.io](https://app.diagrams.net/)
* [Mermaid](https://mermaid.live/)

ERD Diagrams

* [DBDiagram](https://dbdiagram.io)
