<!-- Improved compatibility of back to top link: See: https://github.com/EmadHelmi/herodotus/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="TODO">
    <img src="static/imgs/logo.png" alt="Logo" height="200">
  </a>

<h3 align="center">Herodotus</h3>

  <p align="center">
    An awesome enhanced python logger
    <br />
    <a href="TODO"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="TODO">Examples</a>
    ·
    <a href="TODO">Report Bug</a>
    ·
    <a href="TODO">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#the-history-behind-the-project">The history behind the project</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

### The history behind the project

Python [logging][python-logging-url] package is a powerful tool for logging your messages into any stream.
From a file to third party service, like [Elasticserarch][elastic-url].

But one day in a project I needed to log some messages through many streams with different severities.
For example I want a logger object in which three handlers one for a rotating file handler, one for stdout and one for
elasticsearch.
But I wanted to send each severity to a specific stream. And also I wanted to colorize the stdout log but not the one in
the file.

When I used something like this:

```python
import logging
import some_colorizer_function

my_logger = logging.getLogger("my_logger")
my_logger.debug(
    some_colorizer_function("some message with %s"),
    "args"
)
```

it sends a nice colorized output to the stdout. But an ugly text (with ansi color symbols) sent to the Elasticsearch or
wrote in the file.
So I decided to make some enhancements on the logging package and also decided to publish it. So please fill free to
contribute.

### The naming convention

[Herodotus][Herodotus-wiki] was an ancient Greek historian known as the "Father of History."
He wrote the book "The Histories," one of the earliest historical works.
This book covers various subjects such as history, geography, cultures, civilizations, and wars.
He combined accurate descriptions of events with engaging storytelling.
His work is a blend of historical analysis and cultural narratives, making him a significant figure in the development
of historical writing.

<!-- GETTING STARTED -->

## Getting Started

I've also created a pypi packge for this library. So you can easily use and install it with pip or clone the project.

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't
rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<!-- USAGE EXAMPLES -->

## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos
work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->

## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/EmadHelmi/herodotus/issues) for a full list of proposed features (
and known issues).



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.



<!-- CONTACT -->

## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites
to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/EmadHelmi/herodotus?style=for-the-badge

[contributors-url]: https://github.com/EmadHelmi/herodotus/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/EmadHelmi/herodotus?style=for-the-badge

[forks-url]: https://github.com/EmadHelmi/herodotus/network/members

[stars-shield]: https://img.shields.io/github/stars/EmadHelmi/herodotus?style=for-the-badge

[stars-url]: https://github.com/EmadHelmi/herodotus/stargazers

[issues-shield]: https://img.shields.io/github/issues/EmadHelmi/herodotus?style=for-the-badge

[issues-url]: https://github.com/EmadHelmi/herodotus/issues

[license-shield]: https://img.shields.io/github/license/EmadHelmi/herodotus?style=for-the-badge

[license-url]: https://github.com/EmadHelmi/herodotus/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://www.linkedin.com/in/emad-helmi-1aa321135/

[python-logging-url]: https://docs.python.org/3/library/logging.html

[elastic-url]: https://www.elastic.co/

[Herodotus-wiki]: https://en.wikipedia.org/wiki/Herodotus

[Python.badge]: https://img.shields.io/badge/Python-20233A?style=for-the-badge&logo=python&logoColor=61DAFB

[Python-url]: https://python.org
