# Lab 29 - DjangoX

*Author*: Kassie Bradshaw

My *application* is called **booktracker**

[Link to my GitHub](https://github.com/kassiebradshaw/potential-eureka)

[Link to my tests](booktracker/tests.py)

---

## Overview

It is quite common to set up your Django projects the same way every time.

Some of those common tasks are...

* Create a custom user
* Configure static assets
* Add authentication
* Set up styling
* Install common libraries
* Wire up 3rd party development tools

Repeating these steps over and over violates the DRY (Don't Repeat Yourself) rule. So pro developers usually create a skeleton application they use to start off their projects.

Luckily for us, there's already a great example of such a skeleton - [DjangoX](https://github.com/wsvincent/djangox)

## Feature Tasks & Requirements

* [x] Create a website using DjangoX as a template
* [x] Name your repo whatever you like
* [x] Create a Django app of your choosing
* [x] The specific functionality of the site is up to you but you should have a model that makes use of `get_user_model`

## Implementation Notes

DjangoX does not use Poetry out of the box. So you'll need to look at the files DjangoX does use to see which dependencies are used.

* [x] View `Pipfile` and note the packages section.
  * [x] Use `poetry add` to install packages listed in Pipfile
* [x] Delete the configuration files that aren't needed anymore since we're using Poetry
  * [x] Pipfile
  * [x] Pipfile.lock
  * [x] Dockerfile
  * [x] Docker-compose.yml
  * [x] requirements.txt

## User Acceptance Tests

* [x] Verify that your pages render as expected

## Stretch Goals

* [ ] Add social authentication
* [ ] Add images to your site
