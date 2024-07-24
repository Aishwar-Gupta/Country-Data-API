
<div>
  <h3 align="center">Country Data API</h3>

  <p align="center">
    An API to access information about different countries according to the World Bank.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
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
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I created this project to scrape country date from World Bank's official website.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Below is the list of major frameworks/libraries used to bootstrap the project.

* [![Python][Python]][Python-url]
* [![Selenium][Selenium]][Selenium-url]
* [![FastAPI][FastAPI]][FastAPI-url]
* [![CSS3][CSS3]][CSS3-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Follow the instructions below to get a local copy of the project on your machine and run it to get the required data and functionalities.
To get a local copy up and running follow these simple steps.

### Prerequisites

It is assumed that python3 is installed on the machine and the other prerequisites are as follows:
* Selenium
  ```sh
  pip3 install selenium
  ```
* Web-Driver Manager
  ```sh
  pip3 install webdriver-manager
  ```
* FastAPI
  ```sh
  pip3 install fastapi
  ```
* Uvicorn
  ```sh
  pip3 install uvicorn
  ```
Alternatively, you can run the requirements.txt to get all the installations done automatically.

### Installation

_Below are the steps on installing and setting up your app. This project doesn't rely on any external dependencies or third-party services.

1. Install the above mentioned requirements before proceeding.
2. Clone the repo
   ```sh
   [git clone https://github.com/your_username_/Project-Name.git](https://github.com/Aishwar-Gupta/Country-Data-API/tree/main)
   ```
3. Run the command below
   ```sh
   python3 countryAPI.py
   ```
4. Enter your URL endpoints in the Chrome Browser. You can alternatively skip watching the bot over browser by removing the code below.
   ```js
   options.add_experimental_option("detach", False)  # stop from closing the chrome after done
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use the API enter the URL endpoints of the required data in the address bar of the Chrome Browser. By default, the API runs at port 8000, but can be changed by changing in the countryAPI.py file. Details for the API endpoints can be found below:
 ```js
   "/all-countries": "List of all the countries in the world.",
   "/{Alphabet}": "List of all countries that start with that {Alphabet}.",
   "/population/{country}": "Returns the Population of the {country}.",
   "/country-population/{count}": "Return {count} number of country's population in alphabetical order."}
   ```

_For more details about the data, please refer to the [World Bank Website]([https://example.co](https://data.worldbank.org/country))_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under no licence. Personal Project!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Aishwar Gupta 

Project Link: [https://github.com/your_username/repo_name]([https://github.com/Aishwar-Gupta/Country-Data-API/tree/main)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/

[Selenium]: https://img.shields.io/badge/-selenium-CB02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/

[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/

[CSS3]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://css3.com/


[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
