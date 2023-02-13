# Testing

# Browser Compatibility
---
This website has been tested and operates as expected on Chrome, Microsoft Edge, Safari, Firefox and Opera browsers.

The website has been tested using Chrome Devloper Tools for it's responsiveness on various device viewports.

It responds as intended on the following devices:

* iPhone XR 

* iPhone 12 Pro

* Pixel 5

* Samsung Galaxy S20 Ultra

* iPad Air

* iPad Mini

* Surface Duo

I personally tested the website on my Google Pixel 7 Pro.

# User Stories Testing

* First Time User
    * I want to understand the main purpose of the website.
        * On the homepage there is a brief description of who and what the website is for.

        ![FTU1](/TESTING/FTU1.png)

    * I want to be able to easily understand and navigate the website.
        * There is a navigation bar along the top of every page. Clicking on the logo will return the user to the homepage. There are buttons throughout the website with a clear description of their purpose. There is a Back To Top butoon at the bottom of the definitions page.

        ![FTU2](/TESTING/FTU2.png)

        ![FTU3](/TESTING/FTU3.png)

    * I want to find terminology related to reptile keeping.
        * On the homepage, the dictionary with all the definitions within the database can be found along with a search bar.

        ![FTU4](/TESTING/FTU4.png)

     * I want to be able contribute to the dictionary/glossary.
        * Once a user has registered they are then able to add words to the dictionary.

        ![FTU5](/TESTING/FTU5.png)

* Returning User
    * I want to be able to edit or remove my previous contributions.
        * From within the profile page, a user can edit or remove their contributions.

        ![RU1](/TESTING/RU1.png)

        ![]()

        ![]()

    * I want to be able to contact the website owner.
        * 

        ![RU2](/TESTING/RU2.png)

    * I want to be able to register and/or login.
        * The login and register pages are found within the navigation bar.

        ![RU3](/TESTING/RU3.png)

* Site Owner
    * I want the website to be easily found using search engines.
        * Each webpage has been run through lighthouse which produces a score for Search Engine Optimization. These checks ensure that the page is optimized for search engine results ranking.

    * I want the website to clearly indicate it's purpose.
        * On the homepage there is a brief description of who and what the website is for.

        ![FTU1](/TESTING/FTU1.png)

    * I want site visitors to be able to easily locate the definitions and their contributions.
        * All the words from the dictionary will be on the home page, and if a user wants to view only their submissions, this can be done from the profile page.

        ![FTU4](/TESTING/FTU4.png)

        ![RU1](/TESTING/RU1.png)

    * I want site visitors to be able to register and login.
        * The login and register pages are found within the navigation bar.

        ![RU3](/TESTING/RU3.png)

---

# Code Validation

## HTML

Each page of the website was run through the W3C Markup Validation Service to ensure there were no errors. Could only test on certain pages due to the need to login.

* * definitions.html
    ![home](/TESTING/home.png)

* login.html
    ![login](/TESTING/login.png)

* register.html
    ![register](/TESTING/register.png)


## CSS

The website's CSS was run through the W3C CSS Validation Service (Jigsaw). No issues or errors were found.

* style.css
    ![css](/TESTING/css-validator.png)
---

# Lighthouse

## Desktop Results

* definitions.html
    ![home](/TESTING/M-HOME.png)

* login.html
    ![login](/TESTING/M-LOGIN.png)

* register.html
    ![register](/TESTING/M-REGISTER.png)

* profile.html
    ![profile](/TESTING/m-profile.png)

* add_word.html
    ![addword](/TESTING/m-addword.png)

* edit_word.html
    ![editword](/TESTING/m-editword.png)

## Mobile Results

* definitions.html
    ![home](/TESTING/DT-HOME.png)

* login.html
    ![login](/TESTING/DT-LOGIN.png)

* register.html
    ![register](/TESTING/DT-REGISTER.png)

* profile.html
    ![profile](/TESTING/DT-PROFILE.png)

* add_word.html
    ![addword](/TESTING/DT-ADDWORD.png)

* edit_word.html
    ![editword](/TESTING/DT-EDITWORD.png)
---

# Debugging

## Resolved

* Registration form was not saving user input to MongoDB collection and was not displaying flash message confirmation.
    
    * Eventually realised that I had not put "method='POST'" into register.html form.

## Unresolved

* Unable to change input colour for "word defintion" on add_word.html.

* Unable to view all contributions on user's profile page. Only one is being displayed.

* Unable to make 404 page functional. Tried using the Flask documentation and other resources to no avail.