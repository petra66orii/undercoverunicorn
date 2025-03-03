---
title: Building an E-Commerce Website - Day 1
description: Initial planning for an e-commerce website project. This includes coding technologies used like Django and website features like user authentication.
date: 2025-02-26T19:07:00Z
draft: false
tags:
  - blog
  - coding
  - marketing
  - e-commerce
  - SEO
  - projects
categories:
  - E-Commerce Website Series
---


# Building an E-Commerce Website - Day 1

## My Coding Project Series

This post is the first of many where I will be writing about building an e-commerce website from start to finish. I will write about how to start a project in VS Code (you can use whatever IDE you desire, I prefer VS Code), connect it to GitHub, install all the packages required, and more! 

I'm so excited for this! 

So join me in this wonderful journey of coding and creating a website of your own! 💜

## What Is E-Commerce?

According to Amazon, *"Ecommerce or "electronic commerce" is **the trading of goods and services online**. The internet allows individuals and businesses to buy and sell an increasing amount of physical goods, digital goods, and services electronically."*

So basically, any website that sells something, whether it's physical products, services, or digital products, is considered an e-commerce website.

E-commerce websites have completely changed the game when it comes to business. It is a lot more effortless, all you need is a laptop/smartphone with an Internet connection, a credit card and you're good to go! 

Although it's not that easy. Some websites can be actual scams and you can end up with no product, and no money! So, always check the reviews and ensure the website you're planning to purchase from is reliable.

## What Am I At?

Sooo, I'm currently studying software development within Code Institute's course "Diploma in Full Stack Software Development (E-commerce Applications)" and as I'm nearing the end of the course (I'm not sponsored by them in any way), I have to plan, build and deploy an e-commerce website. I have a list of prerequisites and technologies that I need to use, and I have to follow the Agile methodology to showcase my thought process when it comes to creating websites (*article on the Agile methodology coming up soon!*).

These are the technologies that I am required to use and which I'm most comfortable with at the moment:

**Backend**: Django, Python
**Frontend**: HTML, CSS, Bootstrap, JavaScript
**Database**: PostgreSQL
**Version Control**: Git, GitHub
**Hosting**: Heroku

I have the liberty to choose what I want the website to be about, so I chose honey products, since there is a lot in information regarding honey products, honey usage and beekeeping. And let's face it, everyone loves honey!

I think it's safe to say that I'm not a very experienced developer yet, but I'm definitely a lot more confident than I was a year ago! I'm also a firm believer that building confidence is key when it comes to learning new skills like software development. The perfect way to build confidence when learning software development is ==to do projects==. Building projects are a great way of showcasing your skills, and you're going to learn A LOT more than if you'd just learn the theory.

I'm not saying to not learn theory as well, theory is very important, it can spare you from some very annoying bugs and you don't need to invent the wheel again. But it's crucial to apply the theory.

I used to just watch videos and take notes, and I wasn't practicing at all. Needless to say, when I had to create my first project using only HTML and CSS, I was frightened, even though the theory of these two languages was very easy and logical. It's that panic setting in, where you ask yourself: 

	"Where do I start? What do I do? What if I make a mistake?!"

It's fine. 

You'll make mistakes. Tons of them, actually.

But if you create a mindset of trying to resolve and learn from them, these mistakes are worth it. Because they'll help you become a great software developer. And since technologies are changing all the time, you'll constantly be learning! 

This isn't my first website that I have to build; this course doesn't use exams to score students, but it uses projects. There are different courses depending on what you prefer. For example, I had 5 projects across the course that I had to complete in order to graduate from this course, and my capstone project (the one that I'm writing about right now) is *E-commerce Applications*. Other students would've had *Predictive Analytics* or *Advanced Frontend*. 

I'll link my GitHub where all my portfolio projects are pinned on my profile. Feel free to check them out, I'll also look into writing about them in future articles! 😊

Also, check my GitHub Issues regarding this project! I use them to plan every step of this project, ensuring a seamless integration of technologies and as less time wasted as possible. Along the way I will definitely add more issues if I come across bugs or realise that I missed out on something.

[Link here](https://github.com/petra66orii/honeypot/issues) 😀

### Features - Honeypot

The features that will be present in this website are pretty basic considering that it is an e-commerce website. It will have user authentication, payment options, commenting and reviewing products, a checkout section, and even a blog where users can find out more about the benefits of honey and even a few recipes!

I will use two existing websites for a bit of inspo when it comes to designing: [Honey Heaven](https://www.honeyheaven.co.uk/) (based in UK) and [Leahy Beekeeping](https://www.leahybeekeeping.com/) (based in Ireland). They look good to me and I can use them to see what can I improve upon. 

#### Landing Page

There will be a landing page where the latest offers will be displayed at the top of the page,
followed by reviews and the best rated products. The purpose of this page is to retain the user on this website for as much time as possible and to purchase products.

The hero image will be a nice background of honey pouring down in different foods, giving the website a nice aesthetic feeling to the product being sold. There will also be multiple reviews where users can read about how pleased the buyers are with the products bought.

#### User Authentication

In order to make a purchase, users will have to sign in or create an account if they don't have one. This feature is made possible by Django's AllAuth package, which will enable the user to securely log in/sign up. The sign in/log out/sign up templates are also automatically generated by AllAuth, but they can be easily customised. If you don't have a clue what I'm on about, not to worry, I will dedicate an article solely to setting up AllAuth and all of its perks. ✨

#### Products Page

The products page will contain a list of the products being sold. Each product has a price, rating and an image of the said product.

#### User Profiles

Whenever a user registers on the website, the website will automatically create a new profile for them. Users can then add their personal details that will simplify the checkout process, ensuring a pleasant UX, so that our customers will always return to this website for honey product purchases. 

#### Shopping Bag

The shopping bag will be where all the products that the user added to the basket. They will be able to see the total price they'll pay, and it also provides a space where they can save the products desired whilst still looking around the website.

#### Checkout

The checkout is where the magic begins. It's also where security is the most important, because users will be inputting their credit card details here, and we also wanna make sure that the page processes the payment and the order. I'll be using Stripe API for this and I'll add webhooks that will follow the signals and alert us if something is wrong.

#### Blog

There is also going to be a blog page where users can look up benefits of consuming honey, recipes and much more. This page's purpose is to engage with the customers by enabling comments on these posts where they can share their input! 

## This Is Only the Beginning

Now I've outlined the main features, this project will be the most complex thing I've done so far.

But I'm so excited about it I feel like I need to scream out of excitement! AAAHH!!

Ok, I'm good now. I didn't actually scream because the neighbors might think I'm insane... which I'm not!

Anyway, on the next day, I will design the wireframes and outline flow charts and ERD diagrams for my PostgreSQL models.

Thank you for reading this and I hope I'll inspire you to create your own project!

*Be kind to yourself. Keep achieving!*