# Static Site Generator From Markdown

A static website generator that serves a website given a folder of markdown files.

## Contents
* [Usage](#usage)
  * [Prerequisites](#prerequisites)<br>
  * [Static and Content Directories Preparation](#static-and-content-directories-preparation)<br>
  * [Running The Application](#running-the-application)<br>
* [Example Demonstration](#example-demonstration)
* [Unit Tests](#unit-tests)

## Usage
### Prerequisites
Ensure you have Python 3 installed on your system.

### Static and Content Directories Preparation.
You need to prepare a "static" folder and a "content" folder in your project root directory.

The 'static' folder should contain any files that will be referenced by your webpages. Ensure index.css file should be at the top of the directory, since all generated pages will reference this as their stylesheet. The file structure of the static folder will be reflected in the public folder that contains the generated pages.

The 'content' folder should contain all markdown files you would like to generate into webpages. The file structure of the 'content' folder will be reflected in the public folder that contains the generated pages.

For more guidance on the 'static' and 'content' folders, please follow the example at [Example Demonstration](#example-demonstration) and study the contents of the example files.

### Running the Application
From the project root directory, use the `main.sh` shell script to run the application and start your web server on port 8888:

```bash
./main.sh
```

*[Back To Top](#static-site-generator-from-markdown)* <br>
## Example Demonstration

Copy the example 'static' and 'content' directories to your workspace by running the following command in your project's root directory.

```bash
cp -r ./example/* .
```

Generate your webpages to a 'public' folder and serve them to port 8888 using the `main.sh` shell script. To do so run the following command in your project's root directory.

```bash
./main.sh
```
You can now view the generated pages at the following URLs:
```
http://localhost:8888
http://localhost:8888/majesty/
```

To stop the script, press `Ctrl + C` in the terminal you ran it in.

*[Back To Top](#static-site-generator-from-markdown)* <br>
## Unit Tests
For effortless devlopment and maintenance, this project uses a high coverage of unit tests throughout development:

![image](https://github.com/adamhu714/static-site-generator/assets/105497355/c35f6060-04d1-49e4-8568-e81d2c1ba0c1)


*[Back To Top](#static-site-generator-from-markdown)* <br>
