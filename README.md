# Wiki

#### Video Demo: [Wiki](https://youtu.be/k8kBOH-9AWA)

## Problem to Solve

Given the Internet Age of 2024, we have Wikipedia, an online encyclopedia, where each entry on a specific topic can be accessed by visiting a unique URL. While these entries are rendered as HTML on the web, writing every entry directly in HTML can be cumbersome and inefficient. A more user-friendly approach is to use a simpler markup language that is easier to write and edit, while still supporting the necessary formatting.

This project aims to create a Wikipedia-like web application where users can access, create, and edit encyclopedia entries. The entries are stored in Markdown, a lightweight, human-readable markup language. When users view an entry, the Markdown content will be dynamically converted into HTML, making the application user-friendly both for content creators and viewers. The challenge lies in implementing the functionality to manage, display, and render these Markdown-based entries into a structured web interface.

## Background

Wikipedia serves as a vast online repository of knowledge, with each topic having its own dedicated entry accessible via a unique URL. For instance, visiting `/wiki/HTML` on Wikipedia retrieves the entry for HTML. While Wikipedia pages are rendered in HTML, writing each page manually in HTML can be inefficient and error-prone, especially for non-technical users.

To streamline the process of creating and editing content, Wikipedia uses a lightweight markup language called Wikitext. In this project, however, the focus is on using Markdown, a simpler and more human-friendly markup language. Markdown allows users to create content with easy-to-understand syntax for common formatting elements such as headings, bold text, links, and lists.

By storing each encyclopedia entry as a Markdown file, the web application ensures that entries are easy to write, edit, and maintain. When users request an entry, the application dynamically converts the Markdown content into HTML for rendering in the browser. This approach combines the simplicity of Markdown with the functionality of HTML, allowing for a more intuitive user experience. The challenge lies in building a system that handles the storage, conversion, and display of these entries while providing a seamless user interface for both browsing and editing content.

## Understanding

The Wiki project is a Django-based web application that mimics the functionality of Wikipedia, allowing users to view, create, and edit encyclopedia entries. The project structure is set up within a single Django app called encyclopedia, which provides the foundation for handling the content and rendering it into a web interface.

#### URL Configuration:
The URLs for the encyclopedia app are defined in `encyclopedia/urls.py`. The default route points to the index view, which displays a list of all the current encyclopedia entries. As you develop the application, this URL configuration will be expanded to include additional routes for creating, editing, and viewing individual entries.

#### Utility Functions:
In encyclopedia/util.py, several helper functions are provided to manage the encyclopedia entries:
* `list_entries`: Returns a list of all encyclopedia entry names.
* `save_entry`: Saves a new entry to the encyclopedia. This function requires a title and content (in Markdown format) and stores it as a Markdown file in the entries/ directory.
* `get_entry`: Retrieves an entry by its title and returns the Markdown content if the entry exists. If the entry does not exist, it returns None. These utility functions streamline the process of interacting with encyclopedia entries, making it easy to manage and retrieve Markdown files without having to manually handle file I/O operations.

#### Entry Storage:
Each encyclopedia entry is stored as a separate Markdown file in the `entries/` directory. These files contain the content of the entries, which will later be rendered as HTML when displayed in the web interface. By leveraging Markdown, users can write and format content in a simple, human-readable way, while the application dynamically converts it to HTML for viewing.

#### Views and Templates:
The current implementation of `encyclopedia/views.py` includes a single view, the index view, which is responsible for rendering the home page of the encyclopedia. This view calls the `util.list_entries` function to retrieve a list of all existing entries and passes it to the `encyclopedia/index.html` template for display.

The `index.html` template inherits from a base template `layout.html` and defines the content of the home page. The page displays a list of all encyclopedia entries, presented as an unordered list. The broader page structure, defined in `layout.html`, includes a sidebar with a search field, a home link, and placeholder links for creating a new page or viewing a random entry (which are not yet functional but will be implemented as you progress).

#### Template Structure:
* `layout.html`: Defines the main layout of the Wiki application, including the sidebar and general structure. It provides a consistent look and feel for all pages of the application, ensuring that features like navigation and search are present throughout.
* `index.html`: Displays the list of encyclopedia entries retrieved from the index view, organized in an unordered list. This template extends `layout.html`, ensuring that the common page structure is preserved while focusing on displaying the list of entries.

By following this structure, the application is designed to be modular and extensible. You can easily add new views and templates to handle specific functionality, such as viewing individual entries, creating new ones, or editing existing content.

## Specification

The Wiki project allows users to view, create, edit, search, and explore encyclopedia entries. The application will store each entry in Markdown format and render it as HTML for the user. Below are the specific functionalities that must be implemented:

#### Entry Page:
* Route: `/wiki/TITLE`
    * When a user visits `/wiki/TITLE`, the page should display the content of the encyclopedia entry corresponding to TITLE.
    * The content of the entry should be retrieved using the get_entry function from `util.py`.
    * If the entry does not exist, display an error page informing the user that the requested page was not found.
    * If the entry exists, display the content of the entry in HTML format, with the page title reflecting the name of the entry.

#### Index Page:
* Route: `/`
    * Update the `index.html` template to display clickable links for each encyclopedia entry.
    * When a user clicks on an entry name, they should be redirected to that entry’s page.

#### Search:
* Search Box: In the sidebar of `layout.html`, include a search field for users to search for encyclopedia entries.
* If the search query matches exactly with the title of an encyclopedia entry, redirect the user to that entry's page.
* If the search query matches partially (as a substring) with any entry, display a search results page with a list of matching entries.
* Each matching entry in the search results should be clickable, redirecting the user to the respective entry page.
* If no entries match, display a message indicating no results were found.

#### New Page:
* Route: `/new`
    * Clicking the "Create New Page" link in the sidebar should take the user to a page where they can create a new encyclopedia entry.
    * The page should include:
        * A text input for the entry title.
        * A textarea for entering the Markdown content of the entry.
        * A save button to submit the form.
    * When the user saves the new entry:
        * If an entry with the given title already exists, display an error message.
        * If the title is unique, save the new entry using the `save_entry` function, and redirect the user to the new entry’s page.

#### Edit Page:
* Route: `/wiki/TITLE/edit`
    * On each entry page, include a link to edit the entry’s content.
    * Clicking the edit link should take the user to an edit page where the Markdown content of the entry is pre-loaded into a textarea.
    * The user can make changes and save the updated content.
    * After saving, the updated content should be saved using the `save_entry` function, and the user should be redirected back to the updated entry page.

#### Random Page:
* Route: `/random`
* Clicking the "Random Page" link in the sidebar should take the user to a randomly selected encyclopedia entry.
* The random entry should be chosen from the list of all entries.

#### Markdown to HTML Conversion:
* On each entry’s page, the content of the entry (stored in Markdown format) should be converted to HTML before rendering.
* Use the python-markdown2 package to handle Markdown-to-HTML conversion.

Ensure that headings, bold text, links, lists, and other Markdown syntax are correctly converted to their HTML equivalents before being displayed on the entry page.

